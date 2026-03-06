import os
import json


def cargar(NombreArchivo):
    if not os.path.exists(NombreArchivo):
        return []
    try:
        with open(NombreArchivo, "r") as archivo:
            return json.load(archivo)
    except json.JSONDecodeError:
        return []


def guardar(NombreArchivo, Datos):
    with open(NombreArchivo, "w") as archivo:
        json.dump(Datos, archivo, indent=4)


def GenerarID(datos):
    if not datos:
        return 1
    return datos[-1]["ID"] + 1