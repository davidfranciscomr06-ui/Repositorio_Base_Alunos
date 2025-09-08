import sys
import pygame
from random import randint 
from time import sleep

def reset_bola():
    bola.center = (LARGURA_TELA // 2,ALTURA_TELA // 2)
    barra_direita.y = (ALTURA_TELA - ALTURA_BARRA) // 2
    barra_esquerda.y = (ALTURA_TELA - ALTURA_BARRA) // 2

LARGURA_TELA, ALTURA_TELA = 800,600
FPS = 60
BRANCO = (255,255,255)
PRETO = (0,0,0)

LARGURA_BARRA, ALTURA_BARRA = 10,100
VELOCIDADE_BARRA = 15

TAMANHO_BOLA = 15
VELOCIDADE_BOLA_X = 7
VELOCIDADE_BOLA_Y = 7
pygame.init()
tela= pygame.display.set_mode((LARGURA_TELA,ALTURA_TELA))
pygame.display.set_caption(("pong turma1"))
clock = pygame.time.Clock()
temporizador = 0 

barra_esquerda = pygame.Rect(10, (ALTURA_TELA - ALTURA_BARRA) // 2, LARGURA_BARRA, ALTURA_BARRA)
barra_direita = pygame.Rect(LARGURA_TELA - 20, (ALTURA_TELA - ALTURA_BARRA) // 2, LARGURA_BARRA, ALTURA_BARRA)
bola = pygame.Rect((LARGURA_TELA - TAMANHO_BOLA) // 2, (ALTURA_TELA - TAMANHO_BOLA) // 2, TAMANHO_BOLA, TAMANHO_BOLA)

velocidade_esquerda = 0
velocidade_direita = 0

if randint(0,1) == 0:
        velocidade_bola_x = VELOCIDADE_BOLA_X
else:
    velocidade_bola_x = -VELOCIDADE_BOLA_X

if randint (0,1) == 0:
    velocidade_bola_y = VELOCIDADE_BOLA_Y
else:
    velocidade_bola_y = -VELOCIDADE_BOLA_Y

placar_esquerdo = 0
placar_direito = 0
placar_fonte = pygame.font.Font(None,36)



rodando = True 
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        if evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_w:
               velocidade_esquerda = -VELOCIDADE_BARRA
            if evento.key == pygame.K_s:
                velocidade_esquerda = VELOCIDADE_BARRA
            if evento.key == pygame.K_UP:
                velocidade_direita = -VELOCIDADE_BARRA
            if evento.key == pygame.K_DOWN:
              velocidade_direita = VELOCIDADE_BARRA
        if evento.type == pygame.KEYUP:
            if evento.key == pygame.K_w or evento.key == pygame.K_s:
                velocidade_esquerda = 0
            if evento.key == pygame.K_UP or  evento.key == pygame. K_DOWN:
                velocidade_direita = 0

    barra_esquerda.y += velocidade_esquerda
    barra_direita.y += velocidade_direita


    bola.x += velocidade_bola_x
    bola.y += velocidade_bola_y
    

    if bola.top <= 0 or bola.bottom >= ALTURA_TELA:
        velocidade_bola_y = - velocidade_bola_y 

    #colisao com as barra
    if bola.colliderect(barra_esquerda) or bola.colliderect(barra_direita):
        velocidade_bola_x = -velocidade_bola_x

    barra_esquerda.y =max(0, min(ALTURA_TELA - ALTURA_BARRA,barra_esquerda.y))
    barra_direita.y = max (0,min(ALTURA_TELA - ALTURA_BARRA,barra_direita.y))

    if bola.left <= 0:
        reset_bola()
        temporizador =1
        placar_direito += 1
        velocidade_bola_x = -velocidade_bola_x
    if bola.right >= LARGURA_TELA:
        reset_bola()
        temporizador = 1
        placar_esquerdo  += 1
        velocidade_bola_x = -velocidade_bola_x

    tela.fill(PRETO)
    pygame.draw.rect(tela,(30,144,255),barra_esquerda)
    pygame.draw.rect(tela,(178,34,34),barra_direita)
    pygame.draw.rect(tela, BRANCO,bola)
    pygame.draw.aaline(tela,BRANCO, (LARGURA_TELA // 2,0),(LARGURA_TELA // 2, ALTURA_TELA))
    
    texto_esquerdo = placar_fonte.render(str(placar_esquerdo),True,BRANCO)
    texto_direita = placar_fonte.render(str(placar_direito),True,BRANCO)
    tela.blit(texto_esquerdo,(LARGURA_TELA // 4 - texto_esquerdo.get_width() // 2,20))
    tela.blit(texto_direita,(3* LARGURA_TELA // 4 - texto_direita.get_width() // 2,20))
    pygame.display.flip()

    if temporizador == 1:
        sleep(2)
        temporizador = 0 

    clock.tick(FPS)

pygame.quit()