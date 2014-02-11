def esbinario(num):
	if num == 0: 
		return True 
	elif num % 10 != 0 and num % 10 != 1:
		return False 
	else:
		return esbinario(num // 10)

def bin_dec(num):
	if isinstance(num, int) and esbinario(num):
		return bin_dec_aux(num, 0, 0) 
	else:
		return "Error: numero debe ser entero binario"

def bin_dec_aux(num, factor, result):
	if num == 0: 
		return result 
	else:
		return bin_dec_aux(num // 10, factor + 1, result + num % 10 * 2 ** factor)
