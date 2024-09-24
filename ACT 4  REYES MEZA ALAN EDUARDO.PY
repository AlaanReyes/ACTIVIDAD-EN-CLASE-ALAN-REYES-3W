print("#REYES MEZA ALAN EDUARDO : act- en clase-4 #NOMBRE PRACTICA Y DATOS DE PROGRAMADOR")
print(" ") #ESPACIO PARA AGREGAR LA INFO DE PRACTICA Y PROGRAMADOR

def calcular_promedio():
    try:
        # Solicitar al usuario que ingrese tres números
        numero1 = float(input("Ingrese el primer número: "))#ingresar primer valor
        numero2 = float(input("Ingrese el segundo número: "))#ingresar segundo valor
        numero3 = float(input("Ingrese el tercer número: ")) #ingresar tercer valor
        
        promedio = (numero1 + numero2 + numero3) / 3 # Calcular el promedio
        
        print(f"El promedio de los tres números es: {promedio:.2f}") # Mostrar el resultado

    except ValueError:
        print("Por favor, ingrese valores numéricos válidos.")#error si la entrada no es un número válido

calcular_promedio() # Ejecutar la función