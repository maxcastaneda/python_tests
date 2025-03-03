import os
import datetime
from os import system
import re 
import time

# buscar archivos
def getArchivos(carpeta):
    archivos = []
    rutas = []
    for root, _, files in os.walk(carpeta):
        for file in files:
            rutas.append(os.path.join(root, file))
            archivos.append(file)
            print(os.path.join(root, file))
    return rutas, archivos



inicio = time.time()
carpeta = "Mi_Gran_Directorio"
rutas, archivos = getArchivos(carpeta)

system('cls')
print("-" * 60)
print(f"Fecha de búsqueda: {datetime.datetime.today().strftime("%d/%m/%Y %H:%M:%S")}\n")
print("ARCHIVO\t\t\t\tNRO. SERIE")
print("-------\t\t\t\t----------")
total = 0
for archivo, ruta in zip(archivos, rutas):
    
    openfile = open(ruta, "r")
    texto = openfile.read()    
    
    patron = r"N\D{3}-\d{5}"
    busqueda = re.findall(patron, texto)
    for match in busqueda:
        print(f"{archivo}\t\t\t{match}")
        total += 1

    fin = time.time()

print("\n")
print(f"Numeros encontrados: {total}")
print(f"Duracion de la búsqueda: {round(fin-inicio)} segundos")
print("-" * 60)