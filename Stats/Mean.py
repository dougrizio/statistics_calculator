from Calc.Addition import addition
from Calc.Division import division



def mean(data):
    num_values = len(data)
    total = 0
    for num in data:
        total = addition(total, num)
    return division(num_values, total)

