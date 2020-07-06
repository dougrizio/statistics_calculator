from Calc.Subtraction import subtraction
from Calc.Division import division
from Stats.Mean import mean
from Stats.Standard_Deviation import standard_deviation

def zscore(data):
    rawScore = 100
    dataMean = mean(data)
    stanDev = standard_deviation(data)
    meanMinusRaw = subtraction(dataMean, rawScore)
    return division(stanDev, meanMinusRaw)