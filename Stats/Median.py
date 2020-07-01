from Addition import addition
from Division import division

def median(data):
    numValues = len(data) - 1
    data.sort()
    median1 = float(division(2, data[numValues]))
    median2 = float(division(2, data[numValues - 1]))
    if numValues % 2 == 0:
        return division(2, (addition(median1, median2)))
    else:
        return division(2, median1)