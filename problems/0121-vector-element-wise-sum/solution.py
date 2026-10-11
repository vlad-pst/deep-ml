def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	
	if len(a) != len(b):
		return -1
	else:	
		for i in range(len(a)): 
			b[i] += a[i]	
		return b