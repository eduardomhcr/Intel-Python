import glob
import subprocess

filename = "programas.zip"
listaComandos = ["zip",filename] + glob.glob("*.py")
subprocess.call(listaComandos)



