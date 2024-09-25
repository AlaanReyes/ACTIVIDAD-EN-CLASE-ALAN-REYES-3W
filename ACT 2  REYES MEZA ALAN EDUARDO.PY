print("#REYES MEZA ALAN EDUARDO : act- en clase-2 #NOMBRE PRACTICA Y DATOS DE PROGRAMADOR")

print(" ") #ESPACIO PARA AGREGAR LA INFO DE PRACTICA Y PROGRAMADOR


def calcular_consumo():
    
    try:
        
        # Solicitar kilómetros recorridos y litros consumidos
        kilometros = float(input("Ingrese la cantidad de kilómetros recorridos: "))
        litros = float(input("Ingrese la cantidad de litros de combustible consumidos: "))

        # Verificar que los kilómetros sean mayores que cero
        if kilometros > 0:
            consumo_por_km = litros / kilometros  # Calcular consumo por km
            print(f"El consumo de combustible es: {consumo_por_km:.2f} litros por kilómetro.")
        else:
            print("La cantidad de kilómetros debe ser mayor que cero.")  # Mensaje de error

    except ValueError:
        print("Por favor, ingrese valores numéros válidos.")  # Manejo de error

# Ejecutar la función
calcular_consumo()  # Llama a la función para iniciar el programa 
