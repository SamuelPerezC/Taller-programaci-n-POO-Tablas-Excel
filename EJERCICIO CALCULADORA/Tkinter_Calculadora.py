import tkinter as Tkinter
from tkinter import messagebox
from datetime import datetime

from usuario import Usuario
from numero import Numero
from calculadora import Calculadora

#============METODOS PARA LAS FUNCIONES DE LOS BOTONES============

def tomar_datos(entry_nombre, entry_cedula, obj_usuario):
   nombre = entry_nombre.get()
   cedula = entry_cedula.get()
   if nombre and cedula:
       obj_usuario.set_nombre(nombre)
       obj_usuario.set_id(cedula)
       messagebox.showinfo("Éxito", "Datos de usuario guardados")
   else:
       messagebox.showwarning("Advertencia", "Complete todos los campos")

def tomar_calculo(entry_numero1, entry_numero2, obj_num1, obj_num2):
    numero1 = entry_numero1.get()
    numero2 = entry_numero2.get()
    if numero1 and numero2:
        obj_num1.set_numero(numero1)
        obj_num2.set_numero(numero2)
        messagebox.showinfo("Éxito", "Números guardados")
    else:
        messagebox.showwarning("Advertencia", "Ingrese ambos números")

def hacer_operacion(entry_operacion, obj_num1, obj_num2, obj_calculadora, entry_resultado):
    try:
        tipo_operacion = entry_operacion.get()
        if tipo_operacion.lower() not in ["suma", "resta"]:
            messagebox.showwarning("Advertencia", 'Operación debe ser "suma" o "resta"')
            return
            
        obj_calculadora.operacion = tipo_operacion
        resultado = obj_calculadora.hacer_operacion(obj_num1, obj_num2)
        
        # Limpiar y mostrar resultado
        entry_resultado.delete(0, Tkinter.END)
        entry_resultado.insert(0, str(resultado))
        
    except Exception as e:
        messagebox.showerror("Error", f"Error en operación: {str(e)}")

def guardar_info(obj_usuario, obj_num1, obj_num2, obj_calculadora, entry_fecha, tabla_texto):
    try:
        # Validar datos
        if not obj_usuario.get_nombre() or not obj_usuario.get_id():
            messagebox.showwarning("Advertencia", "Primero guarde datos de usuario")
            return
            
        if not obj_num1.get_numero() or not obj_num2.get_numero():
            messagebox.showwarning("Advertencia", "Primero guarde los números")
            return
            
        if not obj_calculadora.resultado:
            messagebox.showwarning("Advertencia", "Primero realice una operación")
            return
        
        # Tomar fecha actual
        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        obj_calculadora.tomar_fecha(fecha_actual)
        entry_fecha.delete(0, Tkinter.END)
        entry_fecha.insert(0, fecha_actual)
        
        # Acumular en texto_tabla
        obj_calculadora.acumulador_texto(obj_usuario, obj_num1, obj_num2)
        
        # Mostrar en tabla_texto
        tabla_texto.delete("1.0", Tkinter.END)
        tabla_texto.insert(Tkinter.END, obj_calculadora.get_tabla())
        
        messagebox.showinfo("Éxito", "Información guardada")
        
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar: {str(e)}")

def limpiar_campos(entry_nombre, entry_cedula, entry_numero1, entry_numero2, 
                   entry_operacion, entry_resultado, entry_fecha):
    entry_nombre.delete(0, Tkinter.END)
    entry_cedula.delete(0, Tkinter.END)
    entry_numero1.delete(0, Tkinter.END)
    entry_numero2.delete(0, Tkinter.END)
    entry_operacion.delete(0, Tkinter.END)
    entry_resultado.delete(0, Tkinter.END)
    entry_fecha.delete(0, Tkinter.END)

# Crear objetos
obj_usuario = Usuario("", "")
obj_num1 = Numero("")
obj_num2 = Numero("")
obj_calculadora = Calculadora("", "")

#============INICIO INTERFAZ VISUAL============
ventana = Tkinter.Tk()
ventana.title("Calculadora + Usuario")
ventana.geometry("700x700")
ventana.resizable(False, False)

# Título
Tkinter.Label(ventana, text="CALCULADORA CON HISTORIAL", 
             font=("Arial", 16, "bold"), fg="blue").pack(pady=10)

#============SECCIÓN USUARIO============
Tkinter.Label(ventana, text="DATOS DEL USUARIO", 
             font=("Arial", 12, "bold")).pack(pady=5)

frame_usuario = Tkinter.Frame(ventana)
frame_usuario.pack()

Tkinter.Label(frame_usuario, text="Nombre:", width=10, anchor="w").grid(row=0, column=0, padx=5, pady=5)
entry_nombre = Tkinter.Entry(frame_usuario, width=30)
entry_nombre.grid(row=0, column=1, padx=5, pady=5)

