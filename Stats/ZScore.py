from Calc.Subtraction import subtraction
from Calc.Division import division
from Stats.Mean import mean
from Stats.Standard_Deviation import standard_deviation

def zscore(data):
    dataMean = mean(data)
    stanDev = standard_deviation(data)

    listMinuses = []
    for eachRaw in data:
        meanMinusRaw = subtraction(dataMean, eachRaw)
        listMinuses.append(meanMinusRaw)

    listZScores = []
    for eachMinus in listMinuses:
        eachZ = division(stanDev, eachMinus)
        listZScores.append(eachZ)

    return listZScores


