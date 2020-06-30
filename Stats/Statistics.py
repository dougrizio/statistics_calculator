from Calc.Calculator import Calculator
from Stats.Mean import mean

class Statistics(Calculator):

    data = []

    def __init__(self):
        super().__init__()

    def get_mean(self, data):
        self.result = mean(data)
        return self.result