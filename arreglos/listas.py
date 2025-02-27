# declarar listas
mi_lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
otra_lista = ['hola',55,6.1]

print(type(mi_lista))
resultado = len(mi_lista)
print(resultado)
print(mi_lista[0:2])

# sumara listas
mi_lista2 = ['h', 'o', 'l', 'a']
print(mi_lista + mi_lista2)

# las listas no son inmutables como los strings
# y sus elementos se puede editar
mi_lista[0] = 'z'
print(mi_lista)

# append permite agregar elementos a la lista
mi_lista.append('x')
print(mi_lista)

# pop permite eliminar elementos de la lista
mi_lista.pop()
mi_lista.pop(0)
eliminado = mi_lista.pop(0)
print(mi_lista)
print(eliminado)

# pora ordenar las listas:
mi_lista2.sort()
print(mi_lista2)

# para inverir el orde de una lista se usa reverse
mi_lista2.reverse()
print(mi_lista2)

#funcion zip
capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
for capital, pais in zip(capitales, paises):
    print(f"La capital de {pais} es {capital}")

espanol = ["uno", "dos", "tres", "cuatro", "cinco"]
portuges = ["um", "dois", "tres", "quatro", "cinco"]
ingles = ["one", "two", "three", "four", "five"]

numeros = list(zip(espanol, portuges, ingles))
print(numeros)

#maximos y minimos
lista_numeros = [44542247/2, 21310/5, 2134747*33, 44556475, 121676, 6654067, 353254, 123134, 55**12, 611**5]
valor_maximo = max(lista_numeros)

#compresion de listas
palabra = "Python"
lista = [letra for letra in palabra]
print (lista)
lista2 = [n for n in range(0,21,2) if n * 2 > 10]
print (lista2)
lista2 = [n if n * 2 > 19 else 'no' for n in range(0,21,2) if n * 2 > 10]
print (lista2)
pies=[10,20,30,50,50]
metros = [n*3.281 for n in pies]
print (metros)