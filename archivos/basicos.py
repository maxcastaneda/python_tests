mi_archivo = open("prueba.txt")
print(mi_archivo.read()) 
mi_archivo.close()

mi_archivo = open("prueba.txt")
print(mi_archivo.readlines()[1])

#Ejercicio 1
archivo = open("mi_archivo.txt", "w")
archivo.write("Nuevo texto")
archivo.close()
archivo = open("mi_archivo.txt", "r")
print(archivo.read())

#Ejercicio 2
archivo = open("mi_archivo.txt", "a")
archivo.write("Nuevo inicio de sesión")
archivo.close()
archivo = open("mi_archivo.txt", "r")
print(archivo.read())

# Ejercicio 3
registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
archivo = open("registro.txt", "w")
archivo.writelines ([ i + "\t" for i in registro_ultima_sesion])
archivo.close()
archivo = open("registro.txt", "r")
print(archivo.read())

# Ejercicio 4
def abrir_leer(ruta):
    archivo = open(ruta,"r")
    return archivo.read()
# print(abrir_leer(input("ingrese la ruta del archivo:")))

# Ejercicio 5
def sobrescribr(ruta):
    archivo = open(ruta,"w")
    archivo.write("contenido eliminado")

# Ejercicio 6
def registro_error(ruta):
    archivo = open(ruta,"a")
    archivo.write("se ha registrado un error de ejecución")

ruta = input("ingrese la ruta del archivo:")
# sobrescribr(ruta)
registro_error(ruta)
print(abrir_leer(ruta))   