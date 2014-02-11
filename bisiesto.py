def esBisiesto(year):
	if year%400==0:
		return True
	elif year%100==0:
		return False
	elif year%4==0:
		return True
	else:
		return False

esBisiestoDavid = lambda year:(year%4==0 and year%100!=0) or year%400==0


 
