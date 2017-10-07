import pygame
import random

ALTO=400
ANCHO=600
ROJO=(255,0,0)
BLANCO=(255,255,255)
AZUL=(59,131,189)
VERDE=(0,255,0)
centro=[ANCHO/2,ALTO/2]

class Jugador(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(ROJO)
        self.rect=self.image.get_rect()
        self.var_x=0
        self.var_y=0
    def update(self):
        lp=pygame.mouse.get_pos()
        self.rect.x=lp[0]-30
        #self.rect.x+=self.var_x
        #self.rect.y+=self.var_y
        #if self.rect.x>=ANCHO-self.rect[2]:
        #    self.var_x=-6
        #if self.rect.x<=0:
        #    self.var_x=6
        if self.rect.y>=ALTO-self.rect[3]:
            self.var_y=-4
        if self.rect.y<=0:
            self.var_y=4
class Final(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(BLANCO)
        self.rect=self.image.get_rect()

class Bloque(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(VERDE)
        self.rect=self.image.get_rect()

class Rival(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(AZUL)
        self.rect=self.image.get_rect()
        self.var_x=2
        self.var_y=2
    def update(self):
        #self.rect.x+=self.var_x
        self.rect.y+=self.var_y
        if self.rect.x>=ANCHO-self.rect[2]:
            self.var_x=-2
        if self.rect.x<=0:
            self.var_x=2
        if self.rect.y>=ALTO-self.rect[3]-30:
            self.var_y=-2
        if self.rect.y<=0:
            self.var_y=2

class  Proyectil(pygame.sprite.Sprite):
    def __init__(self,an,al):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface([an,al])
        self.image.fill(VERDE)
        self.rect=self.image.get_rect()
        self.var_x=2
        self.var_y=-2
    def update(self):
        #self.rect.x+=self.var_x
        self.rect.y+=self.var_y
        if self.rect.x>=ANCHO-self.rect[2]:
            self.var_x=-2
        if self.rect.x<=0:
            self.var_x=2
        if self.rect.y>=ALTO-self.rect[3]-30:
            self.var_y=-2
        if self.rect.y<=0:
            self.var_y=2



if __name__=='__main__':
    pygame.init()
    pantalla=pygame.display.set_mode([ANCHO,ALTO])
    pantalla.fill(BLANCO)
    fuente=pygame.font.Font(None,36)
    jp=Jugador(70,10)
    bar=Final(600,40)
    bar1=Final(600,1)
    bola=Rival(10,10)
    tmp=0
    jugadores=pygame.sprite.Group()
    general=pygame.sprite.Group()
    balas=pygame.sprite.Group()
    general.add(bola)
    general.add(jp)
    general.add(bar)
    general.add(bar1)
    jugadores.add(jp)

    reloj=pygame.time.Clock()
    ptos=0
    pas=0
    riv=0
    vidas=0
    jp.rect.x=100
    jp.rect.y=340
    bar.rect.x=0
    bar.rect.y=360
    bar1.rect.x=0
    bar1.rect.y=0
    rivales=pygame.sprite.Group()
    bloques=pygame.sprite.Group()
    rivales.add(bola)
    #for i in range(6):
        #r=Bloque(40,20)
        #r.rect.x=random.randrange(10, ANCHO-20)
        #r.rect.y=random.randrange(0, 200)
        #general.add(r)
        #bloques.add(r)
    for i in range(1):
        r=Rival(5,5)
        r.rect.x=random.randrange(10, ANCHO-20)
        r.rect.y=random.randrange(-400, 0)
        rivales.add(r)
        general.add(r)
    general.draw(pantalla)
    pygame.display.flip()
    fin=False
    while not fin:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                fin=True
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_RIGHT:
                    jp.var_x=4
                if event.key==pygame.K_LEFT:
                    jp.var_x=-4
                #if event.key==pygame.K_UP:
                #    jp.var_y=-5
                #if event.key==pygame.K_DOWN:
                #    jp.var_y=5
                if event.key==pygame.K_SPACE:
                    #jp.var_x=0
                    b=Proyectil(10,10)
                    b.rect.x=jp.rect.x+40
                    b.rect.y=jp.rect.y
                    balas.add(b)
                    general.add(b)
                    #jp.var_y=0
        #ls_col=pygame.sprite.spritecollide(jp,rivales,True)
        lb_col=pygame.sprite.spritecollide(bar,rivales,True)
        lr_col=pygame.sprite.spritecollide(bola,bloques,True)
        lb_col=pygame.sprite.groupcollide(balas,rivales,True,True)
        lb_col=pygame.sprite.spritecollide(bar1,balas,True)
        lt_col=pygame.sprite.groupcollide(rivales,jugadores,False,True)
        for elemento in lb_col:
            vidas-=1
            pas+=1
        #for elemento in ls_col:
            #ptos+=1
            #pas+=1
            #elemento.var_y=-2
        for elemento in lr_col:
            ptos+=1
            pas+=1
            bola.var_y=-bola.var_y
            #print elemento
        if tmp==0:
            r=Rival(20,20)
            r.rect.x=random.randrange(10, ANCHO-20)
            r.rect.y=random.randrange(-400, 0)
            rivales.add(r)
            general.add(r)
            tmp=100
        else:
            tmp-=1
        general.update()
        pantalla.fill(BLANCO)
        general.draw(pantalla)
        pygame.display.flip()
        reloj.tick(60)