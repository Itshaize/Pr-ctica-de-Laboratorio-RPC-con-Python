"""Nivel 4: servidor de procesamiento remoto y asíncrono con Pyro4."""

import time

import Pyro4


@Pyro4.expose
class ProcesadorDatos:
    """Procesa una lista de números solicitada por un cliente remoto."""

    def procesar_numeros(self, numeros):
        """Calcula estadísticas y simula una tarea que requiere tiempo."""
        if not numeros:
            raise ValueError("Debes enviar al menos un número.")

        print("Servidor: procesando", numeros)
        time.sleep(6)  # Simula seis segundos de trabajo intensivo.

        resultado = {
            "cantidad": len(numeros),
            "suma": sum(numeros),
            "promedio": sum(numeros) / len(numeros),
            "mayor": max(numeros),
        }
        print("Servidor: procesamiento terminado")
        return resultado


def main():
    """Registra el servicio remoto en el Name Server."""
    daemon = Pyro4.Daemon(host="localhost")
    ns = Pyro4.locateNS(host="localhost", port=9090)
    uri = daemon.register(ProcesadorDatos())
    ns.register("practica.procesamiento", uri)

    print("Servidor de procesamiento iniciado")
    print("URI:", uri)
    print("Registrado como practica.procesamiento")
    daemon.requestLoop()


if __name__ == "__main__":
    main()
