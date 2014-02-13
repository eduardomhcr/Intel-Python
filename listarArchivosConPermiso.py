import subprocess

tienePermisos = lambda linea:linea[3]=="x"

resultado = subprocess.check_output(["ls","-lc"]).decode()

for linea in resultado.splitlines():
	if tienePermisos(linea):
		print(linea.split(":")[1][3:])





	

