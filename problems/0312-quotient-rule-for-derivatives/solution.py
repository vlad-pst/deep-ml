import numpy as np

def quotient_rule_derivative(g_coeffs: list, h_coeffs: list, x: float) -> float:
    """
    Compute the derivative of f(x) = g(x)/h(x) at point x using the quotient rule.
    
    Args:
        g_coeffs: Coefficients of numerator polynomial in descending order
        h_coeffs: Coefficients of denominator polynomial in descending order
        x: Point at which to evaluate the derivative
        
    Returns:
        The derivative value f'(x)
    """
    # g_coeffs[]
    # h_coeffs[]
    # x
    g = 0
    dg = 0
    n = len(g_coeffs)
    for i in range(1, n):
        g += (g_coeffs[i-1] * (x ** (n - i)))
        dg += (g_coeffs[i-1] * (n - i) * (x ** (n - i - 1)))
    g += g_coeffs[n-1]
    
    h = 0
    dh = 0
    m = len(h_coeffs)
    for i in range(1, m):
        h += (h_coeffs[i-1] * (x ** (m - i)))
        dh += (h_coeffs[i-1] * (m - i) * (x ** (m - i - 1)))
    h += h_coeffs[m-1]

    df = (dg * h - g * dh) / (h ** 2)

    return df
