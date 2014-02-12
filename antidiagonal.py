def antidiagonal(matriz):
	r = []
	for e in range(len(matriz)):
		r.append(matriz[e][len(matriz)-1-e])
	return r


