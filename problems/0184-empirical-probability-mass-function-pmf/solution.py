def empirical_pmf(samples):
    """
    Given an iterable of integer samples, return a list of (value, probability)
    pairs sorted by value ascending.
    """
    # Probability = favorable outcomes / all possible outcomes
    n = len(samples)
    pmf = []
    for value in list(set(samples)): 
        pmf.append((value, samples.count(value) / n))

    return pmf