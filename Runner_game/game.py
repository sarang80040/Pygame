import pygame
import sys
import torch
import numpy
pygame.init()
pygame.display.set_caption("SaranGame")
screen = pygame.display.set_mode((800, 400))
clock =pygame.time.Clock() #for controlling framerate - fps
test_font=pygame.font.Font('Pixeltype.ttf',50)
test_surface=pygame.Surface((100,200))
test_surface.fill((255,100,200))
game_active=False
start_time=0
current_time=0
def display_score():
    global current_time,score_surface,score_rect
    current_time=pygame.time.get_ticks()-start_time
    score_surface=test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect=score_surface.get_rect(center=(400,50))
    screen.blit(score_surface,score_rect)

test_surface=pygame.image.load("Sky.png").convert()
ground_surface=pygame.image.load("ground.png").convert()

# score_surface=test_font.render("Hello Sar Game",False,(64,64,64))
# score_rect=score_surface.get_rect(center=(400,50))

snail_surface=pygame.image.load("snail1.png").convert_alpha()
snail_rect=snail_surface.get_rect(midbottom=(700,300))

player_surface=pygame.image.load("player_walk_1.png").convert_alpha()
player_rect=player_surface.get_rect(midbottom=(80,250))
player_gravity=0

player_stand=pygame.image.load("player_stand.png").convert_alpha()
player_stand=pygame.transform.rotozoom(player_stand,0,2) #image,degrees,scale
player_stand_rect=player_stand.get_rect(center=(400,200))

game_name=test_font.render("SarGame",False,(100,60,50))
game_name_rect=game_name.get_rect(center=(400,80))

game_message=test_font.render("Press space to run",False,(100,60,50))
game_message_rect=game_message.get_rect(center=(400,350))

maxscore=0
count=False
while True:
    #draw all our elements
    #update everything on the screen
    
    
    
  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if game_active:
            if event.type==pygame.MOUSEBUTTONDOWN and player_rect.bottom==300:
                if player_rect.collidepoint(event.pos):
                    player_gravity=-20

            if event.type==pygame.KEYDOWN and player_rect.bottom==300:
                player_gravity=-20
        else:
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                game_active=True
                snail_rect.left=700
                start_time=pygame.time.get_ticks()
                player_rect.midbottom=(80,0)
                player_gravity=0

    if game_active: 
        
        screen.blit(test_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        # pygame.draw.rect(screen,"#c0e8ec",score_rect)
        # pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
        #screen.blit(score_surface,score_rect)
        display_score()
        snail_rect.x-=6
        if snail_rect.right<-80:snail_rect.left=700
        screen.blit(snail_surface,snail_rect)

        player_gravity+=1
        player_rect.y+=player_gravity
        if player_rect.bottom>=300:player_rect.bottom=300
        screen.blit(player_surface,player_rect)

        if player_rect.colliderect(snail_rect):
            # pygame.quit()
            # sys.exit()
            game_active=False
            count=True
    
    else:
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        maxscore=max(maxscore,current_time)
        screen.blit(game_message,game_message_rect)
        if(count):
            score_message=test_font.render(f'Your score: {current_time} \tMax score: {maxscore}',False,(100,60,50))
            score_message_rect=score_message.get_rect(center=(400,30))
            screen.blit(score_message,score_message_rect)
        else : 
            screen.blit(game_name,game_name_rect)
   
        
    
    pygame.display.update()
    clock.tick(60)