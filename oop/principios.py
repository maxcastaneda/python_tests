#HERENCIA

#Ejercicio 1
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

class Alumno(Persona):
    pass

#Ejercicio 2
class Mascota:
    def __init__(self, nombre, edad, cantidad_patas):
        self.nombre = nombre
        self.edad = edad
        self.cantidad_patas = cantidad_patas

class Perro(Mascota):
    pass

#Ejercicio 3
class Vehiculo:
    def acelerar(self):
        pass
    def frenar(self):
        pass 

class Automovil(Vehiculo):
    pass 

#Ejercicio 4
"""
Si la clase Hija ha heredado de su padre la forma de reir, y de su madre la vocación, y hoy tienen el mismo trabajo en la Fiscalía, crea la herencia múltiple que le permita a esta clase heredar correctamente de Padre y Madre.
Completa el código suministrado a continuación para lograrlo.
"""
class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")
        
class Hija(Madre,Padre):
    pass

#Ejercicio 5
"""
Crea una clase Ornitorrinco que herede de otras clases: Vertebrado, Pez, Reptil, Ave y Mamifero, tal que "construyas" un animal que tiene los siguientes métodos y atributos:
- poner_huevos()
- tiene_pico = True
- vertebrado = True
- venenoso = True
- nadar()
- caminar()
- amamantar()
"""
class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Mamifero, Pez, Reptil, Ave):
    pass

#Ejercicio 6
"""
Un hijo ha heredado de su padre todas sus características, sin embargo, tienen diferentes hobbies. Logra que la clase Hijo herede de Padre todos sus métodos y atributos, 
sobreescribiendo el método hobby() para que se devuelva[1]: "Juego videojuegos en mi tiempo libre"
[1]: asegúrate de utilizar return seguido de una cadena de texto
"""
class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"
    def reir(self):
        return "Jajaja"
    def hobby(self):
        return "Pinto madera en mi tiempo libre"
    def caminar(self):
        return "Caminando con pasos largos y rápidos"
        
class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"
    
#POLIMORFISMO
# Ejercicio 1
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)

for objeto in [palabra, lista, tupla]:
    print(len(objeto))

#Ejercicio 2
class Mago():
    def atacar(self):
        print("Ataque mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

arquero = Arquero()
mago = Mago()
samurai = Samurai()

for personaje in [arquero, mago, samurai]:
    personaje.atacar()

# Ejercicio 3
class Mago():
    def defender(self):
        print("Escudo mágico")

class Arquero():
    def defender(self):
        print("Esconderse")

class Samurai():
    def defender(self):
        print("Bloqueo")

def personaje_defender(personaje):
    personaje.defender()

mago=Mago()
personaje_defender(mago)