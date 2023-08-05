import copy
import pandas as pd
from ...fields.grid import VStack, HStack
from ...fields.inputs.hidden import InputHiddenField
from ...fields.navigation import Navigation
from ...fields.outputs.table import OutputTableField
from ...page import Page, ContentError


class DeassignJob(Page):
    def __init__(self, distributor):
        super(DeassignJob, self).__init__()

        self.fields = Navigation(VStack([
            OutputTableField("JobStats"),
            OutputTableField("JobTasksStats"),
            InputHiddenField("user_id", None),
        ]))
        self.fields.add_link("Login", "/login")
        self.fields.add_link("Stats", "/stats")

        self.distributor = distributor

    def get_content(self, **kwargs):
        user_id = kwargs.get('user_id')
        if user_id is None:
            raise ContentError({
                "Error": "Login to setup user_id"
            }, redirect_url="/login")

        job = self.distributor.get_job(user_id)

        stats, tasks_stats = self.distributor.job_stats(job)
        self.distributor.deassign_job(job)
        fields = copy.deepcopy(self.fields)
        fields.link["Stats"]["href"] = self.redirect_url("/stats", user_id=user_id)
        return self.fill(fields, {
            "JobStats": pd.DataFrame(
                stats
            ),
            "JobTasksStats": pd.DataFrame(
                tasks_stats
            ),
            "user_id": user_id,
        })

    def process(self, **data):
        data = self.parse(self.fields, data)
        user_id = data.get('user_id')
        if user_id is None:
            return self.redirect_url('/login')

        return self.redirect_url("/job", user_id=user_id, obj_id=0)
