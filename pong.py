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
    xEnemigo=800-anchoRaqueta
    yEnemigo=400
    velocidad=5
    modificadorVelocidad=1


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
                puntajeB+=1
                x=600
                y=400
            if x>800:
                puntajeA+=1
                x=200
                y=400

            #Texto puntajes
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

            #Pseudo Inteligencia Enemiga


            #Dibujos
            pygame.draw.circle(ventana,principal,(x,y),radio, 0)
            pygame.draw.rect(ventana,principal,(xRaqueta,yRaqueta,anchoRaqueta,alturaRaqueta),0)
            pygame.draw.line(ventana, principal, (0,marco),(anchoVentana,marco), 5)
            pygame.draw.rect(ventana, principal, (xEnemigo, yEnemigo, anchoRaqueta, alturaRaqueta), 0)

            #Comportamiento pelota
            if derecha:
                x+=velocidad*modificadorVelocidad
            else:
                x-=velocidad*modificadorVelocidad
            if abajo:
                y+=velocidad*modificadorVelocidad
            else:
                y-=velocidad*modificadorVelocidad

            #Pega con la raqueta del jugador
            if x<(anchoRaqueta+radio) and (yRaqueta<y<(yRaqueta+alturaRaqueta+radio)):
                abajo= not abajo
                derecha= not derecha
            #Pega con el enemigo PENDIENTE
            if x>=anchoVentana-radio:
                derecha=not derecha
            #Pega con el techo o el suelo
            if y>=altoVentana-radio or y<=radio+marco:
                abajo=not abajo

            #Modificador de velocidad
            if x<(anchoRaqueta+radio) and (yRaqueta<y<(yRaqueta+(alturaRaqueta//2)+radio)):
                modificadorVelocidad=5

            #Puntaje Maximo
            if puntajeB>=5 or puntajeA>=5:
                jugando=False

        #Juego termina y se determina un ganador
        else:
            if puntajeB>=5:
                textoDerrota = fuente.render("Perdiste", 0, principal)
                posicionDerrota = textoPuntajeB.get_rect(center=(anchoVentana // 8, altoVentana//5))
                ventana.blit(textoDerrota, posicionDerrota)
            elif puntajeA>=5:
                textoVictoria= fuente.render("Ganaste",0,principal)
                posicionVictoria=textoPuntajeA.get_rect(center=(anchoVentana//8, altoVentana//5))
                ventana.blit(textoVictoria,posicionVictoria)

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()


def main():
    rebotar()


main()
