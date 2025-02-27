"""
Departamentos: Perfumeria, Farmacia, Cosmetica
"""
def sacar_turno(departamento):
    i=0    
    while True:
        i+=1
        yield f"Su turno es: {departamento[0].upper()}-{i}, Aguarde y sera atendido"


