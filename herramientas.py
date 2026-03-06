from Json import guardar, GenerarID, cargar
from validaciones import ValidarEntero, ValidarEntero2, ValidarOpcion, NombreValido
from extras import CategoriaHerramienta, EstadoHerramienta
from datetime import date
import time
from personas import ARCHIVO_PERSONAS

ARCHIVO_HERRAMIENTAS = "Herramientas.json"
ARCHIVO_PRETAMOS="Prestamos.json"
LOGS="Logs.json"
def existenombre(nombre):
    herramienta=cargar(ARCHIVO_HERRAMIENTAS)
    for elemento in herramienta:
        if nombre.lower()==elemento["Nombre"].lower():
            return True
        return False

def agregarHerramientaActual(nombre):
    herramientas = cargar(ARCHIVO_HERRAMIENTAS) 
    for elemento in herramientas:
        if nombre.lower() == elemento["Nombre"].lower():
            msj = f'Este producto ya existe ({elemento["Nombre"]}), actualmente hay {elemento["Cantidad"]}. ¿Cuántos desea sumar?: '
            cantidad_nueva = ValidarEntero2(msj, 0)
            
            if cantidad_nueva:
                elemento["Cantidad"] += cantidad_nueva
                guardar(ARCHIVO_HERRAMIENTAS, herramientas) 
                print("¡Actualización exitosa!")
                return True 
    return False

def AgregarHerramienta():
    herramientas=cargar(ARCHIVO_HERRAMIENTAS)
    nombre=input("Ingrese el nombre de la herramienta: ")
    while NombreValido(nombre)== False:
        print("Nombre no valido.")
        nombre=input("Ingrese el nombre de la herramienta: ")
    if existenombre(nombre)==True:
            agregarHerramientaActual(nombre)
    else:
        CantidadHerramienta=ValidarEntero2("Ingrese la cantidad de la herramienta: ", 0)
        while CantidadHerramienta==None:
            print("La cantidad no es válida, ingrese una cantidad válida")
            CantidadHerramienta=ValidarEntero2("Ingrese la cantidad de la herramienta: ", 0)
        categoria=CategoriaHerramienta()
        while categoria==False:
            print("opcion no valida, intente nuevamente.")
            categoria=CategoriaHerramienta()
        estado=EstadoHerramienta()
        while estado==False:
                print("")
                estado=EstadoHerramienta()
        herramienta={
                "ID": GenerarID(herramientas),
                "Nombre": nombre,
                "Cantidad": CantidadHerramienta,
                "Categoria": categoria,
                "Estado": estado
            }
        herramientas.append(herramienta)
        guardar(ARCHIVO_HERRAMIENTAS, herramientas)

def MostrarHerramientas():
    herramientas=cargar(ARCHIVO_HERRAMIENTAS)
    if not herramientas:
        print("No hay ninguna herramienta registrada.")
        return
    for elemento in herramientas:
        print(f"ID: {elemento['ID']}")
        print(f"Nombre: {elemento['Nombre']}")
        print(f"Cantidad: {elemento['Cantidad']}")
        print(f"Categoria: {elemento['Categoria']}")
        print(f"Estado: {elemento['Estado']}")
        print("-"*20)        

def MostrarPrestamo():
    prestamos = cargar(ARCHIVO_PRETAMOS) 
    
    if not prestamos:
        print("No hay préstamos registrados.")
        return

    for p in prestamos:
        print("-" * 20)
        
        if not isinstance(p, dict):
            print(f"Error de formato en el registro: {p}")
            continue
        
        print(f"ID Préstamo: {p.get('ID', 'Desconocido')}")
        print(f"ID Usuario: {p.get('ID_usuario', 'Desconocido')}")
        print(f"Herramienta: {p.get('Nombre', 'Desconocida')}")
        print(f"Prestado el: {p.get('Fecha_Prestamo', p.get('Fecha', 'Sin fecha'))}")
        print(f"Devuelto el: {p.get('Fecha_Devolucion', 'Pendiente')}")
        print(f"Estado: {p.get('Estado', 'Desconocido')}")


def actualizar_herramienta():
    herramientas=cargar(ARCHIVO_HERRAMIENTAS)
    id_profesion=ValidarEntero("Escoja el ID de la herramienta a actualizar ")
    while id_profesion is None:
        print("ID invalido. Intente nuevamente.")
        id_profesion=ValidarEntero("Escoja el ID de la herramienta a actualizar " )
    for elemento in herramientas:
        if id_profesion==elemento["ID"]:    
            estado=EstadoHerramienta()
            elemento["Estado"]=estado
            guardar(ARCHIVO_HERRAMIENTAS, herramientas)
            return
    print("No se encontro la herramienta con el ID proporcionado.")

