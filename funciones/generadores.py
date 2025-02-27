#Ejercicio 1
"""
Crea un generador (almacenado en la variable generador) que sea capaz de devolver una secuencia infinita de números, 
iniciando desde el 1, y entregando un número consecutivo superior cada vez que sea llamada mediante next.
Pista: Utiliza un loop while para realizar este ejercicio.
"""

def mi_generador():    
    i = 0
    while True:
        i+=1
        yield i 

generador = mi_generador()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

#Ejercicio 2
"""
Crea un generador (almacenado en la variable generador) que sea capaz de devolver de manera indefinida múltiplos de 7, 
iniciando desde el mismo 7, y que cada vez que sea llamado devuelva el siguiente múltiplo (7, 14, 21, 28...).
"""
def mi_generador2():    
    i = 0
    while True:
        i+=7
        yield i 

generador = mi_generador2()

print(next(generador))
print(next(generador))
print(next(generador))
print(next(generador))

#Ejercicio 3
"""
Crea un generador que reste una a una las vidas de un personaje de videojuego, y devuelva un mensaje cada vez que sea llamado:
"Te quedan 3 vidas"
"Te quedan 2 vidas"
"Te queda 1 vida"
"Game Over"
Almacena el generador en la variable perder_vida
"""

def mi_generador3():    
    yield "Te quedan 3 vidas"
    yield "Te quedan 2 vidas"
    yield "Te queda 1 vida"
    yield "Game Over"

perder_vida = mi_generador3()

print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))