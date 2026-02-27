import tkinter as tk
from tkinter import messagebox

from usuario import Usuario
from numero import Numero
from calculadora import Calculadora

# ===============================
# LISTA ACUMULADORA (HISTORIAL)
# ===============================
historial = []

# ===============================
# FUNCIONES
# ===============================

def calcular(tipo_de_operacion):
    try:
        nombre = entry_nombre.get()
        cedula = entry_cedula.get()
        valor1 = int(entry_numero1.get())
        valor2 = int(entry_numero2.get())

        usuario = Usuario(nombre, cedula)
        numero1 = Numero(valor1)
        numero2 = Numero(valor2)

        operacion = Calculadora(numero1, numero2)

        if tipo_de_operacion == "suma":
            resultado = operacion.suma()
            tipo = "SUMA"
        else:
            resultado = operacion.resta()
            tipo = "RESTA"

        entry_resultado.delete(0, tk.END)
        entry_resultado.insert(0, resultado)

        # Guardamos temporalmente la última operación
        global ultima_operacion
        ultima_operacion = {
            "nombre": nombre,
            "cedula": cedula,
            "valor1": valor1,
            "valor2": valor2,
            "tipo": tipo,
            "resultado": resultado
        }

    except ValueError:
        messagebox.showerror("Error", "Ingrese solo números válidos")


def guardar_e_imprimir():
    global ultima_operacion

    if "ultima_operacion" not in globals():
        messagebox.showwarning("Aviso", "Primero debe calcular una operación")
        return

    # Guardar en historial
    historial.append(ultima_operacion)

    # Limpiar tabla
    tabla_texto.delete("1.0", tk.END)

    # Encabezado tipo Excel
    tabla_texto.insert(tk.END, "Nombre\tCedula\tV1\tV2\tTipo\tResultado\n")
    tabla_texto.insert(tk.END, "-"*60 + "\n")

    # Imprimir todo el historial
    for item in historial:
        fila = f"{item['nombre']}\t{item['cedula']}\t{item['valor1']}\t{item['valor2']}\t{item['tipo']}\t{item['resultado']}\n"
        tabla_texto.insert(tk.END, fila)

    messagebox.showinfo("Éxito", "Operación guardada correctamente")


# ===============================
# INTERFAZ GRAFICA ACA MOSTRAMOS LOS TEXTOS VISUALES
# ===============================

ventana = tk.Tk()
ventana.title("Calculadora con Historial")
ventana.geometry("500x600")

tk.Label(ventana, text="CALCULADORA + TOMA DE INFORMACION", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(ventana,text="Nombre").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Cedula").pack()
entry_cedula = tk.Entry(ventana)
entry_cedula.pack()

tk.Label(ventana, text="Numero 1").pack()
entry_numero1= tk.Entry(ventana)
entry_numero1.pack()

tk.Label(ventana,text="Numero 2").pack()
entry_numero2 = tk.Entry(ventana)
entry_numero2.pack()

tk.Label(ventana,text="Resultado").pack()
entry_resultado = tk.Entry(ventana)
entry_resultado.pack()

tabla_texto = tk.Text(ventana, height=12, width=60)
tabla_texto.pack(pady=10)

# BOTONES
tk.Button(ventana, text="Calcular Suma", 
          command=lambda: calcular("suma"), 
          bg="green", fg="white").pack(pady=5)

tk.Button(ventana, text="Calcular Resta", 
          command=lambda: calcular("resta"), 
          bg="blue", fg="white").pack(pady=5)

tk.Button(ventana, text="Guardar e Imprimir Lista", 
          command=guardar_e_imprimir, 
          bg="purple", fg="white").pack(pady=10)

ventana.mainloop()