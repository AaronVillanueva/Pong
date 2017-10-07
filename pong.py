# encoding: UTF-8
# Autor: Aaron Tonatiuh Villanueva Guzmán
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 800
lineas=ALTO//10
# Colores
principal = (255,255,255)  # R,G,B en el rango [0,255]
fondo=(0,0,0)

def rebotar():
    radio=20
    x= ANCHO//3
    y= ALTO//3
    derecha = True
    abajo = False
    marco=ALTO//10
    alturaRaqueta=ALTO//5
    anchoRaqueta=alturaRaqueta//4
    xRaqueta=0
    
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption('Pong Pygame Villanueva')
    #Cambiar visible a 0 una vez el mouse este implementado
    pygame.mouse.set_visible(1)
    reloj = pygame.time.Clock()

    #Fuente Pong!
    #pygame.font.init()
    fuente = pygame.font.Font(None, 100)
    puntajeA = 0
    puntajeB = 0
    termina = False
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

        ventana.fill(fondo)

        #Texto
        textoPong=fuente.render("Pong!",0,principal)
        posicionPong= textoPong.get_rect(center=(400,40))
        ventana.blit(textoPong,posicionPong)
        for cambio in range(0,ALTO,lineas):
            pygame.draw.rect(ventana,principal,(ANCHO//2,marco+cambio,10,30),0)

        #Puntajes
        if x<=0:
            puntajeA+=1
            x=600
            y=400

        textoPuntajeA=fuente.render(str(puntajeA),0,principal)
        posicionPuntajeA=textoPuntajeA.get_rect(center=(ANCHO//6, 40))
        ventana.blit(textoPuntajeA,posicionPuntajeA)
        textoPuntajeB=fuente.render(str(puntajeB),0,principal)
        posicionPuntajeB=textoPuntajeB.get_rect(center=(5*(ANCHO//6), 40))
        ventana.blit(textoPuntajeB,posicionPuntajeB)

        #Mouse
        nada, yRaqueta=pygame.mouse.get_pos()
        if yRaqueta>= ALTO-alturaRaqueta:
            yRaqueta=ALTO-alturaRaqueta
        elif yRaqueta<=0+marco:
            yRaqueta=marco

        #Dibujos
        pygame.draw.circle(ventana,principal,(x,y),radio, 0)
        pygame.draw.rect(ventana,principal,(xRaqueta,yRaqueta,anchoRaqueta,alturaRaqueta),0)
        pygame.draw.line(ventana, principal, (0,marco),(ANCHO,marco), 5)
        if derecha:
            x+=7
        else:
            x-=7
        if abajo:
            y+=7
        else:
            y-=7
        if x<(anchoRaqueta+radio) and (yRaqueta<y<(yRaqueta+alturaRaqueta+radio)):
            abajo= not abajo
            derecha= not derecha
        if x>=ANCHO-radio:
            derecha=not derecha
        if y>=ALTO-radio or y<=radio+marco:
            abajo=not abajo

        if puntajeA>=1:
            x=ALTO+100
            textoDerrota = fuente.render("Perdiste", 0, principal)
            posicionDerrota = textoPuntajeA.get_rect(center=(ANCHO // 8, ALTO//5))
            ventana.blit(textoDerrota, posicionDerrota)

        pygame.display.flip()   # Actualiza trazos
        reloj.tick(60)          # 40 fps

    pygame.quit()   # termina pygame


def main():
    rebotar()


main()
