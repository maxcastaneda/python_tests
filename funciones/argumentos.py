## Ejercicio 1
def suma_cuadrados(*args):
    return sum([i**2 for i in args])

#Ejercicio 2
def suma_absolutos(*args):
    return sum([abs(i) for i in args])

#Ejercicio 3
def numeros_persona(*args):
    return f"{args[0]}, la suma de tus numeros es {sum( args[1:] )}"

print(suma_cuadrados(1,2,3,4,5))

print(suma_absolutos(-1,2,-3,4,-5))

print(numeros_persona("Juan", 1,2,3,4,5))

## Ejercicio 4
def cantidad_atributos(**kwargs):
    return len(kwargs)

## Ejercicio 5
def lista_atributos(**kwargs):
    return [i for i in kwargs.values()]

## Ejercicio 6
def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for key,val in kwargs.items():
        print(f"{key}: {val}")

print (cantidad_atributos(a=1, b=2, c=3, d=4, e=5))

print (lista_atributos(a=1, b=2, c=3, d=4, e=5))

describir_persona("María", color_ojos="azules", color_pelo="rubio")