# Aplicación para gestionar personas y herramientas :hammer:
A continuación se explicara el uso de la aplicación para gestionar herramientas y personas, y que estas personas puedan retirar las herramientas disponibles.
## **¿Como funciona?**
El administrador puede gestionar herramientas y usuarios (Crear, Leer, Editar y Eliminar) también puede ver un registro de logs cuando un usuario intente sacar más herramientas de las que hay en espera o intenta regresar una herramienta que no saco él. 
El manejo de herramientas son con IDs que se les otorga de forma automática. 
Los usuarios se manejan por medio de IDs que son la tarjeta de identidad de la persona.
## ***Como usarla como administrador :lock:***
1. Entrar en la cuenta administrador (:closed_lock_with_key::2105)
1.1. Gestionar Usuario:
--- 1.1.1.	En esta opcion se puede agregar un usuario (El id sera el equivalente al documento de identidad).
--- 1.1.2.	En esta opcion puedes ver todas las personas registradas.
--- 1.1.3.	Aca puedes eliminar a cualquier persona registrada.
--- 1.1.4.	Con esta puedes editar algunas credenciales del usuario deseado (correo y numero telefónico).
1.2 Gestionar Herramientas:
--- 1.1.1.	Sirve para agregar una nueva herramienta(o añadir en caso de que exista ya).
--- 1.1.2.	Con esta mirar el registro actual de herramientas.
--- 1.1.3.	Con este eliminas una herramienta existente.
--- 1.1.4.	Con este editas el estado de una herramienta (pronto a eliminar).
--- 1.1.5.	Hace lo mismo de la anterior pero solo para herramientas dañadas.
--- 1.1.6.	Con esto puedes ver quien y cuando tomaron y devolvieron una herramienta. 
1.3 Logs: Sirve para ver intentos fallidos de tomar o devolver herramienta.

## ***Como usarla como Usuario :busts_in_silhouette:***
1. Entra como usuario (El administrador debe registrarte primero. :closed_lock_with_key:=tarjeta de indentidad).
1.1.	Tomar herramienta: Sirve para tomar una herramienta existente y genera el id prestamo.
1.2 devolver herramienta:	Sirve para devolver una herramienta tomada siempre y cuando la tomara el mismo usuario.
