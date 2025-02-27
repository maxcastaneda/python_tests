from random import *

def mi_funcion(nombre):
    print(f"Hola {nombre}, soy una función")  

mi_funcion("Juan")
mi_funcion("Leana")
mi_funcion("Sheena")

def saludar():
    print ("¡Hola mundo!")

def potencia(base, exponente):
    return base ** exponente
print(potencia(2, 3))

def usd_a_eur(usd):
    return usd * 0.90
dolares = 100
usd_a_eur(dolares)
print(f"{dolares} USD son {usd_a_eur(dolares)} EUR")

def invertir_palabra(palabra):
    return palabra[::-1].upper()
palabra ="Python"
invertir_palabra(palabra)
print(invertir_palabra("Python"))

def todos_positivos(lista):
    for i in lista:
        if i<0:
            return False
    return True
print(todos_positivos([1,2,3,-4,5]))

def suma_menores(listsa):
    suma = 0
    for i in listsa:
        if i>0 and i<=100:
            suma += i
    return suma
lista_numeros =[1,2,3,10001,50]
print(suma_menores(lista_numeros))

def cantidad_pares(lista):
    qty=0
    for i in lista:
        if i%2==0:
            qty += 1
    return qty
print(cantidad_pares([1,2,3,4,5,6,7,8,9,10]))

