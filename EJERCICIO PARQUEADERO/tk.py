import tkinter as tk
from tkinter import messagebox

from usuario import Usuario
from numero import Numero
from calculadora import Calculadora


# ===============================
# INTERFAZ GRÁFICA
# ===============================
ventana = tk.Tk()
ventana.title("Calculadora con toma de informacion")
ventana.geometry("400x500")

tk.Label(ventana, text="CALCULADORA + TOMA DE INFORMACION", font=("Arial", 14, "bold")).pack(pady=10)


#toma de informacion para los campos
def calcular():
    # 1️⃣ Obtener TODOS los datos
    nombre = entry_nombre.get()
    cedula = entry_cedula.get()
    valor1 = entry_numero1.get()
    valor2 = entry_numero2.get()

    # 2️⃣ Convertir números
    valor1 = int(valor1)
    valor2 = int(valor2)

    # 3️⃣ Crear objetos
    usuario = Usuario(nombre, cedula)
    numero1 = Numero(valor1)
    numero2 = Numero(valor2)

    # 4️⃣ Crear calculadora
    operacion = Calculadora(numero1, numero2)

    # 5️⃣ Ejecutar operación
    resultado = operacion.suma()
    resultado = operacion.resta()

    # 6️⃣ Mostrar resultado
    entry_resultado.delete(0, tk.END)
    entry_resultado.insert(0, resultado)

#CREAMOS LOS CAMPOS DE TOMA DE INFORMACION
tk.Label(ventana,text="Nombre").pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()

tk.Label(ventana, text="Id").pack()
entry_cedula = tk.Entry(ventana)
entry_cedula.pack()

tk.Label(ventana, text="Numero 1").pack()
entry_numero1= tk.Entry(ventana)
entry_numero1.pack()

tk.Label(ventana,text="numero 2").pack()
entry_numero2 = tk.Entry(ventana)
entry_numero2.pack()

tk.Label(ventana,text="Resultado para SUMA").pack()
entry_resultado = tk.Entry(ventana)
entry_resultado.pack()

tk.Label(ventana,text="Resultado para RESTA").pack()
entry_resta = tk.Entry(ventana)
entry_resta.pack()


#Botones
tk.Button(ventana, text="Calcular", command=calcular, bg="green", fg="white").pack(pady=5)


ventana.mainloop()




# # Crear una instancia de Usuario
# usuario1 = Usuario("Juan", 123)
# # Mostrar la información del usuario
# usuario1.mostrar_info()

# print("""--------------------------USUARIO-------------------------""")

# # Crear una instancia de Numero
# numero1 = Numero(10)
# numero2 = Numero(5)
# # Mostrar la información del número
# numero1.mostrar_info()
# numero2.mostrar_info()

# print("""-------------------------NUMERO-------------------------""")

# # Crear una instancia de Calculadorea
# operacion1 = Calculadora(numero1=numero1, numero2=numero2)

# # Realizar operaciones y mostrar resultados
# print(f"Suma: {operacion1.suma()}")
# print(f"Resta: {operacion1.resta()}")
# print(f"Multiplicación: {operacion1.multiplicacion()}")
# print(f"División: {operacion1.division()}")

# # Tomar una fecha y mostrarla
# operacion1.tomar_fecha("2024-06-01")
# operacion1.mostrar_fecha()

# print(""""----------OPERACIONES DE CALCULADORA  
      
#       ------------""")

# # Guardar información en una tabla y mostrarla
# operacion1.acumulador_texto(usuario1)
# operacion1.mostrar_tabla()

# print(""""---------------------ALMACENAMIENTO DE INFORMACION---------------------""")
