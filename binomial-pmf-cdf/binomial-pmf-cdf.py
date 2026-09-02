import math

def binomial_pmf_cdf(n: int, p: float, k: int) -> dict:
    """
    Returns a dictionary with pmf and cdf.
    """
    # Write code here
    pmf = (math.factorial(n) * p**k * (1-p)**(n-k)) / (math.factorial(n - k) * math.factorial(k))

    cdf = 0
    for i in range(k+1):
        cdf += (math.factorial(n) * p**i * (1-p)**(n-i)) / (math.factorial(n - i) * math.factorial(i))
    return {'pmf' : pmf, 'cdf' : cdf}
    