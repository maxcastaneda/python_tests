import os
import shutil

#obtener el directorio actual
print(os.getcwd())

# listar archivos en el directorio actual
print(os.listdir())

#shutil.copy("archivo.txt","archivo_copia.txt")
#shutil.move("archivo.txt","c:\\")

for carpeta, subcarpeta, archivo in os.walk("c:\\Users\\maxca\\source\\repos\\python"):
    print(f"Estas en la carpeta: {carpeta}")
    print(f"Subcarpetas:")
    for sub in subcarpeta:
        print(f"\t{sub}")
    print(f"Archivos:")
    for ar in archivo:
        print(f"\t{ar}")

