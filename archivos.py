import json
from utilidades import datos_art, paises, generos

datosart="general.json"
pai="paises2.json"
gen="generos.json"

def cargar_arch(archivo):
    datos={}
    try:
        with open(archivo,"r") as file:
            datos=json.load(file)
    except ValueError:
        print("")

    if archivo =="general.json":
        datos_art.update(datos)
    elif archivo=="generos.json":
        generos.update(datos)
    elif archivo=="paises2.json":
        paises.update(datos)

def guardar():
    with open(datosart,"w") as archivo:
        json.dump(datos_art,archivo,indent=4)
    with open(pai,"w") as archivo:
        json.dump(paises,archivo,indent=4)
    with open(gen,"w") as archivo:
        json.dump(generos,archivo,indent=4)
