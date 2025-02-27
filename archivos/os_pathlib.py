from pathlib import Path 
import os
from os import system

system('cls')

#Ejercicio 1 (carpeta de trabajo actual)
ruta_base = os.getcwd()
print(ruta_base)

#Ejecrcicio 1.1 (directorio "home" del usuario actual)
ruta_base = Path.home()
print(ruta_base)

#Ejercio 2
ruta = Path("Curso Python","Día 6","practicas_path.py")
print(ruta)

#Ejercicio 3
ruta = Path(Path.home(), "Curso Python","Día 6","practicas_path.py")
print(ruta)

