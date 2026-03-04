import tkinter as tkinter
from tkinter import messagebox
from parqueadero import parqueadero
from usuario import usuario
from carro import carro

#=============INICIO DE METODOS=======================

# Lista donde guardaremos todos los puestos
lista_parqueaderos = []

# Acumulador de texto para historial
texto_historial = ""

# FUNCIÓN PARA REGISTRAR ENTRADA
def registrar_entrada():

    #datos que vamos a pedir a obtener
    numero_puesto = entry_puesto.get()
    nombre = entry_nombre.get()
    cedula = entry_cedula.get()
    placa = entry_placa.get()
    tipo = tipo_vehiculo.get()
    color = entry_color.get()

    if numero_puesto == "" or nombre == "" or cedula == "" or placa == "" or color == "":
        messagebox.showwarning("Error", "Todos los campos son obligatorios")
        return

    # Verificar si el puesto ya está ocupado
    for puesto in lista_parqueaderos:
        if puesto.get_numero_puesto() == numero_puesto and puesto.get_estado() == "OCUPADO":
            messagebox.showerror("Este puesto ya está ocupado")
            return

    nuevo_usuario = usuario(nombre, cedula, "Cliente")
    nuevo_carro = carro(placa, tipo, color)
    nuevo_puesto = parqueadero(numero_puesto)

    nuevo_puesto.registrar_entrada(nuevo_usuario, nuevo_carro)

    lista_parqueaderos.append(nuevo_puesto)

    # ===== ACUMULADOR DE TEXTO =====
    global texto_historial

    texto_historial += (
        f"Cédula: {nuevo_usuario.get_cedula()} - "
        f"Nombre: {nuevo_usuario.get_nombre()} - "
        f"Puesto: {numero_puesto} - "
        f"Placa: {nuevo_carro.get_placa_vehiculo()} - "
        f"Tipo: {nuevo_carro.get_tipo_carro()} - "
        f"Color: {nuevo_carro.get_color_carro()} - "
        f"Entrada: {nuevo_puesto.get_fecha_entrada()} {nuevo_puesto.get_hora_entrada()} - "
        f"Estado: OCUPADO\n"
    )

    entry_estado.delete(0, tkinter.END)
    entry_estado.insert(0, "OCUPADO")

    messagebox.showinfo(f"Entrada registrada en puesto {numero_puesto}")


# FUNCIÓN PARA REGISTRAR SALIDA
def registrar_salida():

    numero_puesto = entry_puesto.get()

    if numero_puesto == "":
        messagebox.showwarning("Ingrese número de puesto")
        return

    for puesto in lista_parqueaderos:
        if puesto.get_numero_puesto() == numero_puesto:

            if puesto.get_estado() == "DISPONIBLE":
                messagebox.showinfo("El puesto ya está disponible")
                return

            puesto.registrar_salida()

            # ===== ACUMULADOR DE TEXTO =====
            global texto_historial

            texto_historial += (
                f"Puesto: {numero_puesto} - "
                f"Salida: {puesto.get_hora_salida()} - "
                f"Estado: DISPONIBLE\n"
            )

            entry_estado.delete(0, tkinter.END)
            entry_estado.insert(0, "DISPONIBLE")

            messagebox.showinfo(f"Salida registrada del puesto {numero_puesto}")
            return

    messagebox.showerror("Puesto no encontrado")


# FUNCIÓN PARA LIMPIAR
def Limpiar_campos():
    entry_puesto.delete(0, tkinter.END)
    entry_estado.delete(0, tkinter.END)
    entry_nombre.delete(0, tkinter.END)
    entry_cedula.delete(0, tkinter.END)
    entry_placa.delete(0, tkinter.END)
    entry_color.delete(0, tkinter.END)

    tipo_vehiculo.set("Carro")


# FUNCIÓN PARA MOSTRAR INFORMACIÓN COMPLETA
def imprimir_historial():

    global texto_historial

    if texto_historial == "":
        messagebox.showinfo("No hay registros aún")
        return

    # Limpiar área antes de imprimir
    area_texto.delete("1.0", tkinter.END)

    
    area_texto.insert(tkinter.END, texto_historial)
    


# ====== INIIO INTERFAZ VISUAL =========
ventana = tkinter.Tk()
ventana.title("PARQUEADERO & TIEMPOS")
ventana.geometry("1366x768")

#====== TITULO ============
tkinter.Label(ventana, text="Parqueadero & Tiempos", font=("Arial", 16, "bold"), fg="blue").pack(pady=10)

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
tipo_vehiculo = tkinter.StringVar(value="Carro")

frame_vehiculo = tkinter.LabelFrame(ventana, text="Datos del Vehículo", padx=10, pady=10)
frame_vehiculo.pack(padx=20, pady=5, fill="x")

tkinter.Label(frame_vehiculo, text="PLACA:").grid(row=0, column=0, sticky="w", pady=5)
entry_placa = tkinter.Entry(frame_vehiculo, width=30)
entry_placa.grid(row=0, column=1, padx=5)

tkinter.Label(frame_vehiculo, text="TIPO DE VEHÍCULO:").grid(row=1, column=0, sticky="w", pady=5)

frame_radio = tkinter.Frame(frame_vehiculo)
frame_radio.grid(row=1, column=1, padx=5)

tkinter.Radiobutton(frame_radio, text="Carro", variable=tipo_vehiculo, value="Carro").pack(side="left")
tkinter.Radiobutton(frame_radio, text="Moto", variable=tipo_vehiculo, value="Moto").pack(side="left")
tkinter.Radiobutton(frame_radio, text="Camión", variable=tipo_vehiculo, value="Camión").pack(side="left")

tkinter.Label(frame_vehiculo, text="COLOR:").grid(row=2, column=0, sticky="w", pady=5)
entry_color = tkinter.Entry(frame_vehiculo, width=30)
entry_color.grid(row=2, column=1, padx=5)

# BOTONES PARA REGISTRAR-SALIR- & LIMPIAR
frame_botones = tkinter.Frame(ventana)
frame_botones.pack(pady=10)

tkinter.Button(frame_botones, text="REGISTRAR ENTRADA", command=registrar_entrada, bg="green", fg="white", width=18).pack(side="left", padx=5)
tkinter.Button(frame_botones, text="REGISTRAR SALIDA", command=registrar_salida, bg="red", fg="white", width=18).pack(side="left", padx=5)
tkinter.Button(frame_botones, text="LIMPIAR CAMPOS", command=Limpiar_campos, bg="blue", fg="white", width=18).pack(side="left", padx=5)
tkinter.Button(frame_botones, text="IMPRIMIR HISTORIAL", command=imprimir_historial, bg="purple", fg="white", width=18).pack(side="left", padx=5)

#====AREA DE TABLA E IMPRESION DE DATOS=====
frame_infotabla = tkinter.LabelFrame(ventana, text="Información Detallada", padx=10, pady=10)
frame_infotabla.pack(padx=20, pady=10, fill="both", expand=True)

scrollbar = tkinter.Scrollbar(frame_infotabla)
scrollbar.pack(side="right", fill="y")

area_texto = tkinter.Text(frame_infotabla, yscrollcommand=scrollbar.set)
area_texto.pack(fill="both", expand=True)

scrollbar.config(command=area_texto.yview)

ventana.mainloop()