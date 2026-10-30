import Pyro4

nombre = input("¿Cuál es tu nombre? ")

ns = Pyro4.locateNS(host="localhost", port=9090)
uri = ns.lookup("practica.mensajeria")

servidor = Pyro4.Proxy(uri)

print(servidor.get_fortune(nombre))

while True:
    dato = input("Escribe tu mensaje: ")

    if dato == "/salir":
        break

    print(servidor.get_chat(nombre, dato))

    print("Mensajes del chat:")
    for mensaje in servidor.ver_chat():
        print(mensaje)
