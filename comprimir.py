import glob
import subprocess

# versión no abreviada
filename = "programas.zip"
listaComandos = ["zip",filename] + glob.glob("*.py")
subprocess.call(listaComandos)

# versión abreviada
subprocess.call(["zip","programas.zip"]+glob.glob("*.py"))

