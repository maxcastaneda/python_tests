import pygame
import random

# inicializar pygame
pygame.init()


#setear pantalla y mostrarla
pantalla = pygame.display.set_mode((800, 600))


# titulo e icono
pygame.display.set_caption("Invasion espacial")
icono = pygame.image.load("alien.png")
pygame.display.set_icon(icono)
fondo = pygame.image.load("fondo800.png")


# navecita
navecita =pygame.image.load("astronave.png")
navecita_x = 400-32
navecita_y = 500
navecita_x_cambio = 0
def poner_navecita(x, y):
    pantalla.blit(navecita, (x, y))


# enemigo
ovni = pygame.image.load("ovni.png")
ovni_x = random.randint(0, 800-64)
ovni_y = random.randint(50, 100)
ovni_x_cambio = 0.2
ovni_y_cambio = 10
def poner_ovni(x, y):
    pantalla.blit(ovni, (x, y))


# bala
bala = pygame.image.load("balas.png")
bala_x = 0
bala_y = 500
bala_x_cambio = 0
bala_y_cambio = -1.5
bala_visible = False
def disparar_bala(x, y):
    pantalla.blit(bala, (x+16, y+10))


# explosion
explosion = pygame.image.load("explosion.png")
explotar = False
def poner_explosion(x, y):
    pantalla.blit(explosion, (x, y))


# detectar colisiones
def colision(ovni_x, ovni_y, bala_x, bala_y):
    distancia = ((ovni_x - bala_x)**2 + (ovni_y - bala_y)**2)**0.5
    if distancia < 27:
        return True
    else:
        return False


#loop del juego
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
                if not bala_visible:
                    bala_visible = True
                    bala_x = navecita_x
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
    if ovni_x <= 0:
        ovni_x_cambio = 0.2  
        ovni_y += ovni_y_cambio     
    elif ovni_x >= 800-64:
        ovni_x_cambio = -0.2 
        ovni_y += ovni_y_cambio                 
    ovni_x += ovni_x_cambio

    # poner navecita
    poner_navecita(navecita_x, navecita_y)

    # poner ovni
    poner_ovni(ovni_x, ovni_y)

    # poner bala
    if bala_visible:
        disparar_bala(bala_x, bala_y)
        bala_y += bala_y_cambio
        if bala_y <= 0:
            bala_y = 500
            bala_visible = False

    #colision
    if colision(ovni_x, ovni_y, bala_x, bala_y):
        explotar=True
        ovni_x = random.randint(0, 800-64)
        ovni_y = random.randint(50, 100)
        bala_y = 500
        bala_visible = False

    if explotar:
        poner_explosion(ovni_x, ovni_y)

    # actualizar pantalla
    pygame.display.update()