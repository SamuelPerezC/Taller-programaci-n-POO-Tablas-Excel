import tkinter as tk
from tkinter import messagebox
from parqueadero import parqueadero
from usuario import usuario
from carro import carro
import datetime

# Crear ventana
ventana = tk.Tk()
ventana.title("Sistema de Parqueadero")
ventana.geometry("450x650")  # Un poco más grande para más campos

# Crear objeto de parqueadero
mi_parqueadero = parqueadero("A1")

# FUNCIÓN PARA REGISTRAR ENTRADA
def registrar_entrada():
    # Validar disponibilidad
    if not mi_parqueadero.esta_disponible():
        messagebox.showerror("Error", f"Puesto {mi_parqueadero.get_numero_puesto()} ocupado")
        return
    
    # Obtener datos
    nombre = entry_nombre.get()
    cedula = entry_cedula.get()
    placa = entry_placa.get()
    tipo_vehiculo = entry_tipo_vehiculo.get()
    color = entry_color.get()
    
    # Validar campos vacíos
    if nombre == "" or cedula == "" or placa == "" or tipo_vehiculo == "" or color == "":
        messagebox.showerror("Error", "Todos los campos son obligatorios")
        return
    
    # Crear objetos y registrar
    nuevo_usuario = usuario(nombre, cedula, "Cliente")
    nuevo_carro = carro(placa, tipo_vehiculo, color)
    
    mi_parqueadero.registrar_entrada(nuevo_usuario, nuevo_carro)
    
    # Actualizar interfaz
    actualizar_interfaz()
    mostrar_info_completa()
    limpiar_campos()
    
    messagebox.showinfo("Éxito", "Entrada registrada correctamente")

# FUNCIÓN PARA REGISTRAR SALIDA
def registrar_salida():
    if mi_parqueadero.esta_disponible():
        messagebox.showerror("Error", f"El puesto {mi_parqueadero.get_numero_puesto()} ya está disponible")
        return
    
    # Registrar salida
    mi_parqueadero.registrar_salida()
    
    # Actualizar interfaz
    actualizar_interfaz()
    
    # Mostrar información actualizada
    mostrar_info_completa()
    
    messagebox.showinfo("Éxito", "Salida registrada correctamente")

# FUNCIÓN PARA ACTUALIZAR LA INTERFAZ
def actualizar_interfaz():
    # Actualizar estado
    entry_estado.config(state="normal")
    entry_estado.delete(0, tk.END)
    entry_estado.insert(0, mi_parqueadero.get_estado())
    entry_estado.config(state="readonly")

# FUNCIÓN PARA MOSTRAR INFORMACIÓN COMPLETA
def mostrar_info_completa():
    # Limpiar área de texto
    texto_info.delete(1.0, tk.END)
    
    # Mostrar información del puesto
    texto_info.insert(tk.END, "="*50 + "\n")
    texto_info.insert(tk.END, f"INFORMACIÓN DEL PUESTO {mi_parqueadero.get_numero_puesto()}\n")
    texto_info.insert(tk.END, "="*50 + "\n")
    
    texto_info.insert(tk.END, f"📌 Estado: {mi_parqueadero.get_estado()}\n")
    
    # Si está ocupado, mostrar información detallada
    if mi_parqueadero.get_estado() == "OCUPADO":
        usuario_actual = mi_parqueadero.get_usuario()
        carro_actual = mi_parqueadero.get_carro()
        
        if usuario_actual and carro_actual:
            texto_info.insert(tk.END, "\n USUARIO:\n")
            texto_info.insert(tk.END, f"   {usuario_actual.mostar_info()}\n")
            
            texto_info.insert(tk.END, "\n VEHÍCULO:\n")
            texto_info.insert(tk.END, f"   {carro_actual.mostrar_info()}\n")
            
            texto_info.insert(tk.END, "\n TIEMPO:\n")
            texto_info.insert(tk.END, f"   Entrada: {mi_parqueadero.get_fecha_entrada()} - {mi_parqueadero.get_hora_entrada()}\n")
            
            if mi_parqueadero.get_hora_salida():
                texto_info.insert(tk.END, f"   Salida: {mi_parqueadero.get_hora_salida()}\n")
                # Calcular tiempo
                mi_parqueadero.mostrar_tiempo_parqueo()  # Esto imprime en consola
    else:
        texto_info.insert(tk.END, "\n   El puesto está disponible\n")
    
    texto_info.insert(tk.END, "="*50 + "\n")

