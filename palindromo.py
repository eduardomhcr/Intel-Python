entrada = input("Escriba un número: ")
if entrada.isnumeric():
	x = int(entrada)
	if x//1000==x%10 and (x%1000)//100==(x%100)//10:
		print("Es palíndromo")
	else:
		print("No es palíndromo")
else:
	print("Inválido")
