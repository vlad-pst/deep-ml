def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	
	means = []
	if mode == "row":
		
		means = [sum(row) / len(row) for row in matrix]
	elif mode == "column":
		for j in range(len(matrix[0])):
			s = 0 
			for i in range(len(matrix)):
				s += matrix[i][j]
			means.append(s / len(matrix))

	return means