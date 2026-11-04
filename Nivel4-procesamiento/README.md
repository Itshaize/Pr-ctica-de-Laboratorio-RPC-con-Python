# Nivel 4 — Procesamiento asíncrono con Pyro4

Esta carpeta sigue el estilo de los niveles anteriores: un `server.py`, un `cliente.py`, `Pyro4.Daemon`, `Pyro4.locateNS()` y registro de un servicio llamado `practica.procesamiento`.

## Requisitos

- Python compatible con Pyro4 (se recomienda Python 3.10 para evitar problemas de compatibilidad).
- `python -m pip install Pyro4==4.82`

## Ejecución en tres terminales

1. **Terminal 1**: `python -m Pyro4.naming`
2. **Terminal 2**: `python server.py`
3. **Terminal 3**: `python cliente.py`

Deben quedar abiertas las primeras dos terminales mientras se utiliza el cliente.

## Prueba sugerida

1. Elige **1**, envía `10,20,30,40,50`.
2. Inmediatamente, elige **3** para comprobar que el servidor sigue trabajando. Luego elige **2** y escribe una nota.
3. Mientras procesa, puedes repetir **3** para consultar sin bloquear el menú.
4. Pasados los seis segundos, vuelve a elegir **3** y observa cantidad **5**, suma **150.0**, promedio **30.0**, mayor **50.0**.
5. Ejecuta otro `cliente.py` en una cuarta terminal para observar solicitudes de clientes independientes.

## ¿Qué demuestra?

- `@Pyro4.expose`: hace accesible el método remotamente.
- `Pyro4.locateNS()`: encuentra el Name Server.
- `daemon.register(...)` + `ns.register(...)`: registran el servicio.
- `Pyro4.asyncproxy(servidor)`: permite iniciar la llamada remota sin bloquear el menú del cliente.
- `futuro.ready`: consulta si el resultado ya está disponible.
- `futuro.value`: obtiene el resultado cuando está listo.
- `time.sleep(6)`: **simula** una operación costosa; no es un cálculo intensivo real. La suma, el promedio y el máximo son las operaciones de procesamiento reales.

## Compatibilidad con los demás niveles

El nombre `practica.procesamiento` es distinto de `practica.calculadora`, `practica.mensajeria` y `practica.banco`. Todos pueden utilizar el mismo Name Server en `localhost:9090` sin conflictos de nombre. Inicia **un solo** Name Server; cada servidor Pyro4 utiliza su propio puerto de servicio.

## Evidencias para el informe

Captura 1: Name Server ejecutándose. Captura 2: servidor registrado. Captura 3: cliente con solicitud enviada y nota creada mientras espera. Captura 4: resultado terminado.

**Nota:** La asincronía no significa que Pyro4 deje de esperar en todos los casos: si se consulta `futuro.value` antes de que esté listo, la lectura sí bloquea; por eso se verifica primero `futuro.ready`.
