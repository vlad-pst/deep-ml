def matrixmul(a:list[list[int|float]], 
    b:list[list[int|float]])-> list[list[int|float]]:
	
    if len(a[0]) == len(b):
        c = []
        for i in range(len(a)):
            c.append([])
            for j in range(len(b[0])):
                s = 0
                for l in range(len(b)):
                    s += a[i][l] * b[l][j]
                c[i].append(s)
        return c
    else:
        return -1