import tkinter as tkinter
from tkinter import messagebox
from parqueadero import parqueadero
from usuario import usuario
from carro import carro
import datetime


#=============INICIO DE METODOS=======================
# FUNCIÓN PARA REGISTRAR ENTRADA
def registrar_entrada():

    #datos que vamos a pedir a obtener
    nombre = entry_nombre.get()
    cedula = entry_cedula.get()
    placa = entry_placa.get()
    tipo = tipo_vehiculo.get()
    color = entry_color.get()
    pass


# FUNCIÓN PARA REGISTRAR SALIDA
def registrar_salida():
    pass

# FUNCIÓN PARA LIMPIAR
def Limpiar_campos():
    pass

# FUNCIÓN PARA MOSTRAR INFORMACIÓN COMPLETA
def mostrar_info_completa():
    pass


# ====== INIIO INTERFAZ VISUAL =========
ventana = tkinter.Tk()
ventana.title("PARQUEADERO & TIEMPOS")
ventana.geometry("1366x768")


 #====== TITULO ============
tkinter.Label(ventana, text="Parqueadero & Tiempos", font=("Arial", 16, "bold"), fg="blue").pack (pady=10)

#=====FRAME Y LABEL DE INFORMACION DEL PUESTO===

frame_puesto = tkinter.LabelFrame(ventana, text="Información del Puesto", padx=10, pady=10)
frame_puesto.pack(padx=20, pady=5, fill="x")

tkinter.Label(frame_puesto, text="PUESTO A OCUPAR  :").grid(row=0, column=0, sticky="w")
entry_puesto = tkinter.Entry(frame_puesto, width=20)
entry_puesto.grid(row=0, column=1, padx=5)

tkinter.Label(frame_puesto, text="ESTADO DEL PUESTO?  :").grid(row=1, column=0, sticky="w", pady=5)
entry_estado = tkinter.Entry(frame_puesto, width=20)
entry_estado.grid(row=1, column=1, padx=5)

#===== FRAME Y LABEL DE INFORMACION DEL USUARIO ===

frame_usuario = tkinter.LabelFrame(ventana, text="Datos del Cliente", padx=10, pady=10)
frame_usuario.pack(padx=20, pady=5, fill="x")

tkinter.Label(frame_usuario, text="NOMBRE:").grid(row=0, column=0, sticky="w", pady=5)
entry_nombre = tkinter.Entry(frame_usuario, width=30)
entry_nombre.grid(row=0, column=1, padx=5)

tkinter.Label(frame_usuario, text="CÉDULA:").grid(row=1, column=0, sticky="w", pady=5)
entry_cedula = tkinter.Entry(frame_usuario, width=30)
entry_cedula.grid(row=1, column=1, padx=5)

#===== FRAME Y LABEL DE INFORMACION DEL VEHICULO ===

"""Variable donde se guardará la opción seleccionada del radio button"""
tipo_vehiculo = tkinter.StringVar(value="Carro")

frame_vehiculo = tkinter.LabelFrame(ventana, text="Datos del Vehículo", padx=10, pady=10)
frame_vehiculo.pack(padx=20, pady=5, fill="x")

tkinter.Label(frame_vehiculo, text="TIPO DE VEHÍCULO:").grid(row=1, column=0, sticky="w", pady=5)

tkinter.Label(frame_vehiculo, text="TIPO DE VEHÍCULO:").grid(row=1, column=0, sticky="w", pady=5)

"""Frame para organizar los radio buttons"""
frame_radio = tkinter.Frame(frame_vehiculo)
frame_radio.grid(row=1, column=1, padx=5)

tkinter.Radiobutton(frame_radio, text="Carro", variable=tipo_vehiculo, value="Carro").pack(side="left")
tkinter.Radiobutton(frame_radio, text="Moto", variable=tipo_vehiculo, value="Moto").pack(side="left")
tkinter.Radiobutton(frame_radio, text="Camión", variable=tipo_vehiculo, value="Camión").pack(side="left")

tkinter.Label(frame_vehiculo, text="PLACA:").grid(row=0, column=0, sticky="w", pady=5)
entry_placa = tkinter.Entry(frame_vehiculo, width=30)
entry_placa.grid(row=0, column=1, padx=5)

tkinter.Label(frame_vehiculo, text="COLOR:").grid(row=2, column=0, sticky="w", pady=5)
entry_color = tkinter.Entry(frame_vehiculo, width=30)
entry_color.grid(row=2, column=1, padx=5)

# BOTONES PARA REGISTRAR-SALIR- & ACTUALIZAR
frame_botones = tkinter.Frame(ventana)
frame_botones.pack(pady=10)

btn_entrada = tkinter.Button(frame_botones, text="REGISTRAR ENTRADA", 
                        command=registrar_entrada,
                        bg="green", fg="white", width=15)
btn_entrada.pack(side="left", padx=5)

btn_salida = tkinter.Button(frame_botones, text="REGISTRAR SALIDA", 
                       command=registrar_salida,
                       bg="red", fg="white", width=15)
btn_salida.pack(side="left", padx=5)

btn_actualizar = tkinter.Button(frame_botones, text="ACTUALIZAR", 
                          command=mostrar_info_completa,
                          bg="blue", fg="white", width=15)
btn_actualizar.pack(side="left", padx=5)

#====AREA DE TABLA E IMPRESION DE DATOS=====
frame_infotabla = tkinter.LabelFrame(ventana, text="Información Detallada", padx=10, pady=10)
frame_infotabla.pack(padx=20, pady=10, fill="both", expand=True)

scrollbar = tkinter.Scrollbar(frame_infotabla)
scrollbar.pack(side="right", fill="y")

ventana.mainloop()