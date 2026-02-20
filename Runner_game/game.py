import pygame
import sys
import torch
import numpy
from random import randint
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
    global current_time
    current_time=pygame.time.get_ticks()-start_time
    score_surface=test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect=score_surface.get_rect(center=(400,50))
    screen.blit(score_surface,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x-=6
            
            if obstacle_rect.bottom==300:screen.blit(snail_surface,obstacle_rect)
            else:screen.blit(fly_surface,obstacle_rect)
        #obstacle_list=[obstacle for obstacle in obstacle_list if obstacle.x>-100]
            obstacle_list=[obstacle for obstacle in obstacle_list if obstacle.x>-60]
        return obstacle_list
    else:return []

def collisions(player,obstacles):
    if obstacle_rect_list:
            for obstacle_rect in obstacle_rect_list:
                if player_rect.colliderect(obstacle_rect):
                    count=True
                    return False
    return True     
              
def player_animation():
    #jump
    global player_surface,player_index
    if player_rect.bottom<300:
        player_surface=player_jump
    else:
        player_index+=0.1
        if(player_index>=len(player_walk)):player_index=0 #id index is greater than 1 reset it to 0
        player_surface=player_walk[int(player_index)]
    



jump_sound=pygame.mixer.Sound("mario_jump_sound.mp3")
bg_sound=pygame.mixer.Sound("mario.mp3")
 #play bg sound in loop


test_surface=pygame.image.load("Sky.png").convert()
ground_surface=pygame.image.load("ground.png").convert()

# score_surface=test_font.render("Hello Sar Game",False,(64,64,64))
# score_rect=score_surface.get_rect(center=(400,50))

snail_frame1=pygame.image.load("snail1.png").convert_alpha()
snail_frame2=pygame.image.load("snail2.png").convert_alpha()
snail_frame_index=0
snail_frames=[snail_frame1,snail_frame2]
snail_surface=snail_frames[snail_frame_index]
snail_rect=snail_surface.get_rect(midbottom=(700,300))

fly_frame1=pygame.image.load("Fly1.png").convert_alpha()
fly_frame2=pygame.image.load("Fly2.png").convert_alpha()
fly_frames=[fly_frame1,fly_frame2]
fly_frame_index=0
fly_surface=fly_frames[fly_frame_index]

obstacle_rect_list=[]

player_walk_1=pygame.image.load("player_walk_1.png").convert_alpha()
player_walk_2=pygame.image.load("player_walk_2.png").convert_alpha()
player_walk=[player_walk_1,player_walk_2]
player_index=0 #to select walk1 or walk2
player_jump=pygame.image.load("jump.png").convert_alpha()
player_surface=player_walk[player_index]
player_rect=player_surface.get_rect(midbottom=(80,250))
player_gravity=0

player_stand=pygame.image.load("player_stand.png").convert_alpha()
player_stand=pygame.transform.rotozoom(player_stand,0,2) #image,degrees,scale
player_stand_rect=player_stand.get_rect(center=(400,200))

game_name=test_font.render("SarGame",False,(100,60,50))
game_name_rect=game_name.get_rect(center=(400,80))

game_message=test_font.render("Press space to run",False,(100,60,50))
game_message_rect=game_message.get_rect(center=(400,350))

obstacle_timer=pygame.USEREVENT+1
pygame.time.set_timer(obstacle_timer,1000)

snail_animation_timer=pygame.USEREVENT+2
pygame.time.set_timer(snail_animation_timer,500)

fly_animation_timer=pygame.USEREVENT+3
pygame.time.set_timer(fly_animation_timer,10)

maxscore=0
count=False
loop=0
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
                jump_sound.play()

            if event.type==obstacle_timer:
                if(randint(0,2)):
                    obstacle_rect_list.append(snail_surface.get_rect(midbottom=(numpy.random.randint(900,1000),300)))
                else :
                    obstacle_rect_list.append(fly_surface.get_rect(midbottom=(numpy.random.randint(900,1000),100)))
            
            if event.type==snail_animation_timer:
                if snail_frame_index==0:snail_frame_index=1
                else:snail_frame_index=0
                snail_surface=snail_frames[snail_frame_index]
            
            if event.type==fly_animation_timer:
                if fly_frame_index==0:fly_frame_index=1
                else:fly_frame_index=0
                fly_surface=fly_frames[fly_frame_index]

        else:
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                game_active=True
                #snail_rect.left=700
                bg_sound.play(loops=-1) #play bg sound in loop
                start_time=pygame.time.get_ticks()
              

    if game_active: 
        
        screen.blit(test_surface,(0,0))
        screen.blit(ground_surface,(0,300))
        # pygame.draw.rect(screen,"#c0e8ec",score_rect)
        # pygame.draw.rect(screen,'#c0e8ec',score_rect,10)
        #screen.blit(score_surface,score_rect)
        display_score()
        # snail_rect.x-=6
        # if snail_rect.right<-80:snail_rect.left=700
        # screen.blit(snail_surface,snail_rect)

        #player
        player_gravity+=1
        player_rect.y+=player_gravity
        if player_rect.bottom>=300:player_rect.bottom=300
        player_animation()
        screen.blit(player_surface,player_rect)

        #obstacle_movement
        obstacle_rect_list=obstacle_movement(obstacle_rect_list)


        # if player_rect.colliderect(snail_rect):
        #     # pygame.quit()
        #     # sys.exit()
        #     game_active=False
        #     count=True

        game_active=collisions(player_rect,obstacle_rect_list)
        
    
    else:
        bg_sound.stop()
        obstacle_rect_list.clear()
        player_rect.midbottom=(80,0)
        player_gravity=0
        screen.fill((94,129,162))
        screen.blit(player_stand,player_stand_rect)
        maxscore=max(maxscore,current_time)
        screen.blit(game_message,game_message_rect)
        if(count):
            score_message=test_font.render(f'Your score: {current_time} ',False,(100,60,50))
            score_message_rect=score_message.get_rect(center=(400,30))
            screen.blit(score_message,score_message_rect)
        else : 
            screen.blit(game_name,game_name_rect)
   
        
    
    pygame.display.update()
    clock.tick(60)