print("#REYES MEZA ALAN EDUARDO : act- en clase-3 #NOMBRE PRACTICA Y DATOS DE PROGRAMADOR")
print(" ") #ESPACIO PARA AGREGAR LA INFO DE PRACTICA Y PROGRAMADOR

def convertir_fahrenheit_a_celsius():
    try:
        fahrenheit = float(input("Ingrese la temperatura en grados Fahrenheit: "))#Solicitar al usuario que ingrese la temperatura en Fahrenheit
        celsius = (5 / 9) * (fahrenheit - 32) #Convertir la temperatura a Celsius usando la fórmula
        print(f"La temperatura en grados Celsius es: {celsius:.2f}°C") # Mostrar el resultado
    
    except ValueError:
        print("Por favor, ingrese un valor numérico válido.") #error si la entrada no es un número válido

convertir_fahrenheit_a_celsius()#Ejecutar la función