import numpy as np

def descriptive_statistics(data: list | np.ndarray) -> dict:
    """
    Calculate various descriptive statistics metrics for a given dataset.
    
    Args:
        data: List or numpy array of numerical values
    
    Returns:
        Dictionary containing mean, median, mode, variance, standard deviation,
        percentiles (25th, 50th, 75th), and interquartile range (IQR)
    """
    # Mean
    n = len(data)
    mean = sum(data) / n

    # Mode
    values, counts = np.unique(data, return_counts=True)
    mode = int(values[np.argmax(counts)])

    # Median, Q1, and Q3
    q1 = float(np.percentile(data, 25))
    q2 = float(np.percentile(data, 50))
    q3 = float(np.percentile(data, 75))
    iqr = q3 - q1

    # percentages = [0.25, 0.50, 0.75]
    # quartiles = []
    # for p in percentages:
    #     rank = p * (n + 1)
    #     fractional, integral = np.modf(rank)
    #     integral = int(integral)
    #     quartile = float(data[integral - 1] + fractional * (data[integral] - data[integral - 1]))
    #     quartiles.append(quartile)

    # Variance and standard deviation
    variance = np.var(data).item()
    std = np.std(data).item()

    # my_dict = {
    #     "mean": mean, 
    #     "median": quartiles[1].item(),
    #     "mode": mode.item(),
    #     "variance": np.var(data).item(),
    #     "standard_deviation": np.std(data).item(),
    #     "25th_percentile": quartiles[0].item(),
    #     "50th_percentile": quartiles[1].item(),
    #     "75th_percentile": quartiles[2].item(),
    #     "interquartile_range": (quartiles[2] - quartiles[0]).item(),
    # }

    my_dict = {
        "mean": mean, 
        "median": q2,
        "mode": mode,
        "variance": variance,
        "standard_deviation": std,
        "25th_percentile": q1,
        "50th_percentile": q2,
        "75th_percentile": q3,
        "interquartile_range": (q3 - q1),
    }

    return my_dict