num = input("Escriba un número: ")
if num.isnumeric():
	num = int(num)
	primerDigito = num//100
	segundoDigito = (num%100)//10
	tercerDigito = num%10

	letras = {0:"cero",1:"uno",2:"dos",3:"tres",4:"cuatro",5:"cinco",6:"seis",7:"siete",8:"ocho",9:"nueve"}
	print("{0} {1} {2}".format(letras[primerDigito],letras[segundoDigito],letras[tercerDigito]))	
else:
	print("número inválido")
