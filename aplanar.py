def aplanar(lista):
	resultado = []
	for elemento in lista:
		if isinstance(elemento,list):
			resultado.extend(aplanar(elemento))
		else:
			resultado.append(elemento)
	return resultado


