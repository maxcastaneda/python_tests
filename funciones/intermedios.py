from random import *

### Ejercicio 1
def lanzar_dados():
    dado1 = randint(1,7)
    dado2 = randint(1,7)
    return dado1, dado2

def evaluar_jugada(dado1, dado2):
    resultado = ""
    suma_dados = dado1 + dado2
    if suma_dados <= 6:
        resultado = f"La suma de tus dados es {suma_dados}. Lamentable"    
    elif suma_dados >= 10:
        resultado = f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"    
    else:
        resultado = f"x... {dado1} + {dado2} = {suma_dados}"

    return resultado

dado1, dado2 = lanzar_dados()
print(evaluar_jugada(dado1, dado2))

### Ejercicio 2
def reducir_lista(lista):
    lista_nueva = []
    for i in lista:
        if i not in lista_nueva:
            lista_nueva.append(i)
    lista_nueva.pop(lista_nueva.index(max(lista)))
    return lista_nueva

def promedio(lista):
    return sum(lista)/len(lista)

lista_numeros =  [1,2,15,7,2] 
lista_numeros = reducir_lista(lista_numeros)
print(promedio(lista_numeros))

### Ejercicio 3
def lanzar_moneda():
    return choice(["Cara", "Cruz"])

def probar_suerte(moneda, lista):
    if moneda == "Cara":
        print ("La lista se autodestruira")
        lista.clear()
    else:
        print ("La lista fue salvada")
    return lista

moneda = lanzar_moneda()
lista_numeros = [1,2,15,7,2]
probar_suerte(moneda, lista_numeros)

def contar_primos(numero):
    for i in range(2, numero+1):
        if i%1 == 0 and i%i == 0:
            print(i)
        else:
            continue
        
contar_primos(100)