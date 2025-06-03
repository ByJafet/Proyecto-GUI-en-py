import tkinter as tk
import Logica
from Logica import funcion_reiniciar
from tkinter import Button


ventana = tk.Tk() #Creamos la ventana
ventana.geometry("400x450") #Le ponemos una resolucion a la ventana
ventana.title("Server")

def iniciar_servidor_desde_gui():
    ip = entrada_IP.get()
    puerto = entrada_Puerto.get()
    carpeta = entrada_carpeta.get()
    Logica.iniciar_servidor(ip, puerto, carpeta)

# Consola
consola = tk.Text(ventana, height=10, width=60)
consola.pack(pady=10)

Logica.set_consola(consola)

#Etiqueta de Carpeta
etiqueta_Carpeta = tk.Label(ventana, text="Carpeta")
etiqueta_Carpeta.pack()

#Entrada de Texto de Carpeta
entrada_carpeta = tk.Entry(ventana, width=20)
entrada_carpeta.pack()

#Etiquetas de IP
etiqueta_IP = tk.Label(ventana, text="IP")
etiqueta_IP.pack()

#Entrada de texto de IP
entrada_IP = tk.Entry(ventana, width=20)
entrada_IP.pack()

#Etiqueta de Puerto
etiqueta_Puerto = tk.Label(ventana, width=20, text="Puerto")
etiqueta_Puerto.pack()

#Entrada de Texto de puerto
entrada_Puerto = tk.Entry(ventana, width=15)
entrada_Puerto.pack()


espaciador = tk.Frame(ventana, height=10)
espaciador.pack()
#Botones

#Boton para iniciar servidor
boton_iniciar  = tk.Button(ventana, padx=10,  text="Iniciar", command=iniciar_servidor_desde_gui)
boton_iniciar.pack()

espaciador = tk.Frame(ventana, height=10)
espaciador.pack()

boton_detener = tk.Button(ventana, padx=10, text="Detener", command=Logica.funcion_detener)
boton_detener.pack()

espaciador = tk.Frame(ventana, height=10)
espaciador.pack()

Button(ventana, text="Reiniciar servidor", command=funcion_reiniciar).pack()

ventana.mainloop()