def scalar_multiply(matrix: list[list[int|float]], scalar: int|float) -> list[list[int|float]]:

	array = [[scalar * element for element in row] for row in matrix]
	return array
	