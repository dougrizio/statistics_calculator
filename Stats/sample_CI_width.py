from Stats.ConfidenceInterval import confidence_interval
from Stats.RandomGenerators import list_generator
from Calc.Calculator import squaring, multiplication


sample = list_generator(stop = 10000)
ci = confidence_interval(sample)
confidence_val = ci[0]
width = ci[2]
confidence = .95
base_percent = .5

def get_sample_CI_width(confidence_lvl, widtha):

    w = widtha

    za = confidence / 2
    me = w / 2
    percent = 1- base_percent


    new_za = squaring(za / me)

    multiplied = multiplication(percent, new_za)

    return multiplied


s = get_sample_CI_width(confidence,width)
print(s)
