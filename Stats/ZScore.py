from Calc.Subtraction import subtraction
from Calc.Division import division
from Stats.Mean import mean
from Stats.Standard_Deviation import standard_deviation

def zscore(data):
    dataMean = mean(data)
    stanDev = standard_deviation(data)

    for eachNum in data:
        meanMinusRaw = subtraction(dataMean, eachNum)
        scorez = division(stanDev, meanMinusRaw)
        return scorez