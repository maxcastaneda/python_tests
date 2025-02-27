# Ejercicio 1
class Casa:
    def __init__(self, color, cantidad_pisos):
        self.color = color
        self.cantidad_pisos = cantidad_pisos
casa_blanca = Casa("blanco",4)

# Ejercicio 2
class Cubo:
    caras = 6
    def __init__(self, color):
        self.color = color
cubo_rojo = Cubo("rojo")

# Ejercicio 3
class Personaje:
    real=False
    def __init__(self, especie, magico, edad):
        self.especie =  especie
        self.magico = magico
        self.edad = edad
harry_potter = Personaje("Humano",True,17)

#Ejercicio 4
class Perro:
    def ladrar(self):
        print("Guau!")

#Ejercicio 5
class Mago:
    def lanzar_hechizo(self):
        print("¡Abracadabra!")
merlin = Mago()
merlin.lanzar_hechizo()

#Ejercicio 6
class Alarma:
    def __init__(self, cantidad_minutos):
        self.cantidad_minutos = cantidad_minutos

    def postergar(self, cantidad_minutos):
        print(f"La alarma ha sido pospuesta {self.cantidad_minutos} minutos")

#Ejercicio 7
class Mascota:
    @staticmethod
    def respirar():
        print ("Inhalar... Exhalar")

#Ejercicio 8
class Jugador:
    vivo = False
    @classmethod
    def revivir(cls):
        cls.vivo = True

#Ejercicio 9
class Personaje:
    valor=""
    def __init__(self, cantidad_flechas):
        self.cantidad_flechas = int(cantidad_flechas)
    def lanzar_flecha(self):
        self.cantidad_flechas -=1
    @classmethod
    def assign_valor(cls,valor):
        cls.valor=valor
    @classmethod
    def imprime_valor(cls):
        print(cls.valor)

p1 = Personaje(10)
p2 = Personaje(11)

p1.assign_valor("este")
p1.imprime_valor()
p2.imprime_valor()