def EliminarHerramienta():
    Contador=0
    herramientas=cargar(ARCHIVO_HERRAMIENTAS)
    id_profesion=ValidarEntero("Ingrese el ID de la herramienta a eliminar")
    while id_profesion is None:
        print ("ID invalido. Intente nuevamente")
        id_profesion=ValidarEntero("Ingrese el ID de la herramienta a eliminar")
    for elemento in herramientas:
        if id_profesion==elemento["ID"]:
            herramientas.pop(Contador)
            guardar(ARCHIVO_HERRAMIENTAS, herramientas)
            return
        Contador+=1
    print ("La profesion no existe")

def TomarHerramienta(id_usuario_actual):
    herramientas = cargar(ARCHIVO_HERRAMIENTAS)
    log=cargar(LOGS)
    NombrePersona=cargar(ARCHIVO_PERSONAS)

    id_h = ValidarEntero("ID de la herramienta: ")
    
    for h in herramientas:
        if h["ID"] == id_h and h["Estado"] == "Libre":
            nuevo_p = GenerarPrestamo(id_usuario_actual, id_h, h["Nombre"])

            lista_p = cargar(ARCHIVO_PRETAMOS)
            lista_p.append(nuevo_p)
            guardar(ARCHIVO_PRETAMOS, lista_p)

            h["Cantidad"] -= 1
            if h["Cantidad"] == 0: h["Estado"] = "Ocupada"
            guardar(ARCHIVO_HERRAMIENTAS, herramientas)
            
            print("Hecho.")
            return
    else:    
        print("No disponible o no existe.")
        CreacionLog = {
            "ID": GenerarID(log),
            "Accion": "Tomar herramienta",
            "Fecha y hora": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
            "Error": "No podia tomar la herraminta"
        }
        log.append(CreacionLog)
        guardar(LOGS, log)





def GenerarPrestamo(id_user, id_herramienta, nombre_h):

    prestamos = cargar(ARCHIVO_PRETAMOS) 
    
    prestamo = {
        "ID": GenerarID(prestamos), 
        "ID_usuario": id_user,
        "ID_herramienta": id_herramienta,
        "Nombre": nombre_h,
        "Fecha": str(date.today()),
        "Estado": "Activo"
    }
    return prestamo

def DevolverHerramienta(id_usuario):
    prestamos = cargar(ARCHIVO_PRETAMOS)
    herramientas = cargar(ARCHIVO_HERRAMIENTAS)
    NombrePersona=cargar(ARCHIVO_PERSONAS)
    log=cargar(LOGS)
    id_h = ValidarEntero("Ingrese el ID de la herramienta a devolver: ")
    prestamo_encontrado = False

    for p in prestamos:
        if p.get("ID_usuario") == id_usuario and p.get("ID_herramienta") == id_h and p.get("Estado") == "Activo":
            p["Estado"] = "Finalizado"
            p["Fecha_Devolucion"] = str(date.today())
            prestamo_encontrado = True
            break
            
    if prestamo_encontrado:
        for elemento in herramientas:
            if id_h == elemento["ID"]:
                elemento["Cantidad"] += 1
                if elemento["Cantidad"] > 0:
                    elemento["Estado"] = "Libre"
                break
        
        guardar(ARCHIVO_HERRAMIENTAS, herramientas)
        guardar(ARCHIVO_PRETAMOS, prestamos)
        print("Herramienta devuelta con éxito.")
    else:
        print("No tienes un préstamo activo de esta herramienta.")
        for elemento in NombrePersona:
            id_usuario==elemento["ID"]
    CreacionLog = {
        "ID": GenerarID(log),
        "Accion": "Devolver herramienta", 
        "Fecha y hora": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
        "Error": "No podia devolver la herraminta"
    }
    log.append(CreacionLog)
    guardar(LOGS, log)

    
def HerramientaReparada():
    herramientas=cargar(ARCHIVO_HERRAMIENTAS)
    id_profesion=ValidarEntero("Ingrese el ID de la herramienta reparada: ")
    while id_profesion is None:
        print ("ID invalido. Intente nuevamente")
        id_profesion=ValidarEntero("Ingrese el ID de la herramienta a reparada: ")
    for elemento in herramientas:
        if id_profesion==elemento["ID"]:
            if elemento["Estado"]=="En reparacion" :
                elemento["Estado"]="Libre"
                guardar(ARCHIVO_HERRAMIENTAS, herramientas)
                return
            else:
                print("La herramienta no esta en reparacion en este momento.")
                return
    print ("La herramienta no existe")
    

def MostrarLog():
    log=cargar(LOGS)
    if not log:
        print("No hay logs registrados.")
        return
    for elemento in log:
        print(f"ID: {elemento['ID']}")
        print(f"Accion: {elemento['Accion']}")
        print(f"Fecha y hora: {elemento['Fecha y hora']}")
        print(f"Error: {elemento['Error']}")
        print("-"*20)