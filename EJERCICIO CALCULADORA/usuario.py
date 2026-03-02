class Usuario:
    def __init__(self, nombre, id):
        self.nombre = nombre
        self.id = id
    
    def get_nombre(self):
        return self.nombre
    
    def set_nombre(self, nombre):
        self.nombre = nombre

    def get_id(self):
        return self.id
    
    def set_id(self, id):
        self.id = id
    
    def mostrar_info(self):
        print(f"Usuario: {self.nombre}")
        print(f"ID: {self.id}")
        
    