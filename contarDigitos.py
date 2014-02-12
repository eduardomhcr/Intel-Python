def digitos(num):
	if isinstance(num, int): 
		if num != 0:  
			return digitos_aux(abs(num))
		else: 
			return 1
	else:
     return "Error: entrada inválida"

def digitos_aux(num):
	if num == 0: 
		return 0  
	else:
		return 1 + digitos_aux(num // 10) 