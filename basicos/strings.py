print("\n")


# buscar dentro de un string
mi_texto="Esto es una prueba"
print (f"{mi_texto[0]}")
print (f"{mi_texto[-1]}")
print (f"{mi_texto.index("n")}")
print (f"{mi_texto.rindex("n")}")
print (f"{mi_texto.find("W")}")

# hacer slicing 
texto = "ABCDEFGHIJKLM"
fragmento = texto[2:5]
print(fragmento)
print("abcdefgh"[2:10:2])
print("abcdefgh"[::-1])

# conversion a mayusculas y minusculas
texto = "Este es el texto de Federico"
print(texto.upper())
print(texto.lower())

#split y join
print(texto.split())
textoCSV = "aa,123,4545,dffd,asa"
print(textoCSV.split(","))
print(" ".join(["esto","es","una","frase"]))

# reemplazar texto
print(texto.replace("Federico","Massimo"))

# textos multilinea y busqueda en cadenas
poema = """
esto es un poema que
contiene multiples lineas
y se declara con comillas triples.
"""
print (poema)
print ("texto" in "este es el texto")
print ("texto" not in "este es el texto")
print(len(poema))

print("\n")