from Addition import addition
from Subtraction import subtraction
from Division import division

def median(data):
    sortedDataset = sorted(data)
    numValues = len(sortedDataset)
    if numValues % 2 == 0:
        median1 = sortedDataset[division(2, numValues)]
        median2 = sortedDataset[subtraction(1, division(2, numValues))]
        return division(2, (addition(median1, median2)))
    else:
        return sortedDataset[division(2, numValues)]