Tkinter.Label(frame_usuario, text="Cédula:", width=10, anchor="w").grid(row=1, column=0, padx=5, pady=5)
entry_cedula = Tkinter.Entry(frame_usuario, width=30)
entry_cedula.grid(row=1, column=1, padx=5, pady=5)

Tkinter.Button(frame_usuario, text="Guardar Usuario", 
              command=lambda: tomar_datos(entry_nombre, entry_cedula, obj_usuario),
              bg="lightblue").grid(row=2, column=0, columnspan=2, pady=10)

#============SECCIÓN NÚMEROS============
Tkinter.Label(ventana, text="NÚMEROS A OPERAR", 
             font=("Arial", 12, "bold")).pack(pady=5)

frame_numeros = Tkinter.Frame(ventana)
frame_numeros.pack()

Tkinter.Label(frame_numeros, text="Número 1:", width=10, anchor="w").grid(row=0, column=0, padx=5, pady=5)
entry_numero1 = Tkinter.Entry(frame_numeros, width=30)
entry_numero1.grid(row=0, column=1, padx=5, pady=5)

Tkinter.Label(frame_numeros, text="Número 2:", width=10, anchor="w").grid(row=1, column=0, padx=5, pady=5)
entry_numero2 = Tkinter.Entry(frame_numeros, width=30)
entry_numero2.grid(row=1, column=1, padx=5, pady=5)

Tkinter.Button(frame_numeros, text="Guardar Números", 
              command=lambda: tomar_calculo(entry_numero1, entry_numero2, obj_num1, obj_num2),
              bg="lightgreen").grid(row=2, column=0, columnspan=2, pady=10)

#============SECCIÓN OPERACIÓN============
Tkinter.Label(ventana, text="REALIZAR OPERACIÓN", 
             font=("Arial", 12, "bold")).pack(pady=5)

frame_operacion = Tkinter.Frame(ventana)
frame_operacion.pack()

Tkinter.Label(frame_operacion, text="Operación:", width=10, anchor="w").grid(row=0, column=0, padx=5, pady=5)
entry_operacion = Tkinter.Entry(frame_operacion, width=30)
entry_operacion.grid(row=0, column=1, padx=5, pady=5)
entry_operacion.insert(0, "suma")

Tkinter.Label(frame_operacion, text="Resultado:", width=10, anchor="w").grid(row=1, column=0, padx=5, pady=5)
entry_resultado = Tkinter.Entry(frame_operacion, width=30, bg="lightyellow")
entry_resultado.grid(row=1, column=1, padx=5, pady=5)

Tkinter.Button(frame_operacion, text="Realizar Operación", 
              command=lambda: hacer_operacion(entry_operacion, obj_num1, obj_num2, obj_calculadora, entry_resultado),
              bg="orange").grid(row=2, column=0, columnspan=2, pady=10)

#============SECCIÓN FECHA============
Tkinter.Label(ventana, text="FECHA", 
             font=("Arial", 12, "bold")).pack(pady=5)

frame_fecha = Tkinter.Frame(ventana)
frame_fecha.pack()

Tkinter.Label(frame_fecha, text="Fecha:", width=10, anchor="w").grid(row=0, column=0, padx=5, pady=5)
entry_fecha = Tkinter.Entry(frame_fecha, width=30, bg="lightgray")
entry_fecha.grid(row=0, column=1, padx=5, pady=5)

#============BOTONES DE ACCIÓN============
frame_botones = Tkinter.Frame(ventana)
frame_botones.pack(pady=10)

Tkinter.Button(frame_botones, text="Guardar Información", 
              command=lambda: guardar_info(obj_usuario, obj_num1, obj_num2, obj_calculadora, 
                                          entry_fecha, tabla_texto),
              bg="purple", fg="white", width=18).grid(row=0, column=0, padx=5)

Tkinter.Button(frame_botones, text="Limpiar Campos", 
              command=lambda: limpiar_campos(entry_nombre, entry_cedula, entry_numero1, 
                                            entry_numero2, entry_operacion, entry_resultado, entry_fecha),
              bg="gray", fg="white", width=18).grid(row=0, column=1, padx=5)

#============HISTORIAL============
Tkinter.Label(ventana, text="HISTORIAL", 
             font=("Arial", 12, "bold")).pack(pady=5)

frame_historial = Tkinter.Frame(ventana)
frame_historial.pack(pady=5)

scrollbar = Tkinter.Scrollbar(frame_historial)
scrollbar.pack(side=Tkinter.RIGHT, fill=Tkinter.Y)

tabla_texto = Tkinter.Text(frame_historial, height=10, width=70, 
                          yscrollcommand=scrollbar.set)
tabla_texto.pack(side=Tkinter.LEFT, fill=Tkinter.BOTH)

scrollbar.config(command=tabla_texto.yview)
tabla_texto.insert(Tkinter.END, "Historial aparecerá aquí...")

ventana.mainloop()