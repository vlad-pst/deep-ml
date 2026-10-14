def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	if len(a[0]) != len(b):
		return -1
	else:
		for row in a:
			i = 0
			while i < len(b): 
				row[i] *= b[i]
				i += 1
			a[0][a.index(row)] = sum(row)
			
		return a[0]
		
