from numeros import *

farmacia = sacar_turno("Farmacia")
perfumeria = sacar_turno("Perfumeria")
cosmetica = sacar_turno("Cosmetica")

while True:
    print ("""
Seleccione el departamento:
[1] Farmacia
[2] Perfumeria
[3] Cosmetica
[4] Salir
    """)
    opcion = int(input ("Seleccion: "))
    match opcion:
        case 1 :
            turno = next(farmacia)
        case 2 :
            turno = next(perfumeria)
        case 3 :
            turno = next(cosmetica)
        case 4 :
            break
    print(turno)
