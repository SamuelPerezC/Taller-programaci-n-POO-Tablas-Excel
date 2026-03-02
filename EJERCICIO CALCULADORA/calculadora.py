class Calculadora:
    def __init__(self, operacion , fecha ):
        self.operacion = operacion
        self.texto_tabla = ""
        self.fecha = fecha  
        self.resultado = None  

    #-------------------------HACER OPERACIONES-------------------------#

    def hacer_suma(self, num1, num2):
        dato = int(num1) + int(num2)
        print(f"Suma: {dato}")
        self.resultado = dato  # Guardamos el resultado
        return dato
    
    def hacer_resta(self, num1, num2):
        dato = int(num1) - int(num2)
        print(f"Resta: {dato}")
        self.resultado = dato  # Guardamos el resultado
        return dato
    
    def hacer_operacion(self, obj_num1, obj_num2):
        if self.operacion == "suma":
            resultado = self.hacer_suma(obj_num1.get_numero(), obj_num2.get_numero())
            return resultado
        elif self.operacion == "resta":
            resultado = self.hacer_resta(obj_num1.get_numero(), obj_num2.get_numero())
            return resultado
        else:
            print("Operación no válida")
            return None

    #-------------------------TOMAR FECHA-------------------------#

    def tomar_fecha(self, fecha):
        self.fecha = fecha  
        
    def get_fecha(self):
        return self.fecha   
    
    def mostrar_fecha(self):
        print(f"Fecha: {self.fecha}")
        
    #====================TABLA PARA ALMACENAR DATOS DE USUARIO=========================#
    
    def acumulador_texto(self, obj_usuario, numero1, numero2):  
        self.texto_tabla += f" Cédula: {obj_usuario.get_id()} - Nombre: {obj_usuario.get_nombre()} - Número1: {numero1.get_numero()} - Número2: {numero2.get_numero()} - Operación: {self.operacion} - Resultado: {self.resultado} - Fecha: {self.fecha}\n"
    
    # Método para establecer la operación
    def set_operacion(self, operacion):
        self.operacion = operacion
    
    # Método para obtener la operación
    def get_operacion(self):
        return self.operacion
    
    # Método para obtener el resultado
    def get_resultado(self):
        return self.resultado
            
    def get_tabla(self):
        return self.texto_tabla  
    
    def mostrar_tabla(self):    
        print("             |Historial almacenado|         ")
        print(self.texto_tabla)
    
    # Método para limpiar la tabla si es necesario
    def limpiar_tabla(self):
        self.texto_tabla = ""