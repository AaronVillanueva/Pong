# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 400
# Colores
principal = (255,255,255)  # R,G,B en el rango [0,255]
VERDE_BANDERA = (0, 122, 0)
ROJO = (255, 0, 0)
fondo=(0,0,0)

def rebotar():
    radio=20
    x= ANCHO//2
    y= ALTO//2
    derecha = True
    abajo = False

    alturaRaqueta=ALTO//5
    anchoRaqueta=alturaRaqueta//4
    xRaqueta=0
    yRaqueta=ALTO//2 + alturaRaqueta//2
    
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(fondo)
        # Dibujar, aquí haces todos los trazos que requieras
        pygame.draw.circle(ventana,principal,(x,y),radio, 0)
        pygame.draw.rect(ventana,principal,(xRaqueta,yRaqueta,anchoRaqueta,alturaRaqueta),0)
        for cambio in range(0,800,100):
            pygame.draw.rect(ventana,BLANCO,(ANCHO//2,0+cambio,10,30),0)
        posRaqueta=xRaqueta
        if derecha:
            x+=7
        else:
            x-=7
        if abajo:
            y+=7
        else:
            y-=7
        if x>=ANCHO-radio:
            derecha=not derecha
        if y>=ALTO-radio or y<=radio:
            abajo=not abajo


        pygame.display.flip()   # Actualiza trazos
        reloj.tick(60)          # 40 fps

    pygame.quit()   # termina pygame


def main():
    rebotar()


main()
