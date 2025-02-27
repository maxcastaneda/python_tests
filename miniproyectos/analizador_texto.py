
print("\n")
texto = input("**Ingresa el texto a analizar: \n")
l1,l2,l3 = input("**Ingresa 3 letras a buscar: \n")

print("\n")
print(f"El texto tiene {texto.upper().count(l1.upper())} letras {l1}")
print(f"El texto tiene {texto.upper().count(l2.upper())} letras {l2}")
print(f"El texto tiene {texto.upper().count(l3.upper())} letras {l3}")

print("\n")
palabras = texto.split(" ")
# palabras = texto.split() # esto es igual que la linea anterior.
print(f"El texto tiene {len(palabras)} palabras")

print("\n")
print(f"La primer letra del texto es: {texto[0]}")
print(f"La ultima letra del texto es: {texto[::-1][0]}")

print("\n")
print(f"Tu frase en orden inverso es:\n{texto[::-1]}")

print("\n")
print(f"La palabra Python se encuentra en el texto: {"PYTHON" in texto.upper()}")

print("\n")