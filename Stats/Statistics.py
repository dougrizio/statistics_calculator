from Calc.Calculator import Calculator
from Stats.Mean import mean
from Stats.simple_sample import get_sample

class Statistics(Calculator):

    data = []

    def __init__(self):
        super().__init__()

    def get_mean(self, data):
        self.result = mean(data)
        return self.result

    def get_simple_sample(self, data):
        self.result = get_sample(data, sample_size = 3)
        return self.result