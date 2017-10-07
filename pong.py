# encoding: UTF-8
# Autor: Aaron Tonatiuh Villanueva Guzmán
# Muestra cómo utilizar pygame para escribir programas que dibujan en la pantalla

import pygame

# Dimensiones de la pantalla
anchoVentana = 800
altoVentana = 800
lineas=altoVentana//10
# Colores
principal = (255,255,255)  # R,G,B en el rango [0,255]
fondo=(0,0,0)

def rebotar():
    radio=20
    x= anchoVentana//3
    y= altoVentana//3
    derecha = True
    abajo = False
    marco=altoVentana//10
    alturaRaqueta=altoVentana//5
    anchoRaqueta=alturaRaqueta//4
    xRaqueta=0
    
    pygame.init()
    ventana = pygame.display.set_mode((anchoVentana, altoVentana))
    pygame.display.set_caption('Pong Pygame Villanueva')
    #Cambiar visible a 0 una vez el mouse este implementado
    pygame.mouse.set_visible(1)
    reloj = pygame.time.Clock()
    jugando=True
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
        if jugando==True:
            #Texto
            textoPong=fuente.render("Pong!",0,principal)
            posicionPong= textoPong.get_rect(center=(400,40))
            ventana.blit(textoPong,posicionPong)
            for cambio in range(0,altoVentana,lineas):
                pygame.draw.rect(ventana,principal,(anchoVentana//2,marco+cambio,10,30),0)

            #Puntajes
            if x<=0:
                puntajeA+=1
                x=600
                y=400

            textoPuntajeA=fuente.render(str(puntajeA),0,principal)
            posicionPuntajeA=textoPuntajeA.get_rect(center=(anchoVentana//6, 40))
            ventana.blit(textoPuntajeA,posicionPuntajeA)
            textoPuntajeB=fuente.render(str(puntajeB),0,principal)
            posicionPuntajeB=textoPuntajeB.get_rect(center=(5*(anchoVentana//6), 40))
            ventana.blit(textoPuntajeB,posicionPuntajeB)

            #Mouse
            nada, yRaqueta=pygame.mouse.get_pos()
            if yRaqueta>= altoVentana-alturaRaqueta:
                yRaqueta=altoVentana-alturaRaqueta
            elif yRaqueta<=0+marco:
                yRaqueta=marco

            #Dibujos
            pygame.draw.circle(ventana,principal,(x,y),radio, 0)
            pygame.draw.rect(ventana,principal,(xRaqueta,yRaqueta,anchoRaqueta,alturaRaqueta),0)
            pygame.draw.line(ventana, principal, (0,marco),(anchoVentana,marco), 5)
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
            if x>=anchoVentana-radio:
                derecha=not derecha
            if y>=altoVentana-radio or y<=radio+marco:
                abajo=not abajo

            if puntajeA>=5:
                jugando=False

        #Pantalla derrota
        else:
            textoDerrota = fuente.render("Perdiste", 0, principal)
            posicionDerrota = textoPuntajeA.get_rect(center=(anchoVentana // 8, altoVentana//5))
            ventana.blit(textoDerrota, posicionDerrota)

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()


def main():
    rebotar()


main()
