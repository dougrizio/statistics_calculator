from Calc.Addition import addition
from Calc.Subtraction import subtraction
from Calc.Multiplication import multiplication
from Calc.Division import division
from Calc.Squaring import squaring
from Calc.Squarerooting import squarerooting

from Stats.Mean import mean

#for testing
sample = [1, 5, 9, 5, 3, 1, 8, 8]


def confidence_interval(sample):
   # finding sample standard deviation

   old_sample_size = len(sample)
   new_sample_size = subtraction(1, old_sample_size)
   sample_mean = mean(sample)

   subtract_mean_result = []
   for item in sample:
      result = subtraction(sample_mean, item)
      subtract_mean_result.append(result)

   squared_list = []
   for num in subtract_mean_result:
      squared_result = squaring(num)
      squared_list.append(squared_result)

   squared_list_total = 0
   for num in squared_list:
      squared_list_total += num

   sample_variance = division(new_sample_size, squared_list_total)
   sample_deviation = squarerooting(sample_variance)

   # finding confidence interval

   confidence_level = .95
   t_distribution = 2.262
   # taken from t_distribution chart https://www.statisticshowto.com/probability-and-statistics/confidence-interval/#CISample

   confidence_minus_one = subtraction(confidence_level, 1)
   new_confidence = division(2, confidence_minus_one)

   squareroot_of_sample = squarerooting(old_sample_size)
   CI = division(squareroot_of_sample, sample_deviation)
   interval = multiplication(CI, t_distribution)

   lower_end = subtraction(interval, sample_mean)
   upper_end = addition(interval, sample_mean)
   width = subtraction(lower_end, upper_end)

   return [lower_end, upper_end, width]

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



