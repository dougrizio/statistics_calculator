import scipy.stats as st
from math import ceil

N1 = 100000

cl1 = 0.95

e1 = 0.05

p1 = 0.5

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


result = sample(N1, cl1, e1, p1)

print(result)
