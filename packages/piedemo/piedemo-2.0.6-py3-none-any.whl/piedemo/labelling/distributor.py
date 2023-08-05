import os
from datetime import datetime, timedelta
import math

import numpy as np
from bson import ObjectId
from pymongo.database import Database


class Distributor(object):
    def __init__(self,
                 length,
                 db: Database):
        self.length = length
        self.db = db

    def generate_token(self, user_id, hashed_password):
        pass

    def is_valid_token(self, token):
        pass

    def count(self):
        raise NotImplementedError()

    def next_job(self):
        raise NotImplementedError()

    def assign_job(self, job, user_id):
        if job["user_id"] is not None:
            raise RuntimeError("Can't assign already assigned job, please create new")
        if self.db.job.find_one({"user_id": user_id, "ended_at": None}) is not None:
            raise RuntimeError("Can't assign job for user, that already have a job")
        self.db.job.update_one({"_id": job["_id"]},
                               {"$set": {"user_id": user_id, "assigned_at": datetime.now()}},
                               upsert=False)

    def deassign_job(self, job):
        self.db.job.delete_one({"_id": job["_id"]})

    def create_job(self,
                   indices):
        indices = list(indices)
        if not (0 <= min(indices) < max(indices) < self.length):
            raise RuntimeError("Bad job configuration")

        result = self.db.job.insert_one({
            "indices": indices,
            "created_at": datetime.now(),
            "assigned_at": None,
            "ended_at": None,
            "user_id": None,
            "started_at": [[] for _ in range(len(indices))],
            "submit_count": [0 for _ in range(len(indices))],
            "submit_at": [[] for _ in range(len(indices))],
            "comments": [[] for _ in range(len(indices))],
        })
        return self.db.job.find_one({"_id": result.inserted_id})

    def add_comment(self, job, obj_id, user_id, comment: str, checked: bool):
        self.db.job.update_one({"_id": job["_id"]},
                               {"$push": {
                                   f"comments.{obj_id}": {
                                       "user_id": user_id,
                                       "comment": comment,
                                       "checked": checked,
                                   }
                               }})

    def get_job(self, user_id):
        job = self.db.job.find_one({"user_id": user_id, "ended_at": None})
        if job is None:
            job = self.next_job()
            if job is not None:
                self.assign_job(job, user_id)
        return job

    def get_job_by_id(self, job_id):
        if job_id is None:
            return None
        return self.db.job.find_one({"_id": ObjectId(job_id)})

    def job_stats(self, job):
        job = self.db.job.find_one({'_id': job['_id']})
        full_duration = None  #(job['ended_at'] - job['created_at']).total_seconds()
        user_duration = None  # (job['ended_at'] - job['assigned_at']).total_seconds()
        return {
            'user_id': [job['user_id']],
            'full_duration': [full_duration],
            'user_duration': [user_duration],
            'number_elements': [len(job['indices'])],
        }, {
            'task_durations': [np.mean([(job['submit_at'][i][j] - job['started_at'][i][j]).total_seconds()
                                        for j in range(len(job['submit_at'][i]))])
                               for i in range(len(job['indices']))],
            'submit_count': [job['submit_count'][i] for i in range(len(job['indices']))],
        }

    def daily_stats(self):
        assigned_jobs_count = self.db.job.count_documents({})
        finished_jobs_count = self.db.job.count_documents({"ended_at": {"$ne": None}})

        if assigned_jobs_count == 0 or finished_jobs_count == 0:
            return {}

        start_date = self.db.job.find_one(sort=[("assigned_at", 1)])["assigned_at"].date()
        end_date = self.db.job.find_one({"ended_at": {"$ne": None}},
                                        sort=[("ended_at", -1)])["ended_at"].date()
        start_date = datetime.combine(start_date, datetime.min.time())
        end_date = datetime.combine(end_date, datetime.min.time())
        total = self.count()

        # Daily metrics
        d = start_date
        td = timedelta(days=1)

        daily_metrics = []

        while d <= end_date:
            daily_metrics.append({
                "date": d,
                "assigned_jobs_count": self.db.job.count_documents({"assigned_at": {"$gte": d, "$lt": d + td}}),
                "ended_jobs_count": self.db.job.count_documents({"ended_at": {"$gte": d, "$lt": d + td}}),
                "assigned_and_not_done_count": self.db.job.count_documents({"assigned_at": {"$gte": d, "$lt": d + td},
                                                                            "$or": [{"ended_at": {"$gte": d + td}}, {"ended_at": None}]}),
                "progress": self.db.job.count_documents({"ended_at": {"$lt": d + td}}) / self.count(),
                "active_users": len(self.db.job.distinct("user_id", {"ended_at": {"$gte": d, "$lt": d + td}})),
            })
            d += td
        return daily_metrics

    def stats(self):
        users = self.db.job.distinct("user_id")
        if len(users) == 0:
            return {}
        start_date = self.db.job.find_one(sort=[("assigned_at", 1)])["assigned_at"].date()
        end_date = self.db.job.find_one(sort=[("ended_at", -1)])["ended_at"]
        if end_date is None:
            end_date = start_date
        else:
            end_date = end_date.date()
        end_date = max(end_date, self.db.job.find_one(sort=[("assigned_at", -1)])["assigned_at"].date())
        start_date = datetime.combine(start_date, datetime.min.time())
        end_date = datetime.combine(end_date, datetime.min.time())
        d = start_date
        td = timedelta(days=1)
        result = {user_id: [] for user_id in users}
        result["__cumsum"] = []
        result["__sum"] = []

        assigned = 0
        ended = 0
        while d <= end_date:
            for user_id in users:
                assigned_jobs = list(self.db.job.find({'user_id': user_id,
                                                       "assigned_at": {"$gte": d, "$lt": d + td}}))
                ended_jobs = list(self.db.job.find({'user_id': user_id,
                                                    "ended_at": {"$gte": d, "$lt": d + td}}))
                result[user_id].append({
                    "date": d,
                    "assigned": len(assigned_jobs),
                    "ended": len(ended_jobs),
                    "assigned_jobs": [str(job['_id']) for job in assigned_jobs],
                    "ended_jobs": [str(job['_id']) for job in ended_jobs],
                })

            assigned_today = sum([result[user_id][-1]["assigned"] for user_id in users])
            ended_today = sum([result[user_id][-1]["ended"] for user_id in users])
            result["__sum"].append({
                "date": d,
                "assigned": assigned_today,
                "ended": ended_today,
            })

            assigned += assigned_today
            ended += ended_today

            result["__cumsum"].append({
                "date": d,
                "assigned": assigned,
                "ended": ended,
            })

            d += td
        return result

    def finish_job(self, job):
        ended_at = datetime.now()
        self.db.job.update_one({"_id": job["_id"]},
                               {"$set": {"ended_at": ended_at}})

    def submit(self, job, obj_id,
               started_at,
               submit_at):
        if not (0 <= obj_id < len(job['indices'])):
            raise RuntimeError("obj id missing range")
        print(job)

        self.db.job.update_one({"_id": job["_id"]},
                               {"$inc": {f"submit_count.{obj_id}": 1},
                                "$push": {f"submit_at.{obj_id}": submit_at,
                                          f"started_at.{obj_id}": started_at}},
                               upsert=False)

    def missing_index(self):
        created = set()
        for job in self.db.job.find():
            created.update(list(job['indices']))
        return sorted(list(set(range(self.length)).difference(created)))


class SimpleDistributor(Distributor):
    def __init__(self, length, db, n_per_batch):
        super(SimpleDistributor, self).__init__(length, db)
        self.n_per_batch = n_per_batch

    def count(self):
        return math.ceil(self.length / self.n_per_batch)

    def next_job(self):
        indices = self.missing_index()[:self.n_per_batch]
        print("Indices:", indices)
        if len(indices) == 0:
            return None
        job = self.create_job(indices)
        print("Created job: ", job)
        return job
