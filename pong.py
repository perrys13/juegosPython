import pygame
pygame.init()

ventana=pygame.display.set_mode((800,800))
frames=pygame.time.Clock()

run= True

#colores
blanco=(255,255,255)
negro=(0,0,0)
#posicion jugador1
j1posx=0
j1posy=300
#posicion jugador2
j2posx=780
j2posy=300
#velocidad jugadores
j1vel=0
j2vel=0
#posicion pelota
pposx=400
pposy=400
#velocidad pelota
pvelx=3
pvely=3


while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        #control de velocidades
        if event.type == pygame.KEYDOWN:
            # Jugador 1
            if event.key == pygame.K_w:
                j1vel = -5
            if event.key == pygame.K_s:
                j1vel = 5

            # Jugador 2
            if event.key == pygame.K_UP:
                j2vel = -5
            if event.key == pygame.K_DOWN:
                j2vel = 5

        if event.type == pygame.KEYUP:
            # Jugador 1
            if event.key == pygame.K_w:
                j1vel = 0
            if event.key == pygame.K_s:
                j1vel = 0
            # Jugador 2
            if event.key == pygame.K_UP:
                j2vel = 0
            if event.key == pygame.K_DOWN:
                j2vel = 0


    #generar movimiento jugadores
    #verifico que los jugadores no se salgan de la pantalla
    if 0 < j1posy < 700:
        j1posy += j1vel
        j2posy += j2vel
    elif j1posy == 700:
        j1posy -= 5
    elif j1posy == 0:
        j1posy += 5

    #generar movimiento pelota
    pposx += pvelx
    pposy += pvely

    #si pelota sale de pantalla  por izq o derecha
    if pposx > 800 or pposx < 0:
        pposx=400
        pposy=400


    #si pelota toca techo o piso rebota
    if pposy > 800 or pposy<0:

        pvely*=-1



    ventana.fill(negro)
    jugador1=pygame.draw.rect(ventana,(blanco),(j1posx,j1posy,20,100))
    jugador2=pygame.draw.rect(ventana,(blanco),(j2posx,j2posy,20,100))
    pelota=pygame.draw.circle(ventana,blanco,(pposx,pposy),15)

    # si pelota toca jugador rebota
    if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
        pvelx *= -1

        
    frames.tick(500)
    pygame.display.flip()
pygame.quit()