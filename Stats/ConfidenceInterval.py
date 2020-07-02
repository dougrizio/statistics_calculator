
from Calc.Calculator import Calculator
from Stats.Statistics import Statistics

population = [1, 5, 9, 5, 3, 1, 8, 8]


def confidence_interval(sample):
   calc = Calculator()
   stats = Statistics()
   confidence_level = .95
   sample_size = len(sample) - 1
   sample_mean = stats.get_mean(population)
   subtract_mean_result = []
   squared_list = []

   for item in sample:
       result = item - sample_mean
       subtract_mean_result.append(result)

   for num in subtract_mean_result:
       squared_result = Calculator.square(calc, num)
       squared_list.append(squared_result)

   print(sample_size)
   print(sample_mean)
   print(subtract_mean_result)
   print(squared_list)



confidence_interval(population)

