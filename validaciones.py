def ValidarEntero(mensaje):
    try:
        return int(input(mensaje))
    except:
        return None


def ValidarEntero2(mensaje, V_minimo):
    try:
        dato = int(input(mensaje))
        if dato <= V_minimo:
            return None
        else:
            return dato
    except:
        return None


def ValidarOpcion(mensaje, V_minimo, V_maximo):
    try:
        dato = int(input(mensaje))
        if dato < V_minimo or dato > V_maximo:
            return None
        else:
            return dato
    except:
        return None


def NombreValido(nombre):
    if nombre.strip() == "":
        return False
    return True


def ValidarClave(ClaveIngresada):
    try:
        clave = 2105
        if clave != ClaveIngresada:
            return None
        else:
            return True
    except:
        return None