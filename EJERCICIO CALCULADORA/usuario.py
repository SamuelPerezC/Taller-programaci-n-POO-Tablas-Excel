class Usuario:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre
    
    def mostrar_info(self):
        print(f"Usuario: {self.nombre}")
        print(f"ID: {self.id}")
        
    