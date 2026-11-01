def matrix_determinant_and_trace(matrix: list[list[float]]) -> tuple[float, float]:
	"""
	Compute the determinant and trace of a square matrix.
	
	Args:
		matrix: A square matrix (n x n) represented as list of lists
	
	Returns:
		Tuple of (determinant, trace)
	"""
	n = len(matrix)
	trace_matrix = 0
	determinant_matrix = 0
	for i in range(n-1):
		trace_matrix += matrix[i][i]
		for j in range(i+1,n):
			determinant_two_dim = matrix[n-2][i] * matrix[n-1][j] - matrix[n-2][j] * matrix[n-1][i]
			# Temporary solution for matrixes of 2x2 and 3x3. Does not hold for n > 3. 
			if n == 3:
				determinant_matrix += ((-1) ** (n-i-j) * matrix[0][n-i-j] * determinant_two_dim)
			elif n == 2:
				determinant_matrix += determinant_two_dim

	trace_matrix += matrix[n-1][n-1]

	return (float(determinant_matrix), float(trace_matrix))
	