# FUNCIÓN PARA LIMPIAR CAMPOS
def limpiar_campos():
    entry_nombre.delete(0, tk.END)
    entry_cedula.delete(0, tk.END)
    entry_placa.delete(0, tk.END)
    entry_tipo_vehiculo.delete(0, tk.END)
    entry_color.delete(0, tk.END)

# CREACIÓN DE LA INTERFAZ
titulo = tk.Label(ventana, text="SISTEMA DE PARQUEADERO", 
                  font=("Arial", 16, "bold"), fg="navy")
titulo.pack(pady=10)

# Frame para información del puesto
frame_puesto = tk.LabelFrame(ventana, text="Información del Puesto", padx=10, pady=10)
frame_puesto.pack(padx=20, pady=5, fill="x")

tk.Label(frame_puesto, text="NÚMERO DE PUESTO:").grid(row=0, column=0, sticky="w")
entry_puesto = tk.Entry(frame_puesto, width=20)
entry_puesto.grid(row=0, column=1, padx=5)
entry_puesto.insert(0, mi_parqueadero.get_numero_puesto())
entry_puesto.config(state="readonly")

tk.Label(frame_puesto, text="ESTADO:").grid(row=1, column=0, sticky="w", pady=5)
entry_estado = tk.Entry(frame_puesto, width=20)
entry_estado.grid(row=1, column=1, padx=5)
entry_estado.insert(0, mi_parqueadero.get_estado())
entry_estado.config(state="readonly")

# Frame para datos del usuario
frame_usuario = tk.LabelFrame(ventana, text="Datos del Usuario", padx=10, pady=10)
frame_usuario.pack(padx=20, pady=5, fill="x")

tk.Label(frame_usuario, text="NOMBRE:").grid(row=0, column=0, sticky="w", pady=5)
entry_nombre = tk.Entry(frame_usuario, width=30)
entry_nombre.grid(row=0, column=1, padx=5)

tk.Label(frame_usuario, text="CÉDULA:").grid(row=1, column=0, sticky="w", pady=5)
entry_cedula = tk.Entry(frame_usuario, width=30)
entry_cedula.grid(row=1, column=1, padx=5)

# Frame para datos del vehículo
frame_vehiculo = tk.LabelFrame(ventana, text="Datos del Vehículo", padx=10, pady=10)
frame_vehiculo.pack(padx=20, pady=5, fill="x")

tk.Label(frame_vehiculo, text="PLACA:").grid(row=0, column=0, sticky="w", pady=5)
entry_placa = tk.Entry(frame_vehiculo, width=30)
entry_placa.grid(row=0, column=1, padx=5)

tk.Label(frame_vehiculo, text="TIPO DE VEHÍCULO:").grid(row=1, column=0, sticky="w", pady=5)
entry_tipo_vehiculo = tk.Entry(frame_vehiculo, width=30)
entry_tipo_vehiculo.grid(row=1, column=1, padx=5)

tk.Label(frame_vehiculo, text="COLOR:").grid(row=2, column=0, sticky="w", pady=5)
entry_color = tk.Entry(frame_vehiculo, width=30)
entry_color.grid(row=2, column=1, padx=5)

# Frame para botones
frame_botones = tk.Frame(ventana)
frame_botones.pack(pady=10)

btn_entrada = tk.Button(frame_botones, text="REGISTRAR ENTRADA", 
                        command=registrar_entrada,
                        bg="green", fg="white", width=15)
btn_entrada.pack(side="left", padx=5)

btn_salida = tk.Button(frame_botones, text="REGISTRAR SALIDA", 
                       command=registrar_salida,
                       bg="red", fg="white", width=15)
btn_salida.pack(side="left", padx=5)

btn_actualizar = tk.Button(frame_botones, text="ACTUALIZAR", 
                          command=mostrar_info_completa,
                          bg="blue", fg="white", width=15)
btn_actualizar.pack(side="left", padx=5)

#AREA DE TABLAS EN LABELFRAME PAR QUE QUEDE AGRUPADO VISUALMENTE
frame_info = tk.LabelFrame(ventana, text="Información Detallada", padx=10, pady=10)
frame_info.pack(padx=20, pady=10, fill="both", expand=True)

texto_info = tk.Text(frame_info, height=12, width=50)
texto_info.pack(side="left", fill="both", expand=True)

scrollbar = tk.Scrollbar(frame_info)
scrollbar.pack(side="right", fill="y")

texto_info.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=texto_info.yview)

# Mostrar información inicial
mostrar_info_completa()

ventana.mainloop()