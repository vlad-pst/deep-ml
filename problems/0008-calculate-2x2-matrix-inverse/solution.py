def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    inverse_matrix = []
    determinant_two_dim = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    if determinant_two_dim == 0:
        return None
    else:
        for i in range(len(matrix)):
            a = (-1) ** (i) * matrix[1][1-i] / determinant_two_dim
            b = (-1) ** (i+1) * matrix[0][1-i] / determinant_two_dim
            inverse_matrix.extend([[a, b]]) 
        return inverse_matrix