import tkinter as Tkinter
from tkinter import messagebox

from usuario import Usuario
from numero import Numero
from calculadora import Calculadora

#============METODOS PARA LAS FUNCIONES DE LOS BOTONES============

def calcular(operacion):
    nombre = entry_nombre.get()
    cedula = entry_cedula.get()

    """TRAEMOS EL NUMERO PERO ENTRA EN FORMATO STRING"""
    numero1 = entry_numero1.get()
    numero2 = entry_numero2.get()
    """CONVERTIMOS EL STRING DE NUMERO A VALOR NUMERICO"""
    obj_numero1 = Numero(numero1)
    obj_numero2 = Numero(numero2)

    obj_calculadora = Calculadora(obj_numero1, obj_numero2)

    if operacion == "suma":
        resultado = obj_calculadora.suma()
        tipo = "SUMA"
    elif operacion == "resta":
        resultado = obj_calculadora.resta()
        tipo = "RESTA"

    entry_operacion.delete(0, Tkinter.END)
    entry_operacion.insert(0, resultado)



def guardar_info():
 pass


#============INICIO DESDE LA PARTE VISUAL============
ventana = Tkinter.Tk()
ventana.title("Calculadora + Usuario")
ventana.geometry("1366x768")
"""CON TODOS ESTOS YA SE CREA LA VENTANA DE  LA CALCULADORA"""

#=====================================================


#============CONTINUO A CREAR LOS INPUTS============
Tkinter.Label(ventana, text="Nombre del Usuario:").pack()
entry_nombre = Tkinter.Entry(ventana)
entry_nombre.pack()

Tkinter.Label(ventana, text="Cedula del Usuario:").pack()
entry_cedula = Tkinter.Entry(ventana)
entry_cedula.pack()

Tkinter.Label(ventana, text="Primer Número:").pack()
entry_numero1 = Tkinter.Entry(ventana)
entry_numero1.pack()

Tkinter.Label(ventana, text="Segundo Número:").pack()
entry_numero2 = Tkinter.Entry(ventana)
entry_numero2.pack()

Tkinter.Label(ventana, text="Resultado de la Operación:").pack()
entry_operacion = Tkinter.Entry(ventana)
entry_operacion.pack()

"""CREAMOS EL AREA DE LA TABLA, RECRODAR QUE TENEMOS UN METODO EN CALCULADORA QUE SE LLAMA TABLA_TEXTO"""
tabla_texto = Tkinter.Text(ventana, height=12, width=50)
tabla_texto.pack(pady=10) #el pady baje mas la tabla y no quede pegada a resultado de la operacion

#==============================================================


#============INICIAMOS A LA CREACION DE BOTONES============

Tkinter.Button(ventana,text="Operacion SUMA", command=lambda: calcular("suma")).pack()

# Tkinter.Button(ventana,text="Guardar info + Limpiar campos e imprimir", command=guardar_info).pack() pass



ventana.mainloop()


