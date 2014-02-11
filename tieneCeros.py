def tieneCeros(n):
	if n==0:
		return True
	else:
		return aux(abs(n))

tieneCerosAlternativa = lambda n:n==0 and aux_alt(abs(n))
aux_alt = not n==0 and n%10==0 or aux_alt(n//10)


def aux(n):
	if n==0:
		return False
	elif n%10==0:
		return True
	else:
		return aux(n//10)



