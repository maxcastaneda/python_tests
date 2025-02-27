serie="N-02"

#approach con if
if serie == "N-01":
    print("Samsung")
elif serie == "N-02":
    print("Nokia")
elif serie == "N-03":
    print("Motorola")
else:
    print ("No identificado")

#approach con match
match serie:
    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print ("No identificado")

cliente = { 'nombre':'juan', 'apellido' : 'fuentes' , 'peso' : 88, 'altura' : 1.80 }
pelicula = { 'titulo':'Titanic', 'ficha_tecnica': {'director' : 'James Cameron' , 'año' : 1997, 'duracion' : 195 } }
elementos =[cliente,pelicula,'libro']

for e in elementos:
    match e:
        case {'nombre':n, 'apellido':a, 'peso':p, 'altura':al}:
            print("es un cliente")
            print(f"cliente: {n} {a} pesa {p} y mide {al}")
        case {'titulo':t, 'ficha_tecnica': {'director':d, 'año':an, 'duracion':du}}:
            print("es una pelicula")
            print(f"pelicula: {t} dirigida por {d} en {an} con duracion de {du}")
        case _:
            print("que chingaos es esto!")