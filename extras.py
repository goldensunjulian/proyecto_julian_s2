from validaciones import ValidarOpcion
import time


def CategoriaHerramienta():
    try:
        while True:
            op = ValidarOpcion("""
        ¿A que categoria pertenece la herramienta?
        1. Construcción
        2. Jardinería
        3. Vehículos
        4. Electrodomésticos                                  
                         """, 1, 4)
            match op:
                case 1:
                    categoria = "Construccion"
                case 2:
                    categoria = "Jardineria"
                case 3:
                    categoria = "Vehiculos"
                case 4:
                    categoria = "Electrodomesticos"
            return categoria
    except:
        print("Opcion invalida, intente nuevamente.")
        return False


def EstadoHerramienta():
    try:
        while True:
            op = ValidarOpcion("""
        ¿Cual es el estado de la herramienta?
        1. Libre
        2. Ocupada
        3. En reparación
        4. Cancelar y salir                 
                         """, 1, 3)
            match op:
                case 1:
                    estado = "Libre"
                case 2:
                    estado = "Ocupada"
                case 3:
                    estado = "En reparacion"
            return estado
    except:
        print("Opcion invalida, intente nuevamente.")
        return False
