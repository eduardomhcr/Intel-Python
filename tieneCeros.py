def tieneCeros(n):
	if n==0:
		return True
	else:
		return aux(abs(n))

tieneCerosAlternativa = lambda n:n==0 and aux(abs(n))

def aux(n):
	if n==0:
		return False
	elif n%10==0:
		return True
	else:
		return aux(n//10)



