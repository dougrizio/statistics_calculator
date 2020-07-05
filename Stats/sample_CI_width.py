from Stats.ConfidenceInterval import confidence_interval
from Stats.RandomGenerators import list_generator

sample = list_generator()
ci = confidence_interval(sample)
confidence_val = ci[0]
width = ci[3]
confidence = .95

def get_sample_CI_width(confidence_lvl, widtha):
    c = confidence_lvl
    w = widtha

    za = confidence / 2
