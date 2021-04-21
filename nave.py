import pygame
import os
import random
import time

pygame.font.init()
pygame.init()
ANCHO,ALTO=800,600

reloj=pygame.time.Clock()
ventana=pygame.display.set_mode((ANCHO,ALTO))
pygame.display.set_caption("El juego de la nave wacho")


#cargar naves enemigas
nave_roja=pygame.image.load(os.path.join("resources","naveroja.png"))
nave_verde=pygame.image.load(os.path.join("resources","naveverde.png"))
nave_azul=pygame.image.load(os.path.join("resources","naveazul.png"))
#cargar jugador
nave_jugador=pygame.image.load(os.path.join("resources","jugador.png"))
#cargar lasers
laser_rojo=pygame.image.load(os.path.join("resources","laserrojo.png"))
laser_verde=pygame.image.load(os.path.join("resources","laserverde.png"))
laser_azul=pygame.image.load(os.path.join("resources","laserazul.png"))
laser_jugador=pygame.image.load(os.path.join("resources","laserjugador.png"))
#cargar fondo
fondo=pygame.transform.scale(pygame.image.load(os.path.join("resources","fondo.png")),(ANCHO,ALTO))

#CLASE NAVE
class Nave:
    def __init__(self,x,y,vida=100):
        self.x=x
        self.y=y
        self.vida=vida
        self.naveimg=None
        self.laserimg=None
        self.lasers=[]
        self.cd=0
    def draw(self,ventana):
        ventana.blit(self.naveimg,(self.x,self.y))
    def get_width(self):
        return self.naveimg.get_width()
    def get_height(self):
        return self.naveimg.get_height()



#CLASE JUGADOR
class Jugador(Nave):
    def __init__(self,x,y,vida=100):
        super().__init__(x,y,vida)
        self.naveimg=nave_jugador
        self.laserimg=laser_jugador
        self.mask=pygame.mask.from_surface(self.naveimg)
        self.vidamaxima=vida

class Enemigo(Nave):
    coloresdic={
                "rojo":(nave_roja,laser_rojo),"azul":(nave_azul,laser_azul),"verde":(nave_verde,laser_verde)
    }

    def __init__(self,x,y,color,vida=100):
        super().__init__(x,y,vida)
        self.naveimg,self.laserimg = self.coloresdic[color]
        self.mask=pygame.mask.from_surface(self.naveimg)
    def movimiento(self,vel):
        self.y +=vel








#FUNCION PRINCIPAL
def main():
    run=True
    FPS=60
    nivel=0
    vidas=5
    velocidad=5
    velocidadenemigos=1
    enemigos=[]
    oleada=5

    fuente=pygame.font.SysFont("comicsans",60)
    jugador=Jugador(400,300)

    def redraw_window():

        nivel_label=fuente.render(f"nivel: {nivel}",1,(255,255,255))
        vidas_label = fuente.render(f"vidas: {vidas}", 1, (255, 255, 255))

        ventana.blit(fondo, (0, 0))
        ventana.blit(nivel_label, (ANCHO - nivel_label.get_width() - 15,15))
        ventana.blit(vidas_label, (15, 15))
        for enemigo in enemigos:
            enemigo.draw(ventana)
        jugador.draw(ventana)


        pygame.display.update()







    while run:

        reloj.tick(FPS)

        #if len(enemigos) == 0:
            #nivel+=1
            #oleada+=5
            #for i in range(oleada):
                


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run=False

        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_UP] and jugador.y > 0 - 8:
            jugador.y-=velocidad
        if teclas[pygame.K_DOWN] and jugador.y < ALTO - jugador.get_height():
            jugador.y+=velocidad
        if teclas[pygame.K_LEFT] and jugador.x > -8:
            jugador.x-=velocidad
        if teclas[pygame.K_RIGHT] and jugador.x < ANCHO - jugador.get_width() +8:
            jugador.x+=velocidad

        redraw_window()

main()
