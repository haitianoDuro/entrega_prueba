def tareas():

    opcion = [
        "Registrar cliente",
        "Listar clientes registrados",
        "Registrar compra",
        "Listar compras de un cliente",
        "Salir del programa",
    ]
    for i, opcion in enumerate(opcion):
        print(f"{i+1}. {opcion}")

def registrar_cliente(bd):
    
    nombre = input("Ingrese primer nombre del cliente: ").upper()
    apellido = input("Ingrese primer apellido del cliente: ").upper()
    correo = input("correo electronico: ")

    id_cliente = len(bd) + 1

    bd.append(
        {
            "nombre": nombre,
            "apellido": apellido,
            "correo": correo,
            "ID": id_cliente,
            "compras": []
        }
    )

    print("\nSE HA AGREGADO UN CLIENTE NUEVO A LA BD!\n")    

def listar_clientes(bd):
    print("\nLos clientes registrados son:\n")
    print("ID\tNombre\t\t\t\tCorreo")
    for cliente in bd:
        print(f'{cliente["ID"]}\t{cliente["nombre"]} {cliente["apellido"]}\t\t{cliente["correo"]}')

    print("\nListado creado con éxito!\n")

def registrar_compra(bd):
    id = int(input("Ingrese el ID del cliente que compra: "))

    for cliente in bd:

        if cliente["ID"] == id:
            fecha = input("Ingrese fecha de compra (AAAA-MM-DD): ")
            monto = int(input("Ingrese monto de la compra: "))
            cliente["compras"].append(
                {
                    "fecha": fecha,
                    "monto": monto,
                    "puntos": round(monto*0.01)
                 
                }
            )
            print(f'\nSe ha agregado una compra a {cliente["nombre"]} {cliente["apellido"]}.')
             

def listar_puntos(bd):
    id = int(input("Ingrese el ID del cliente que compra: "))

    for cliente in bd:
        if cliente["ID"] == id:
            texto = f"ID CLIENTE: {id}\n"
            texto += f'NOMBRE CLIENTE: {cliente["nombre"]} {cliente["apellido"]}\n'
            texto += f"Fecha de Compra\t\tMonto Total\t\tPuntos\n"

            punto_totales = 0
            for monto in cliente["compras"]:
                texto += f'{monto["fecha"]}\t\t${monto["monto"]}\t\t\t\t{monto["puntos"]}\n'
                punto_totales += (monto["monto"])*0.01

            texto += f'PUNTO TOTALES A CANJEAR:  {round(punto_totales)} pesos'

            with open(f"RESUMEN_CLIENTE_ID_{id}.txt", "w", encoding='utf-8') as archivo:
	            archivo.write(texto)

            print("ARCHIVO CREADO")

            break


 
    