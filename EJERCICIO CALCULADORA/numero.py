class Numero:
    def __init__(self,numero):
        self.numero = int(numero)
        """CONVERTIMOS EL NUMERO STRISNG  A NUMERO ENTERO YA QUE SIN EL INT PYTHON LOS VE COMO TEXTO Y LOS CONCATENA"""
        
    def get_numero(self):
        return self.numero
    
    def set_numero(self, numero):
        self.numero = numero
        
    def mostrar_info(self):
        print(f"Numero: {self.numero}")
        