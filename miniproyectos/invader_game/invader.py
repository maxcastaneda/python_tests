import pygame
import random
from pygame import mixer

# inicializar pygame
pygame.init()


#setear pantalla y mostrarla
pantalla = pygame.display.set_mode((800, 600))


# texto de puntaje
puntaje = 0
fuente = pygame.font.Font("Starjedi.ttf", 32)
texto_x = 10
texto_y = 10
def mostrar_puntaje(x, y):
    puntaje_texto = fuente.render("Score: " + str(puntaje), True, (255, 255, 255))
    pantalla.blit(puntaje_texto, (x, y))


# titulo e icono
pygame.display.set_caption("Invasion espacial")
icono = pygame.image.load("alien.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo800.png")


# agregar musica
mixer.music.load("MusicaFondo.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)


# navecita
navecita =pygame.image.load("astronave.png")
navecita_x = 400-32
navecita_y = 500
navecita_x_cambio = 0
def poner_navecita(x, y):
    pantalla.blit(navecita, (x, y))


# enemigos
total_enemigos = 10                 
velocidad_enemigos = 0.3
avance_enemigos = 20
class Enemigo:
    def __init__(self):
        self.ovni = pygame.image.load("ovni.png")
        self.x = random.randint(0, 800-64)
        self.y = random.randint(0, 200)
        self.x_cambio = velocidad_enemigos
        self.y_cambio = avance_enemigos 
    def poner_ovni(self, x, y):
            pantalla.blit(self.ovni, (x, y))

enemigos = []
for i in range(total_enemigos):
    enemigos.append(Enemigo())


# bala
class Bala:
    def __init__(self,x,y):
        self.bala = pygame.image.load("balas.png")
        self.x = x
        self.y = y
        self.x_cambio = 0
        self.y_cambio = -1.8
    def disparar_bala(self, x, y):
        pantalla.blit(self.bala, (x+16, y+10))

balas = []

# explosion
explotar = False
explotar_x = 0
explotar_y = 0
explotar_w = 64
explotar_h = 64
explotar_alpha = 255
def poner_explosion(x, y, w, h, a):
    explosion = pygame.image.load("explosion.png")
    explosion = pygame.transform.scale(explosion, (w, h))
    explosion.set_alpha(a)
    pantalla.blit(explosion, (x, y))


# detectar colisiones
def colision(ovni_x, ovni_y, bala_x, bala_y):
    distancia = ((ovni_x - bala_x)**2 + (ovni_y - bala_y)**2)**0.5
    if distancia < 27:
        return True
    else:
        return False


# texto final del juego
fuente2 = pygame.font.Font("METALORD.ttf", 84)
def texto_final():    
    texto_final = fuente2.render("MAMASTE OVER", True, (255, 255, 255))
    pantalla.blit(texto_final, (100, 200))


#loop del juego
explosioncount = 0
ejecutar = True
while ejecutar:

    # fondo
    pantalla.blit(fondo, (0, 0))

    # analizar eventos 
    for event in pygame.event.get():
        # cerrar programa
        if event.type == pygame.QUIT:
            ejecutar = False

        # pescar teclas
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                navecita_x_cambio = -0.5
            elif event.key == pygame.K_RIGHT:
                navecita_x_cambio = 0.5
            elif event.key == pygame.K_SPACE: 
                sonido_bala = mixer.Sound("disparo.mp3")
                sonido_bala.play()
                bala=Bala(navecita_x, 500)   
                balas.append(bala)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                navecita_x_cambio = 0

    # modificar ubicacion de la nave
    navecita_x += navecita_x_cambio
    if navecita_x <= 0:
        navecita_x = 0
    elif navecita_x >= 800-64:
        navecita_x = 800-64
    
    # modificar ubicacion del ovni
    for i in range(total_enemigos):

        # terminar el juego
        if enemigos[i].y >= 450:
            for j in range(total_enemigos):
                enemigos[j].y = 1000
            texto_final()
            break;

        if enemigos[i].x <= 0:
            enemigos[i].x_cambio = velocidad_enemigos
            enemigos[i].y += enemigos[i].y_cambio     
        elif enemigos[i].x >= 800-64:
            enemigos[i].x_cambio = velocidad_enemigos * -1
            enemigos[i].y += enemigos[i].y_cambio                 
        enemigos[i].x += enemigos[i].x_cambio

        # poner ovni
        enemigos[i].poner_ovni(enemigos[i].x, enemigos[i].y)

        # colisiones
        for b in balas:
            if colision(enemigos[i].x, enemigos[i].y, b.x, b.y):
                sonido_colision = mixer.Sound("Golpe.mp3")
                sonido_colision.play()
                puntaje += 20
                explotar=True
                explotar_x = enemigos[i].x
                explotar_y = enemigos[i].y
                enemigos[i].x = random.randint(0, 800-64)
                enemigos[i].y = random.randint(50, 100)
                balas.remove(b)
                #enemigos.remove(enemigos[i])
                #total_enemigos -= 1

    # poner navecita
    poner_navecita(navecita_x, navecita_y)

    # poner bala
    for b in balas:
        b.disparar_bala(b.x, b.y)
        b.y += b.y_cambio
        if b.y <= 0:
            balas.remove(b)


    if explotar:
        explotar_w+=0.2
        explotar_h+=0.2
        explotar_alpha-=2
        poner_explosion(explotar_x, explotar_y,explotar_w,explotar_h,explotar_alpha)
        explosioncount += 1
        if explosioncount > 200:
            explotar = False
            explosioncount = 0
            explotar_w = 64
            explotar_h = 64
            explotar_alpha = 255

    # mostrar puntaje
    mostrar_puntaje(texto_x, texto_y)

    # actualizar pantalla
    pygame.display.update()