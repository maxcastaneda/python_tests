# entendiendo el uso de subfunciones y funciones como objetos...
def cambiar_letras(tipo):

    def mayuscula(texto):
        print(texto.upper())

    def minuscula(texto):
        print(texto.lower())

    if tipo == "may":
        return mayuscula
    elif tipo == "min":
        return minuscula

operacion = cambiar_letras("may")

operacion("palabra")

# ahora ejemplo los decoradores:
def decorar_saludo(funcion):
    def otra_funcion(*args):
        print('hola')
        funcion(*args)
        print('adios')
    return(otra_funcion)

def medir_tiempo(funcion):
    def wrapper(*args):
        import time
        inicio = time.time()
        funcion(*args)
        fin = time.time()
        print(f"Tiempo de ejecucion: {fin-inicio}")
    return wrapper

@decorar_saludo
@medir_tiempo
def mayusculas(texto):
    print(texto.upper())

@decorar_saludo 
@medir_tiempo
def minusculas(texto):
    print(texto.lower())

mayusculas("Python")

