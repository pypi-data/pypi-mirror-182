import os
from .image import OutputImageField


class OutputImageWithObjectDetectionField(OutputImageField):
    def __init__(self, name):
        super(OutputImageWithObjectDetectionField, self).__init__(name)

    def set_output(self, data):
        pass
