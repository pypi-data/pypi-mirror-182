from collections import namedtuple

import pandas as pd


TrainStepResult = namedtuple('EvaluationStepResult', ('epoch', 'loss', 'time', 'cumulative_time'))


class Traicer:
    def __init__(self, line_type: type = TrainStepResult):
        self.line_type = line_type
        self.entries = []

    def push(self, *args, **kwargs):
        self.entries.append(self.line_type(*args, **kwargs))

    @property
    def df(self):
        return pd.DataFrame(self.entries, columns = self.line_type._fields)
