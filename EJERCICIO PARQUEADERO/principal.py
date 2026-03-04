from usuario import usuario
from carro import carro
from parqueadero import parqueadero

print("="*50)
print("BIENVENIDO AL SISTEMA DE PARQUEADERO")
print("="*50)

# Variable para guardar el puesto actual
puesto_actual = None

while True:
    print("\n" + "="*50)
    print("MENÚ PRINCIPAL")
    print("="*50)
    print("1. Registrar entrada")
    print("2. Registrar salida")
    print("3. Ver información")
    print("4. Salir")
    print("="*50)
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        print("\n--- REGISTRAR ENTRADA ---")
        
        # Pedir datos
        nombre = input("Nombre del usuario: ")
        cedula = input("Cédula: ")
        tipo = input("Tipo de usuario: ")
        placa = input("Placa del vehículo: ")
        tipo_carro = input("Tipo de vehículo: ")
        color = input("Color: ")
        num_puesto = input("Número de puesto: ")
        
        # Crear objetos
        usuario1 = usuario(nombre, cedula, tipo)
        carro1 = carro(placa, tipo_carro, color)
        puesto_actual = parqueadero(num_puesto)
        
        # Registrar entrada
        puesto_actual.registrar_entrada(usuario1, carro1)
        print(f"✅ Entrada registrada en puesto {num_puesto}")
        
    elif opcion == "2":
        print("\n--- REGISTRAR SALIDA ---")
        
        if puesto_actual is None:
            print("Primero debe registrar una entrada")
        elif puesto_actual.esta_disponible():
            print("El puesto ya está disponible")
        else:
            puesto_actual.registrar_salida()
            print("✅ Salida registrada")
    
    elif opcion == "3":
        print("\n--- INFORMACIÓN ---")
        
        if puesto_actual is None:
            print("No hay información registrada")
        else:
            puesto_actual.mostrar_info()
    
    elif opcion == "4":
        print("\n👋 ¡Gracias por usar el sistema!")
        break
    
    else:
        print("❌ Opción no válida")
    
    input("\nPresione Enter para continuar...")