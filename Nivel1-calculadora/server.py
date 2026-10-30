import Pyro4

@Pyro4.expose
class GreetingMaker:

    def get_fortune(self, name):
        return "Hola, " + name + ". Bienvenido a Pyro4"

    def get_suma(self, dato1, dato2):
        return "La respuesta es: " + str(dato1 + dato2)

    def get_resta(self, dato1, dato2):
        return "La respuesta es: " + str(dato1 - dato2)

    def get_multiplicar(self, dato1, dato2):
        return "La respuesta es: " + str(dato1 * dato2)

    def get_division(self, dato1, dato2):
        if dato2 == 0:
            return "No se puede dividir por cero bro"
        else:
            return "La respuesta es: " + str(dato1 / dato2)


daemon = Pyro4.Daemon(host="localhost")

ns = Pyro4.locateNS(host="localhost", port=9090)

uri = daemon.register(GreetingMaker())

ns.register("practica.calculadora", uri)

print("Servidor iniciado")
print("URI:", uri)
print("Registrado como practica.calculadora")

daemon.requestLoop()
