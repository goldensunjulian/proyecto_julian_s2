from Json import guardar, GenerarID, cargar
from validaciones import ValidarEntero, ValidarEntero2, ValidarOpcion, NombreValido
from extras import CategoriaHerramienta, EstadoHerramienta
#guardar/mostrar-leer/eliminar/editar

ARCHIVO_PERSONAS = "Personas.json"
def existenombre(nombre):
    profesiones=cargar(ARCHIVO_PERSONAS)
    for elemento in profesiones:
        if nombre==elemento["Nombres"]:
            return True
    return False

def AgregarPersona():
    personas=cargar(ARCHIVO_PERSONAS)
    nombre=input("Ingrese el nombre de la persona: ")
    while NombreValido(nombre)== False or existenombre(nombre)==True:
        if existenombre(nombre)==True:
            print ("La prersona ya esta regristrada, ingrese otra persona")
        print("El nombre no es válido, ingrese un nombre válido")
        nombre=input("Ingrese el nombre de la persona: ")
    apellido1=input("Ingrese el apellido de la persona: ")
    while NombreValido(apellido1)== False:
        print("El nombre no es válido, ingrese un nombre válido")
        apellido1=input("Ingrese el apellido de la persona: ")
    id=ValidarEntero("Ingrese el numero de identificacion porfavor")
    while id==None:
        print("El numero de identificacion no es valido, ingrese un numero de identificacion valido")
        id=ValidarEntero("Ingrese el numero de identificacion porfavor")
    telefono=ValidarEntero("Ingrese el numero de telefono porfavor")
    while telefono==None:
        print("El numero de telefono no es valido, ingrese un numero de telefono valido")
        telefono=ValidarEntero("Ingrese el numero de telefono porfavor")
    Gmail=input("Ingrese la direccion de correo electronico ")
    Gmail.count("@")
    while Gmail.count("@")!=1:
        print("El correo electronico no es valido, ingrese un correo electronico valido")
        Gmail=input("Ingrese la direccion de correo electronico ")
    persona={
        "ID": id,
        "Nombres": nombre.capitalize(),
        "Apellidos": apellido1.capitalize(),
        "Telefono": telefono,
        "Gmail": Gmail.capitalize()
    }
    personas.append(persona)
    guardar(ARCHIVO_PERSONAS,personas)

def mostrar_personas():
    personas=cargar(ARCHIVO_PERSONAS)
    if not personas:
        print("No hay ninguna persona registrada.")
        return
    for elemento in personas:
        print(f"ID: {elemento['ID']}")
        print(f"Nombres: {elemento['Nombres']}")
        print(f"Apellidos: {elemento['Apellidos']}")
        print(f"Telefono: {elemento['Telefono']}")
        print(f"Gmail: {elemento['Gmail']}")
        print("-"*20)

def EliminarPersona():
    personas=cargar(ARCHIVO_PERSONAS)
    mostrar_personas()
    id_profesion=ValidarEntero("Escoja el ID de la persona a eliminar ")
    while id_profesion is None:
        print("ID invalido. Intente nuevamente.")
        id_profesion=ValidarEntero("Escoja el ID de la persona a eliminar ")
    for elemento in personas:
        if elemento["ID"]==id_profesion:
            personas.remove(elemento)
            guardar(ARCHIVO_PERSONAS, personas)
            print("Persona eliminada exitosamente.")
            return
    print("No se encontró ninguna persona con ese ID.")

def actualizar_persona():
    personas=cargar(ARCHIVO_PERSONAS)
    mostrar_personas()
    id_persona=ValidarEntero("Escoja el ID de la persona a actualizar ")
    while id_persona is None:
        print("ID invalido. Intente nuevamente.")
        id_persona=ValidarEntero("Escoja el ID de la persona a actualizar ")
    for elemento in personas:
        if id_persona==elemento["ID"]:
            telefono=ValidarEntero("Ingrese el nuevo numero de telefono porfavor")
            while telefono==None:
                print("El numero de telefono no es valido, ingrese un numero de telefono valido")
                telefono=ValidarEntero("Ingrese el nuevo numero de telefono porfavor")
            Gmail=input("Ingrese el nuevo correo electronico")
            elemento["Telefono"]=telefono
            elemento["Gmail"]=Gmail.capitalize()
            guardar(ARCHIVO_PERSONAS, personas)
            print("Persona actualizada exitosamente.")
            return
    print("No se encontró ninguna persona con ese ID.")

def LogearUsuairio():
    usuario=cargar(ARCHIVO_PERSONAS)
    try:
        id_usuario=ValidarEntero("Ingrese su numero de identificacion porfavor")
        while id_usuario==None:
            print("El numero de identificacion no es valido, ingrese un numero de identificacion valido")
            id_usuario=ValidarEntero("Ingrese su numero de identificacion porfavor")
        for elemento in usuario:
            if id_usuario==elemento["ID"]:
                print(f"Bienvenido {elemento['Nombres']} {elemento['Apellidos']}")
                return id_usuario
        print("No se encontró ninguna persona con ese ID.")
    except:
        return 