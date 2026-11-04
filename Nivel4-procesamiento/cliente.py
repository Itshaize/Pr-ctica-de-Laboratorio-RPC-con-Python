"""Nivel 4: cliente que continúa trabajando durante una llamada remota."""

import Pyro4


def main():
    """Envía una tarea al servidor y consulta su resultado más tarde."""
    ns = Pyro4.locateNS(host="localhost", port=9090)
    uri = ns.lookup("practica.procesamiento")
    servidor = Pyro4.Proxy(uri)

    # Las llamadas remotas devolverán un resultado futuro inmediatamente.
    Pyro4.asyncproxy(servidor)
    futuro = None
    notas = []

    while True:
        print("\n--- PROCESADOR DE DATOS ---")
        print("1. Enviar números para procesar")
        print("2. Escribir una nota mientras se procesa")
        print("3. Consultar el resultado")
        print("4. Salir")
        opcion = input("Elige una opción: ").strip()

        if opcion == "1":
            if futuro is not None:
                print("Primero consulta el resultado de la tarea anterior.")
                continue

            entrada = input("Números separados por comas (ej. 10,20,30): ")
            try:
                numeros = [float(valor.strip()) for valor in entrada.split(",")]
            except ValueError:
                print("Entrada no válida. Escribe solamente números.")
                continue

            futuro = servidor.procesar_numeros(numeros)
            print("Solicitud enviada. ¡Puedes seguir usando el menú!")

        elif opcion == "2":
            nota = input("Escribe una nota: ")
            notas.append(nota)
            print("Nota guardada localmente. Total de notas:", len(notas))

        elif opcion == "3":
            if futuro is None:
                print("Todavía no has enviado ninguna tarea.")
            elif not futuro.ready:
                print("El servidor todavía está procesando los datos.")
            else:
                try:
                    datos = futuro.value
                    print("Cantidad:", datos["cantidad"])
                    print("Suma:", datos["suma"])
                    print("Promedio:", datos["promedio"])
                    print("Mayor:", datos["mayor"])
                except (Pyro4.errors.PyroError, ValueError) as error:
                    print("No se pudo completar el trabajo:", error)
                futuro = None

        elif opcion == "4":
            servidor._pyroRelease()
            print("Cliente finalizado")
            break

        else:
            print("Opción no válida")


if __name__ == "__main__":
    try:
        main()
    except Pyro4.errors.PyroError as error:
        print("Error de conexión con Pyro4:", error)
