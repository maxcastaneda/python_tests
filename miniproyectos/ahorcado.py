from faker import Faker
import re

def mostrar_palabra(palabra, adivinadas):
    display=""    
    for letra in palabra:
        if letra in adivinadas:
            display += letra + " "
        else:
            display += "_ "
    
    print("\n" + "*" * 50 + "\n")             
    print (display)

intentos_totales = 10

# generar palabra
fake = Faker('es_ES')

while True:
    nombre = fake.first_name().upper()
    unicas = set(nombre)
    if len(unicas) <= 6 and not bool(re.search(r"[áéíóúÁÉÍÓÚ]", nombre)):
        break

print("\n" + "*" * 50 )
print("\nVamos a jugar al ahorcado!")
print(
f"""
Instrucciones:
Las palabras a adivinar son nombres propios de personas en espanol.
Tendras {intentos_totales} intentos para adivinar las letras de la palabra.
"""
)
print("*" * 50 + "\n") 
input("Estas listo? Presiona ENTER para empezar")

adivinadas = set()
incorrectas = set()
intentos = 0
while True:
    mostrar_palabra(nombre, adivinadas)
    letra = input(f"Intento ({intentos}/{intentos_totales}) Ingresa una letra: ")
    
    if letra.upper() in incorrectas or letra.upper() in adivinadas:
        print(f"Ya intentaste con {letra}, intenta con otra letra!")
        continue

    if letra.upper() in nombre:
        adivinadas.add(letra.upper())
        print(f"Felicidades [{letra}] esta en la palabra!")
    else:
        incorrectas.add(letra.upper())
        print(f"Fallo! te quedan {intentos_totales-intentos-1} intentos")
        intentos += 1

    if len(unicas) == len(adivinadas):
        print(f"Felicidades! Adivinaste la palabra {nombre}")
        break

    if intentos == intentos_totales:
        print(f"Lo siento no adivinaste, la palabra era: {nombre}")
        break

print("\n")