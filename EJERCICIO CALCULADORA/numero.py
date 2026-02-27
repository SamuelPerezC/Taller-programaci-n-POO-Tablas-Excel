class Numero:
    def __init__(self,numero):
        self.numero = numero
        
    def get_numero(self):
        return self.numero
    
    def set_numero(self, numero):
        self.numero = numero
        
    def mostrar_info(self):
        print(f"Numero: {self.numero}")
        