import os


class LabellingDataset(object):
    def __init__(self):
        super(LabellingDataset, self).__init__()

    def __getitem__(self, index):
        raise NotImplementedError()

    def __len__(self):
        raise NotImplementedError()

    def save(self, idx, data, meta=None):
        raise NotImplementedError()

    def load(self, idx, meta=None):
        raise NotImplementedError()
