from random import randint

print("\n")
nombre = input("Cual es tu nombre muchachon?? ")
jugar = input(f"Quieres jugar {nombre}? (s/n) ")

if jugar.lower() != "s":
    print("ALV pues ...")
    exit()

print("\nBienvenido a adivina el numero!!")
print("Las reglas son las siguientes:\nYo seleccionare un numero entre 1 y 100 y tendras 8 intentos para adivinar, tras cada intento te dare pistas en caso de fallar")
input("Presiona enter para empezar a jugar...")

print("\n")

numero = randint(1,100)
adivinado = False

for n in range(1,9):
    numero_usuario = input(f"intento numero {n}: Cual es el numero secreto? ")
    if numero == int(numero_usuario):
        print(f"Felicidades {nombre} has adivinado el numero secreto en {n} intentos")
        adivinado = True
        break
    elif int(numero_usuario) < 1 or int(numero_usuario) > 100:
        print("No manches... te dije que el numero secreto esta entre 1 y 100!")
    elif numero < int(numero_usuario):
        print("El numero secreto es menor")
    else:
        print("El numero secreto es mayor")

if not adivinado:
    print(f"\nLo siento {nombre} has agotado tus 8 intentos, el numero secreto era {numero}")

print("\n")