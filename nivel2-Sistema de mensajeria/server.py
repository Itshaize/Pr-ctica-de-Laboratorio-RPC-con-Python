import Pyro4

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class GreetingMaker:

    def __init__(self):
        self.mensajes = []

    def get_fortune(self, name):
        return "Hola, " + name + ". Bienvenido al chat"

    def get_chat(self, nombre, mensaje):
        self.mensajes.append(nombre + ": " + mensaje)
        return "Mensaje enviado"

    def ver_chat(self):
        return self.mensajes


daemon = Pyro4.Daemon(host="localhost")

ns = Pyro4.locateNS(host="localhost", port=9090)

uri = daemon.register(GreetingMaker())

ns.register("practica.mensajeria", uri)

print("Servidor iniciado")
print("URI:", uri)

daemon.requestLoop()
