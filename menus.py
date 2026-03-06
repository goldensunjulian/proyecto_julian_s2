from validaciones import ValidarOpcion, ValidarClave
from herramientas import MostrarLog
from herramientas import MostrarPrestamo,AgregarHerramienta, MostrarHerramientas, actualizar_herramienta, EliminarHerramienta, TomarHerramienta, DevolverHerramienta, HerramientaReparada
from personas import AgregarPersona, mostrar_personas, EliminarPersona, actualizar_persona,LogearUsuairio
def MenuPrincipal():
    try:
        while (True):
            op=ValidarOpcion("""
        Ingrese el numero acorde a la accion deseada.
                             1. Entrar como usuario
                             2. Entrar como administrador
                             3. Salir
        """,1,4)
            if op==4:
                break
            match op:
                case 1:
                    id_usuario=LogearUsuairio()
                    if id_usuario:
                        MenuPersonas(id_usuario)
                    else:
                        print("Usuario no encontrado, intente nuevamente.")
                case 2:
                    ClaveIngresada=int(input("Ingrese la clave de administrador: "))
                    ValidarClave(ClaveIngresada)
                    while ValidarClave(ClaveIngresada)==None:
                        print("Clave incorrecta, intente nuevamente. Intentar nuevamente?")
                        intentar=ValidarOpcion("""1. Si
2. No"""
                                               ,1,2)
                        if intentar==2:
                            return
                        ClaveIngresada=int(input("Ingrese la clave de administrador: "))
                        ValidarClave(ClaveIngresada)
                    MenuAdmi()
                case _:
                    print("Opcion no valida, intente nuevamente.")
    except:
        return
def MenuAdmiHerramientas():
    try:
        while (True):
            op=ValidarOpcion("""
Que desea hacer hoy.
                             1. Agregar heramienta.
                             2. Mirar el registro actual de herramientas.
                             3. Eliminar herramientas.
                             4. Editar estado de herramienta.
                             5. Herramienta arreglada
                             6. Registro de prestamos
                             7. Salir

""",1,7)
            if op==7:
                break
            match op:
                case 1:
                    AgregarHerramienta()
                case 2:
                    MostrarHerramientas()
                case 3:
                    EliminarHerramienta()
                case 4:
                    actualizar_herramienta()
                case 5:
                    HerramientaReparada()
                case 6:
                    MostrarPrestamo()
                case 7:
                    break
                case _:
                    print("Opcion no valida, intente nuevamente.")
    except:
        print("")


def MenuAdmi():
    try:
        while (True):
            op=ValidarOpcion("""
Que desea administrar hoy.
                             1. Herramientas.
                             2. Personas.
                             3. Logs.
                             4. Salir

""",1,3)
            if op==4:
                break
            match op:
                case 1:
                    MenuAdmiHerramientas()
                case 2:
                    administrar_personas()
                case 3:
                    MostrarLog()
                case _:
                    print("Opcion no valida, intente nuevamente.")
    except:
        print("Opcion no valida")
def administrar_personas():
    try:
        while (True):
            op=ValidarOpcion("""Que desea hacer hoy.
                             1. Agregar persona.
                             2. Mirar el registro actual de personas.
                             3. Eliminar persona.
                             4. Editar persona.
                             5. Salir""",1,5)
            if op==5:
                break
            match op:
                case 1:
                    AgregarPersona()
                case 2:
                    mostrar_personas()
                case 3:
                    EliminarPersona()
                case 4:
                    actualizar_persona()
                case _:
                    print("Opcion no valida, intente nuevamente.")
    except:
        print("Opcion no valida")


def MenuPersonas(id_usuario):
    try:
        while (True):
            op=ValidarOpcion("""Que desea hacer hoy.
                             1. Tomar prestada una herramienta.
                             2. Devolver una herramienta.
                             3. Salir""",1,3)
            if op==3:
                break
            match op:
                case 1:
                    MostrarHerramientas()
                    TomarHerramienta(id_usuario)
                case 2: 
                    MostrarHerramientas()
                    DevolverHerramienta(id_usuario)
                case _:
                    print("Opcion no valida, intente nuevamente.")
    except:
        print("Opcion no valida")