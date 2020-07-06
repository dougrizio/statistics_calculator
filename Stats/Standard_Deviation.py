from Calc.Squarerooting import squarerooting
from Stats.Variance import variance

def standard_deviation(data):
    var = variance(data)
    stanDev = squarerooting(var)
    return stanDev