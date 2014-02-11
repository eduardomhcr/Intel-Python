password = input("Ingrese el password:")

tieneMayuscula, tieneMinuscula, tieneNumero, tieneEspecial = False,False,False,False
for letra in password:
	tieneMayuscula, tieneMinuscula, tieneNumero, tieneEspecial = tieneMayuscula or letra.isupper(),tieneMinuscula or letra.islower(), tieneNumero or letra.isnumeric(), tieneEspecial or not letra.isalnum()

if tieneMayuscula and tieneMinuscula and tieneNumero and tieneEspecial:
	print("Fuerte")
elif tieneMayuscula and tieneNumero or tieneMinuscula and tieneNumero or tieneNumero and tieneEspecial or tieneMayuscula and tieneEspecial or tieneMinuscula and tieneEspecial:
	print("Medio")
else:
	print("débil")



