from http.server import HTTPServer, SimpleHTTPRequestHandler
import threading
import os
import time

consola = None
servidor = None
servidor_thread = None
ultima_ip = None
ultimo_puerto = None
ultima_carpeta = None

def iniciar_servidor(ip, puerto, carpeta):
    global servidor, servidor_thread, ultima_ip, ultimo_puerto, ultima_carpeta

    ultima_ip = ip
    ultimo_puerto = puerto
    ultima_carpeta = carpeta

    os.chdir(carpeta)
    direccion = (ip, int(puerto))
    servidor = HTTPServer(direccion, SimpleHTTPRequestHandler)

    def ejecutar():
        print(f"Servidor iniciado en http://{ip}:{puerto}")
        escribir_consola(f"Servidor iniciado en http://{ip}:{puerto}")
        servidor.serve_forever()

    servidor_thread = threading.Thread(target=ejecutar)
    servidor_thread.daemon =True
    servidor_thread.start()

def set_consola(ref_consola):
    global consola
    consola = ref_consola

def escribir_consola(mensaje):
    if consola is not None:
        consola.insert("end", mensaje + "\n")
        consola.see("end")

def funcion_iniciar():
    escribir_consola("Iniciando Servidor...")

def funcion_detener():
    def detener_y_mostrar():
        global servidor
        if servidor:
            escribir_consola("Deteniendo servidor...")
            servidor.shutdown()
            servidor.server_close()
            servidor = None
            escribir_consola("Servidor detenido")
        else:
            escribir_consola("No hay Servidor activo")
    threading.Thread(target=detener_y_mostrar).start()

def funcion_reiniciar():
    def reiniciar():
        global servidor
        if servidor:
            escribir_consola("Reseteando Servidor...")
            servidor.shutdown()
            servidor.server_close()
            servidor = None
            time.sleep(2)
        if ultima_ip and ultimo_puerto and ultima_carpeta:
            iniciar_servidor(ultima_ip, ultimo_puerto, ultima_carpeta)
        else:
            escribir_consola("No hay ajustes previos para reiniciar")
    threading.Thread(target=reiniciar).start()
