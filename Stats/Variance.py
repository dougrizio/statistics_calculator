from Calc.Subtraction import subtraction
from Calc.Squaring import squaring
from Stats.Mean import mean

def variance(data):
    varMean = mean(data)

    listDiffs = []
    for eachNum in data:
        eachDiff = subtraction(eachNum, varMean)
        listDiffs.append(eachDiff)

    listSquares = []
    for eachDiff in listDiffs:
        eachSquare = squaring(eachDiff)
        listSquares.append(eachSquare)

    totalVariance = mean(listSquares)
    return totalVariance