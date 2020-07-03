from Calc.Addition import addition
from Calc.Division import division

data = [4,2,8,9,10]

def mean(data):
    num_values = len(data)
    total = 0
    for num in data:
        total = addition(total, num)
    return division(num_values, total)

result = mean(data)
print(data)
print( "mean: " + str(result))