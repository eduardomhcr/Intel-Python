import glob
import os

def crearDiccionario(ext="txt"):
    listaDeArchivos = glob.glob("*.{0}".format(ext))
    diccionario = {}
    for archivo in listaDeArchivos:
        f = open(archivo,"r")
        diccionario[archivo] = f.read()
        f.close()
    return diccionario
    
def obtenerExt(fileName):
    return "None" if fileName.find(".") == -1 else fileName[fileName.find(".")+1:]
    
def crearDiccionarioDeExtensiones():
    diccionario = {}
    for archivo in os.listdir(os.getcwd()):
        ext = obtenerExt(archivo)
        if ext in diccionario:
            diccionario[ext].append(archivo)
        else:
            diccionario[ext] = [archivo]
    return diccionario
    
