import os

from piedemo.fields.outputs.base import OutputField


class OutputLineChartField(OutputField):
    def __init__(self, name):
        super(OutputLineChartField, self).__init__(name=name)
        self.data = {"x": [], "y": []}

    def set_output(self, data):
        self.data = data

    def clear(self):
        self.data = {"x": [], "y": []}

    def generate(self):
        return {
            "card": "OutputCanvasJSCard",
            "data": {
                "name": self.name,
                "options": {
                    "animationEnabled": True,
                    "exportEnabled": True,
                    "theme": "light1",
                    "title": {
                        "text": self.name
                    },
                    "data": [{
                        "type": "line",
                        "toolTipContent": "{x}, {y}",
                        "dataPoints": [
                            {"x": x, "y": y}
                            for x, y in zip(self.data["x"], self.data["y"])
                        ]
                    }]
                }
            }
        }
