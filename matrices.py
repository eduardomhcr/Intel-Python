def esMatriz(matriz):
	if isinstance(matriz,list) and len(matriz)>0 and isinstance(matriz[0],list):
		longitud = len(matriz[0])
		if longitud == 0:
			return False
		for fila in matriz:
			if not isinstance(fila,list) or longitud != len(fila):
				return False
			for ele in fila:
				if not isinstance(ele,int) or isinstance(ele,bool):
					return False
		return True
	else:
		return False


def sumarMatrices(m1,m2):
	if esMatriz(m1) and esMatriz(m2) and len(m1)==len(m2) and len(m1[0])==len(m2[0]):
		matrizResultado = []
		for numFila in range(len(m1)):
			filaResultado = []
			for numCol in range(len(m1[0])):
				res = m1[numFila][numCol] + m2[numFila][numCol]
				filaResultado  = filaResultado + [res]
			matrizResultado = matrizResultado + [filaResultado]
		return matrizResultado
	else:
		return False

def obtenerMaximos(matriz):
	resultado = []
	for fila in matriz:
		resultado.append(max(fila))
	return resultado





