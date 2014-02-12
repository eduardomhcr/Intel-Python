import glob

def crearDiccionario(ext="txt"):
    listaDeArchivos = glob.glob("*.{0}".format(ext))
    diccionario = {}
    for archivo in listaDeArchivos:
        f = open(archivo,"r")
        diccionario[archivo] = f.read()
        f.close()
    return diccionario
    
    