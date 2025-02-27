# Ejercicio 1
"""
Implementa para la siguiente función suma(), un manejador de errores simple que ante cualquier error, imprima en pantalla el mensaje: "Error inesperado". 
En caso contrario, deberá limitarse a mostrar el resultado de la suma entre los dos números.
"""
def suma(num1,num2):
    try:        
        print(num1+num2)
    except:
        print ("Error Inesperado")

suma(1,"ddd")

# Ejercicio 2
"""
Implementa para la siguiente función cociente(), un manejador de errores:
    Ante un error de tipo (TypeError), debe imprimir en pantalla el mensaje: "Los argumentos a ingresar deben ser números"
    Si se generara una división por cero (error del tipo ZeroDivisionError), el mensaje mostrado debe ser: "El segundo argumento no debe ser cero"
"""
def cociente(num1,num2):
    try:    
        print(num1/num2)
    except TypeError:
        print("Los argumentos a ingresar deben ser números")
    except ZeroDivisionError:
        print("El segundo argumento no debe ser cero")

cociente(200,0)

# Ejercicio 3
"""
Implementa un manejador de errores dentro de la siguiente función, abrir_archivo():
    En caso de que el archivo que se intenta abrir no pueda ser hallado (FileNotFoundError), mostrar en pantalla el mensaje: "El archivo no fue encontrado"
    En caso de que otro tipo de error ocurra, mostrar el mensaje: "Error desconocido"
    Si no se produce ningún error, imprimir en pantalla: "Abriendo exitosamente"
    En todos los casos, al finalizar, imprimir: "Finalizando ejecución"
"""


def abrir_archivo(nombre_archivo):
    try:
        archivo = open(nombre_archivo)
    except FileNotFoundError:
        print("El archivo no fue encontrado")
    except:
        print("Error desconocido")
    else:
        print("Abriendo exitosamente")
    finally:
        print("Finalizando ejecución")