print ("REYES MEZA ALAN EDUARDO-act- en clase-5") #NOMBRE DE PRACTICA Y DATOS DEL PRGRAMADOR
print(" ") #ESPACIO PARA NOMBRE
import random # generar números aleatorios
numero_a_adivinar = random.randint(1, 50) #Genera un número aleatorio entre 1 y 50
intentos = 0  # Contador de intentos

print("Adivina el número entre 1 y 50.")

while True:
    try:
        adivinanza = int(input("Tu adivinanza: ")) # Solicita al usuario que ingrese su adivinanza
        intentos += 1  # Incrementa el contador de intentos
        
        if adivinanza < numero_a_adivinar: # Compara la adivinanza con el número a adivinar
            print("Mayor.")  # Indica que el número es mayor
        elif adivinanza > numero_a_adivinar:
            print("Menor.")  # Indica que el número es menor
        else:
            print(f"¡Correcto! {intentos} intentos.")  # Mensaje de éxito y número de intentos
            break  # Termina el bucle si se adivina correctamente
    except ValueError:
        print("Número inválido.") # error si un numero no es valido