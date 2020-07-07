
from Calc.Calculator import Calculator
from Stats.Mean import mean

#for testing
#sample = [1, 5, 9, 5, 3, 1, 8, 8]


def confidence_interval(sample):
   calc = Calculator()
   result = []


   sample_size = len(sample) - 1
   sample_mean = mean(sample)
   subtract_mean_result = []
   squared_list = []
   total = 0
   #taken from t_distribution chart https://www.statisticshowto.com/probability-and-statistics/confidence-interval/#CISample
   t_distribution = 2.262

   confidence_level = .95

   for item in sample:
       result = item - sample_mean
       subtract_mean_result.append(result)

   for num in subtract_mean_result:
       squared_result = Calculator.square(calc, num)
       squared_list.append(squared_result)

   for num in squared_list:
       total += num

   total2 = total / sample_size

   sample_deviation = Calculator.squareroot(calc, total2)

   conf = (1 - confidence_level) / 2

   ci = sample_deviation / Calculator.squareroot(calc,sample_size + 1)

   interval = calc.multiply(ci, t_distribution)

   lower_end = calc.subtract(interval, sample_mean)
   upper_end = calc.add(interval,sample_mean)
   width = calc.subtract(lower_end, upper_end)

   result = [lower_end, upper_end, width]


   return result

'''
 print("sample size: " + str(sample_size))
 print("sample mean: " + str(sample_mean))
 print("subtracted mean result: " + str(subtract_mean_result))
 print("sqaured list: " + str(squared_list))
 print("current total: " + str(total))
 print("total 2: " + str(total2))
 print("sample deviation:" + str(sample_deviation))
 print("confidence level: " + str(conf))
   print("z_score: " + str(interval))
   print("----------------Confidence interval----------------------")
   print("interval lower end: " + str(lower_end))
   print("interval upper end: " + str(upper_end))
   print("width: " + str(round(width, 2)))
'''



