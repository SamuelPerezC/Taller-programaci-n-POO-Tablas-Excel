class carro:
    def __init__(self,placa_vehiculo,tipo_carro,color_carro):
        self.placa_vehiculo=placa_vehiculo
        self.tipo_carro=tipo_carro
        self.color_carro=color_carro
        
    def get_placa_vehiculo(self):
        return self.placa_vehiculo
    
    def set_placa_vehiculo(self,nueva_placa_vehiculo):
        self.placa_vehiculo=nueva_placa_vehiculo
    
    
    def get_tipo_carro(self):
        return self.tipo_carro
    
    def set_tipo_carro(self,nuevo_tipo_carro):
        self.tipo_carro=nuevo_tipo_carro
        
    
    def get_color_carro(self):
        return self.color_carro
    
    def set_color_carro(self,nuevo_color_carro):
        self.color_carro=nuevo_color_carro
        
    
    def mostrar_info(self):
        return f"Placa Vehiculo: {self.placa_vehiculo}, Tipo Carro:{self.tipo_carro}, Color Vehiculo: {self.color_carro}"
        
        