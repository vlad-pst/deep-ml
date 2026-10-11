def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    """
    Transpose a 2D matrix by swapping rows and columns.
    
    Args:
        a: A 2D matrix of shape (m, n)
    
    Returns:
        The transposed matrix of shape (n, m)
    """
    # Complexity (highest, not efficient): m*n
    b = []

    for j in range(len(a[0])):
        b.append([])
        for i in range(len(a)):
            b[j].append(a[i][j])

    return b
    pass