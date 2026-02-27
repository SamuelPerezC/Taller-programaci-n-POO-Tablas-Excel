class usuario:
    def __init__(self,nombre_usuario,cedula_usuario,tipo_usuario):
        self.nombre_usuario=nombre_usuario
        self.cedula_usuario=cedula_usuario
        self.tipo_usuario=tipo_usuario
        
    def get_nombre(self):
        return self.nombre_usuario
    
    def set_nombre(self,nuevo_nombre_usuario):
        self.nombre_usuario = nuevo_nombre_usuario
        
    def get_cedula(self):
        return self.cedula_usuario
    
    def set_cedula(self, nuevo_cedula_usuario):
        self.cedula_usuario = nuevo_cedula_usuario   
        
    def get_tipo(self):
        return self.tipo_usuario
    
    def set_tipo(self,nuevo_tipo_usuario):
        self.tipo_usuario = nuevo_tipo_usuario 
        
    def mostar_info(self):
        return f"Usuario: {self.nombre_usuario}, Cedula: {self.cedula_usuario}, tipo: {self.tipo_usuario}"
        
           