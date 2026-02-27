# parqueadero.py
import datetime

class parqueadero:
    def __init__(self, numero_puesto):
        self.numero_puesto = numero_puesto
        self.usuario = None
        self.carro = None
        self.fecha_entrada = None
        self.hora_entrada = None
        self.hora_salida = None
        self.estado = "DISPONIBLE"  # DISPONIBLE u OCUPADO
    
    # --- GETTERS Y SETTERS (lo que están aprendiendo) ---
    
    def get_numero_puesto(self):
        return self.numero_puesto
    
    def set_numero_puesto(self, nuevo_numero):
        self.numero_puesto = nuevo_numero
    
    def get_usuario(self):
        return self.usuario
    
    def set_usuario(self, nuevo_usuario):
        self.usuario = nuevo_usuario
    
    def get_carro(self):
        return self.carro
    
    def set_carro(self, nuevo_carro):
        self.carro = nuevo_carro
    
    def get_fecha_entrada(self):
        return self.fecha_entrada
    
    def set_fecha_entrada(self, nueva_fecha):
        self.fecha_entrada = nueva_fecha
    
    def get_hora_entrada(self):
        return self.hora_entrada
    
    def set_hora_entrada(self, nueva_hora):
        self.hora_entrada = nueva_hora
    
    def get_hora_salida(self):
        return self.hora_salida
    
    def set_hora_salida(self, nueva_hora):
        self.hora_salida = nueva_hora
    
    def get_estado(self):
        return self.estado
    
    def set_estado(self, nuevo_estado):
        self.estado = nuevo_estado
    
    # --- MÉTODOS PRINCIPALES ---
    
    def registrar_entrada(self, usuario, carro):
        """Registra la entrada de un vehículo"""
        self.set_usuario(usuario)
        self.set_carro(carro)
        
        ahora = datetime.datetime.now()
        self.set_fecha_entrada(ahora.strftime("%d/%m/%Y"))
        self.set_hora_entrada(ahora.strftime("%H:%M:%S"))
        self.set_estado("OCUPADO")
        
        print(f"\n✅ Entrada registrada en el puesto {self.get_numero_puesto()}")
        print(f"   Fecha: {self.get_fecha_entrada()}")
        print(f"   Hora: {self.get_hora_entrada()}")
    
    def registrar_salida(self):
        """Registra la salida de un vehículo"""
        if self.get_estado() == "DISPONIBLE":
            print(f"\n❌ El puesto {self.get_numero_puesto()} ya está disponible")
            return
        
        ahora = datetime.datetime.now()
        self.set_hora_salida(ahora.strftime("%H:%M:%S"))
        self.set_estado("DISPONIBLE")
        
        print(f"\n✅ Salida registrada del puesto {self.get_numero_puesto()}")
        print(f"   Hora de salida: {self.get_hora_salida()}")
        self.mostrar_tiempo_parqueo()
    
    def mostrar_info(self):
        """Muestra toda la información del puesto"""
        print("\n" + "="*50)
        print(f"INFORMACIÓN DEL PUESTO {self.get_numero_puesto()}")
        print("="*50)
        
        print(f"📌 Estado: {self.get_estado()}")
        
        if self.get_estado() == "OCUPADO" and self.get_usuario() and self.get_carro():
            usuario = self.get_usuario()
            carro = self.get_carro()
            
            print("\n👤 USUARIO:")
            print(f"   Nombre: {usuario.get_nombre()}")
            print(f"   Cédula: {usuario.get_cedula()}")
            print(f"   Tipo: {usuario.get_tipo()}")
            
            print("\n🚗 VEHÍCULO:")
            print(f"   Placa: {carro.get_placa_vehiculo()}")
            print(f"   Tipo: {carro.get_tipo_carro()}")
            print(f"   Color: {carro.get_color_carro()}")
            
            print("\n⏱️  TIEMPOS:")
            print(f"   Entrada: {self.get_fecha_entrada()} - {self.get_hora_entrada()}")
            if self.get_hora_salida():
                print(f"   Salida: {self.get_hora_salida()}")
        else:
            print("\n   El puesto está disponible")
        
        print("="*50)
    
    def mostrar_tiempo_parqueo(self):
        """Calcula y muestra el tiempo de parqueo"""
        if self.get_fecha_entrada() and self.get_hora_entrada() and self.get_hora_salida():
            entrada = datetime.datetime.strptime(
                f"{self.get_fecha_entrada()} {self.get_hora_entrada()}", 
                "%d/%m/%Y %H:%M:%S"
            )
            salida = datetime.datetime.strptime(
                f"{self.get_fecha_entrada()} {self.get_hora_salida()}", 
                "%d/%m/%Y %H:%M:%S"
            )
            
            tiempo = salida - entrada
            minutos = int(tiempo.total_seconds() / 60)
            
            if minutos < 60:
                print(f"⏱️  Tiempo total: {minutos} minutos")
            else:
                horas = minutos // 60
                mins = minutos % 60
                print(f"⏱️  Tiempo total: {horas} horas y {mins} minutos")
    
    def esta_disponible(self):
        """Retorna True si el puesto está disponible"""
        return self.get_estado() == "DISPONIBLE"
    
    def esta_ocupado(self):
        """Retorna True si el puesto está ocupado"""
        return self.get_estado() == "OCUPADO"