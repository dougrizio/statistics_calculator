from Calc.Calculator import Calculator
from Stats.Mean import mean
from Stats.Median import median
from Stats.Mode import mode
from Stats.simple_sample import get_sample
from Stats.ConfidenceInterval import confidence_interval
from Stats.margin_of_error import margin_of_error

class Statistics(Calculator):

    data = []

    def __init__(self):
        super().__init__()

    def get_mean(self, data):
        self.result = mean(data)
        return self.result

    def get_median(self, data):
        self.result = median(data)
        return self.result

    def get_mode(self, data):
        self.result = mode(data)
        return self.result

    def get_simple_sample(self, data):
        sample_size = 6
        self.result = get_sample(data, sample_size)
        return self.result

    def get_confidence_interval (self, data):

        self.result = confidence_interval(data)
        return self.result

    def get_margin_of_error(self, crit_val, standard_error):
        self.result = margin_of_error(crit_val, standard_error)
        return self.result


crit_val = 1.645
standard_error = .013



