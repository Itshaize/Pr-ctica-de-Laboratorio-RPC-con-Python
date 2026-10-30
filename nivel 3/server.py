import Pyro4

@Pyro4.expose
@Pyro4.behavior(instance_mode="single")
class GreetingMaker:

    def __init__(self):
        self.saldo = 0

    def get_fortune(self, name):
        return "Hola, " + name + ". Bienvenido al banco"

    def get_retirar(self, dinero):
        if dinero <= 0:
            return "Ingrese un valor mayor a cero"

        if self.saldo >= dinero:
            self.saldo -= dinero
            return "Retiro aprobado. Saldo actual: " + str(self.saldo)
        else:
            return "Saldo insuficiente"

    def get_depositar(self, dinero):
        if dinero <= 0:
            return "Ingrese un valor mayor a cero"

        self.saldo += dinero
        return "Deposito aprobado. Saldo actual: " + str(self.saldo)

    def get_consultar(self):
        return "Tu saldo actual es: " + str(self.saldo)


daemon = Pyro4.Daemon(host="localhost")

ns = Pyro4.locateNS(host="localhost", port=9090)

uri = daemon.register(GreetingMaker())

ns.register("practica.banco", uri)

print("Servidor iniciado")
print("URI:", uri)
print("Registrado como practica.banco")

daemon.requestLoop()