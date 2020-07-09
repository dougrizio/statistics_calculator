import scipy.stats as st
from math import ceil



#https://towardsdatascience.com/how-to-sample-data-with-code-327359dce10b
def sample(N, cl, e, p):
    # first we get the z-score
    z = st.norm.ppf(1 - (1 - cl) / 2)
    # then the n_0 value
    n_0 = z**2 * p * (1 - p) / e**2
    # and finally we calculate n
    n = n_0 / (1 + (n_0 - 1) / N)
    # we also need to round up to the nearest integer
    n = ceil(n)
    # finally we return our sample size
    return n


c_form = sample(10000, 0.95, .05, .05)

