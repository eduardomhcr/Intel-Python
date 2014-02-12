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



