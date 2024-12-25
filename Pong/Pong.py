#LIBRERIE
import pygame
import random
import time
import math

#Inizializzazioni di PyGame
pygame.init()
pygame.font.init()

#Gestione finestra
GAME_RES = WINDOW_WIDTH, WINDOW_HEIGHT = 640, 480
GAME_TITLE = "Pong"
BG_COLOR = (0, 0, 0)

#Gestione velocità del gioco
FPS = 144
dt = 1000 / FPS / 1000
window = pygame.display.set_mode(GAME_RES, pygame.HWACCEL|pygame.HWSURFACE|pygame.DOUBLEBUF)
pygame.display.set_caption(GAME_TITLE)
clock = pygame.time.Clock()

#Gestione testi
player_score_font = pygame.font.SysFont('Comic Sans MS', 64)
enemy_score_font = pygame.font.SysFont('Comic Sans MS', 64)
player_score_value = 0
enemy_score_value = 0

#Gestione immagini
player_img = pygame.image.load("assets/bricks/paddle1_2p.png")
enemy_img = pygame.image.load("assets/bricks/paddle2_2p.png")
ball_img = pygame.image.load("assets/ball/ball.png")
###Proporzione immagini
player_img = pygame.transform.scale(player_img, (16, 64))
enemy_img = pygame.transform.scale(enemy_img, (16, 64))
ball_img = pygame.transform.scale(ball_img, (16, 16))
###Coordinate associate alle immagini (diventano sprite)
player_rect = player_img.get_rect(center=(32, 32))
enemy_rect = enemy_img.get_rect(center=(32, 32))
ball_rect = ball_img.get_rect(center=(32, 32))
###Posizionamento sprite
player_rect.x = 0
player_rect.y = (WINDOW_HEIGHT // 2) - 32
enemy_rect.x = WINDOW_WIDTH-16
enemy_rect.y = (WINDOW_HEIGHT // 2) - 32
ball_rect.x = WINDOW_WIDTH // 2
ball_rect.y = WINDOW_HEIGHT // 2
ball_direction = random.randint(1, 4)
###Velocità di spostamento sprite
player_movespeed = 200 * dt
enemy_movespeed = 200 * dt
ball_movespeed = 200 * dt

#Inizializzazione variabili utili al funzionamento del gioco
loops = 1



#Gestione chiusura del gioco
game_ended = False
while not game_ended:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_ended = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game_ended = True
    
    #COMANDI
    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_w]:
        player_rect.y -= player_movespeed
    elif keys_pressed[pygame.K_s]:
        player_rect.y += player_movespeed
    if keys_pressed[pygame.K_UP]:
        enemy_rect.y -= enemy_movespeed
    elif keys_pressed[pygame.K_DOWN]:
        enemy_rect.y += enemy_movespeed
    
    # Controllo che le coordinate non escano dallo schermo
    if player_rect.y < 0:
        player_rect.y = 0
    if player_rect.y > WINDOW_HEIGHT - player_rect.height:
        player_rect.y = WINDOW_HEIGHT - player_rect.height
    if enemy_rect.y < 0:
        enemy_rect.y = 0
    if enemy_rect.y > WINDOW_HEIGHT - enemy_rect.height:
        enemy_rect.y = WINDOW_HEIGHT - enemy_rect.height
    if ball_rect.y < 0:
        if ball_direction == 1:
            ball_direction = 4
        if ball_direction == 2:
            ball_direction = 3
    if ball_rect.y > WINDOW_HEIGHT - ball_rect.height:
        if ball_direction == 4:
            ball_direction = 1
        if ball_direction == 3:
            ball_direction = 2
    
    #Preset direzionamento palla
    if ball_direction == 1:
        ball_rect.x += 1
        ball_rect.y -= 1
    if ball_direction == 2:
        ball_rect.x -= 1
        ball_rect.y -= 1
    if ball_direction == 3:
        ball_rect.x -= 1
        ball_rect.y += 1
    if ball_direction == 4:
        ball_rect.x += 1
        ball_rect.y += 1
        
    #Quando la palla esce dai bordi verticali
    if ball_rect.x < 0:
        ball_rect.x = WINDOW_WIDTH // 2
        ball_rect.y = WINDOW_HEIGHT // 2
        ball_direction = random.randint(1, 4)
        enemy_score_value += 1
    if ball_rect.x > WINDOW_WIDTH:
        ball_rect.x = WINDOW_WIDTH // 2
        ball_rect.y = WINDOW_HEIGHT // 2
        ball_direction = random.randint(1, 4)
        player_score_value += 1
        
    #Collisioni Racchetta-Palla
    if player_rect.colliderect(ball_rect):
        if ball_direction == 3:
            ball_direction = 4
        if ball_direction == 2:
            ball_direction = 1
    if enemy_rect.colliderect(ball_rect):
        if ball_direction == 4:
            ball_direction = 3
        if ball_direction == 1:
            ball_direction = 2
    
        
                
    # Update game logic
    loops += 1
     
    # Display draw and update
    pygame.Surface.fill(window, BG_COLOR)
    window.blit(player_img, (math.ceil(player_rect.x), math.ceil(player_rect.y)))
    window.blit(enemy_img, (math.ceil(enemy_rect.x), math.ceil(enemy_rect.y)))
    window.blit(ball_img, (math.ceil(ball_rect.x), math.ceil(ball_rect.y)))
    player_score = player_score_font.render(str(player_score_value), True, (255, 255, 255))
    enemy_score = enemy_score_font.render(str(enemy_score_value), True, (255, 255, 255))
    window.blit(player_score, (32, 0))
    window.blit(enemy_score, (WINDOW_WIDTH-64, 0))
    pygame.display.update()
    dt = clock.tick(FPS)
    dt /= 1000
    
pygame.quit()
exit(0)
                
