import Pyro4

nombre = input("¿Cuál es tu nombre? ")

ns = Pyro4.locateNS(host="localhost", port=9090)
uri = ns.lookup("practica.banco")

servidor = Pyro4.Proxy(uri)

print(servidor.get_fortune(nombre))

while True:
    try:
        dato = input(
            "CUENTANOS Que quieres hacer\n"
            "1._Retirar\n"
            "2._Depositar\n"
            "3._Consultar\n"
            "Escribe /salir para terminar\n"
        )

        if dato == "/salir":
            break

        if dato == "1":
            dato2 = float(input("Inserta el valor que quieres retirar: "))
            print(servidor.get_retirar(dato2))

        elif dato == "2":
            dato2 = float(input("Inserta el valor que quieres depositar: "))
            print(servidor.get_depositar(dato2))

        elif dato == "3":
            print(servidor.get_consultar())

        else:
            print("Opcion no valida")

    except ValueError:
        print("======================")
        print("Ingrese un numero valido")
        print("======================")