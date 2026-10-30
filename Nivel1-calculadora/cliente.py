import Pyro4
import os

nombre = input("¿Cuál es tu nombre? ")

ns = Pyro4.locateNS(host="localhost", port=9090)
uri = ns.lookup("practica.calculadora")
servidor = Pyro4.Proxy(uri)

print(servidor.get_fortune(nombre))


while True:
    dato = input("Te gustaria hacer una operacion matematica escoge \n"
          "1 - SUMA \n" \
          "2 - Resta\n" \
          "3 - Multiplicacion\n" \
          "4 - Division\n")

    try:
        datoIn=int(dato)
        print("dato",datoIn)

        if datoIn == 1:
            dato1=float(input("Ingrese un numero que quiera operar: "))
            dato2=float(input("Ingrese el segundo numero que quiere operar: "))
            print(servidor.get_suma(dato1,dato2))

        elif datoIn == 2:
            dato1=float(input("Ingrese un numero que quiera operar: "))
            dato2=float(input("Ingrese el segundo numero que quiere operar: "))
            print(servidor.get_resta(dato1,dato2))

        elif datoIn == 3:
            dato1=float(input("Ingrese un numero que quiera operar: "))
            dato2=float(input("Ingrese el segundo numero que quiere operar: "))
            print(servidor.get_multiplicar(dato1,dato2))

        elif datoIn == 4:
            dato1=float(input("Ingrese un numero que quiera shacer la operacion: "))
            dato2=float(input("Ingrese el segundo numero que quiere operar: "))
            print(servidor.get_division(dato1,dato2))

        else:
            print("envia un dato valido")

    except ValueError:
        print("======================")
        print("Ingrese datos enteros ")
        print("======================")


servidor = Pyro4.Proxy(uri)

print(servidor.get_fortune(nombre))
