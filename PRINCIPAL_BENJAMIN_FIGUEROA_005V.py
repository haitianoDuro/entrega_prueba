
from FUNCIONES_BENJAMIN_FIGUEROA_005V import *




BD = [
    {
        "nombre": "Benjamin",
        "apellido": "Figueroa",
        "correo": "rock.lee1@live.cl",
        "ID": 1,
        "compras":[{"fecha":"1999-05-24","monto":25000,"puntos":250}],
        
    }
]


while True:

    tareas()

    opcion = input("Ingrese la opccion que desea realizar: ")

    if opcion == "1":
        registrar_cliente(BD)

    elif opcion == "2":
        listar_clientes(BD)

    elif opcion == "3":
        registrar_compra(BD)

    elif opcion == "4":
        listar_puntos(BD)

    elif opcion == "5":
        print("Adios, gracias por comprar con nosotros.")
        break

    else:
        print("nooo papito esta puro leseando")