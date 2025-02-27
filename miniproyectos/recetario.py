from colorama import init, Fore, Back, Style
from os import system
from pathlib import Path 

init(autoreset=True)
rutahome= Path("Recetas")


def leeropcion(mensaje, max):
    while True:
        opcion=input(Fore.BLUE + mensaje +  "[ ]\b\b")
        if len(opcion) != 1:
            print ("opcion no valida!")
            continue
        if not opcion.isdigit():
            print ("opcion no valida!")
            continue
        if int(opcion)>max:
            print ("opcion no valida!")
            continue
        break
    return opcion


def mostrar_menu():
    system('cls')
    total_recetas = [r for r in rutahome.rglob("*.txt")]
    print(Fore.WHITE + """
    ____  ___________________________    ____  ________ 
   / __ \/ ____/ ____/ ____/_  __/   |  / __ \/  _/ __ \\
  / /_/ / __/ / /   / __/   / / / /| | / /_/ // // / / /
 / _, _/ /___/ /___/ /___  / / / ___ |/ _, _// // /_/ / 
/_/ |_/_____/\____/_____/ /_/ /_/  |_/_/ |_/___/\____/     
    """)
    print ("Bienvenido al recetario mamalón")
    print (f"Tenemos un total de {len(total_recetas)} recetas")
    print (f"Las recetas estan guardadas en \"{rutahome}\" \n\n")
    print (Back.WHITE + Fore.RED + " [ 1 ] - " + Fore.BLACK + " leer receta          ")
    print (Back.WHITE + Fore.RED + " [ 2 ] - " + Fore.BLACK + " crear receta         ")
    print (Back.WHITE + Fore.RED + " [ 3 ] - " + Fore.BLACK + " crear categoria      ")
    print (Back.WHITE + Fore.RED + " [ 4 ] - " + Fore.BLACK + " eliminar receta      ")
    print (Back.WHITE + Fore.RED + " [ 5 ] - " + Fore.BLACK + " eliminar categoria   ")
    print (Back.WHITE + Fore.RED + " [ 6 ] - " + Fore.BLACK + " finalizar programa   ")

    print("\n")
    opcion = leeropcion("Selecciona una opción", 6) 
    return opcion


def mostrar_categorias():
    system('cls')
    subcarpetas = [f.name for f in rutahome.iterdir() if f.is_dir()]
    i = 1
    categorias = []
    for carpeta in subcarpetas:
        print (Back.WHITE + Fore.RED + f" [ {i} ] - " + Fore.BLACK + f" {carpeta} ")
        categorias.append(carpeta)
        i +=1
    print("\n")
    opcion = leeropcion("Selecciona una categoria ", i-1) 
    return categorias[int(opcion)-1]


def mostrar_recetas(categoria):
    system('cls')    
    ruta = Path(rutahome,categoria)
    archivos = [f.stem for f in ruta.rglob("*.txt") if f.is_file()]
    if len(archivos) == 0:
        input("No hay recetas en esta categoria! presione ENTER para continuar...")
        return 0
    i = 1
    recetas = []
    for archivo in archivos:
        print (Back.WHITE + Fore.RED + f" [ {i} ] - " + Fore.BLACK + f" {archivo} ")
        recetas.append(archivo)
        i +=1
    print("\n")
    opcion = leeropcion(Fore.WHITE + "Selecciona la receta ", i-1) 
    return recetas[int(opcion)-1]    


def abrir_receta(categoria,receta):
    archivo = Path(rutahome, categoria, receta+".txt")
    receta = open(archivo,"r",encoding="utf-8")
    system('cls')
    print(Fore.CYAN + receta.read())
    input(Fore.WHITE + "\n\nPresione ENTER para cerrar y volver al menu...")
    receta.close()


def leer_receta():    
    categoria = mostrar_categorias()
    receta = mostrar_recetas(categoria)
    if receta == 0:
        return    
    abrir_receta(categoria,receta)


def crear_receta():
    categoria = mostrar_categorias()
    system('cls')
    nombre_receta = input("Ingresa el nombnre de la receta: ")        
    lineas = []
    print("Ingresa el contenido de la receta a continuacion, preciona ENTER dos veces para terminar!")
    while True:
        linea = input()  # Leer una línea del usuario
        if linea == "":  # Si la línea está vacía, salir del bucle
            break
        lineas.append(linea)
    texto_completo = "\n".join(lineas)
    archivo=open(Path(rutahome,categoria,nombre_receta + ".txt"),"w")
    archivo.write(texto_completo)


def crear_categoria():
    system('cls')
    nombre_categoria = input("Ingresa el nombre de la neva categoria: ")        
    nueva_carpeta = Path(rutahome,nombre_categoria)
    nueva_carpeta.mkdir(parents=True, exist_ok=True)
    input ("La categoria ha sido creada, pesione ENTER para continuar...")


def eiliminar_receta():    
    categoria = mostrar_categorias()
    receta = mostrar_recetas(categoria)
    if receta == 0:
        return    
    archivo = Path(rutahome, categoria, receta+".txt")
    receta = open(archivo,"r",encoding="utf-8")
    system('cls')
    print(receta.read())
    confirmacion = ""
    receta.close()
    while not confirmacion.lower() in "sn" or not len(confirmacion) == 1:
        confirmacion = input(Fore.RED + "\n\nEsta receta se eliminara, confirmar?? (S/N)")
    if confirmacion == "s":
        archivo.unlink()
        input("La receta ha sido mandada a la goma con exito, presione ENTER para continuar ... ")
    else:
        input(Fore.WHITE + "se cancelo la eliminación, presione ENTER para continuar ... ")



def eliminar_categoria():    
    categoria = mostrar_categorias()
    ruta = Path(rutahome,categoria)
    archivos = [f for f in ruta.rglob("*.txt") if f.is_file()]
    system('cls')
    confirmacion = ""
    while not confirmacion.lower() in "sn" or not len(confirmacion) == 1:
        confirmacion = input(Fore.RED + f"\n\nHay {len(archivos)} recetas en esta categoria, todo se eliminara. confirmar?? (S/N)")
    if confirmacion == "s":
        for archivo in archivos:
            print(Fore.WHITE + f"Eliminando {archivo} ...")
            Path(archivo).unlink()
        ruta.rmdir()
        input("La categoria ha sido mandada a la goma con exito, presione ENTER para continuar ... ")
    else:
        input("se cancelo la eliminación, presione ENTER para continuar ... ")    


while True:
    opcion = mostrar_menu()
    match opcion:
        case "1":
            leer_receta()
        case "2":
            crear_receta()
        case "3":
            crear_categoria()
        case "4":
            eiliminar_receta()            
        case "5":
            eliminar_categoria()
        case "6": 
            print ("Hasta luego!")
            break