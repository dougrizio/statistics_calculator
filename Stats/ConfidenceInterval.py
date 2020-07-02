from Stats.Mean import mean
from Stats.Statistics import Statistics
from Calc.Calculator import Calculator

population = [1, 5, 9, 5, 3, 1, 8, 8]


def confidence_interval(sample):
   self = Calculator()
   confidence_level = .95
   sample_size = len(sample) - 1
   sample_mean = mean(sample)
   subtract_mean_result = []
   squared_list = []

   for item in sample:
       result = item - sample_mean
       subtract_mean_result.append(result)

   for num in subtract_mean_result:
       squared_result = Calculator.square(self, num)
       squared_list.append(squared_result)

   print(sample_size)
   print(sample_mean)
   print(subtract_mean_result)
   print(squared_list)



confidence_interval(population)

