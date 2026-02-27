from usuario import Usuario
from numero import Numero
from calculadora import Calculadora

# Crear una instancia de Usuario
usuario1 = Usuario("Juan", 123)
# Mostrar la información del usuario
usuario1.mostrar_info()

print("""--------------------------USUARIO-------------------------""")

# Crear una instancia de Numero
numero1 = Numero(10)
numero2 = Numero(5)
# Mostrar la información del número
numero1.mostrar_info()
numero2.mostrar_info()

print("""-------------------------NUMERO-------------------------""")

# Crear una instancia de Calculadorea
operacion1 = Calculadora(numero1=numero1, numero2=numero2)

# Realizar operaciones y mostrar resultados
print(f"Suma: {operacion1.suma()}")
print(f"Resta: {operacion1.resta()}")
print(f"Multiplicación: {operacion1.multiplicacion()}")
print(f"División: {operacion1.division()}")

# Tomar una fecha y mostrarla
operacion1.tomar_fecha("2024-06-01")
operacion1.mostrar_fecha()

print(""""----------OPERACIONES DE CALCULADORA  
      
      ------------""")

# Guardar información en una tabla y mostrarla
operacion1.acumulador_texto(usuario1)
operacion1.mostrar_tabla()

print(""""---------------------ALMACENAMIENTO DE INFORMACION---------------------""")
