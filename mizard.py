import pygame
from pygame.locals import *

pygame.font.init()
pygame.display.init()

img = pygame.image.load('up_run1.png')
img2 = pygame.image.load('up_run2.png')
img3 = pygame.image.load('up_run3.png')
left = pygame.image.load('forward_left_run1.png')
left2 = pygame.image.load('forward_left_run2.png')
left3 = pygame.image.load('forward_left_run3.png')
right = pygame.image.load('forward_right_run1.png')
right2 = pygame.image.load('forward_right_run2.png')
right3 = pygame.image.load('forward_right_run3.png')
down = pygame.image.load('up_down1.png')
down2 = pygame.image.load('up_down2.png')
down3 = pygame.image.load('up_down3.png')
icon = pygame.image.load('icon.png')

background = pygame.image.load(r'C:\Users\coden\Downloads\Counterspell Game\newbasemap.png')
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
anim = 1
anim_delay = 0

running = True
intro = True
strange = True
strange2 = True
moving = False

wall1 = pygame.Rect((0, 50, 50, 350))
wall2 = pygame.Rect((50, 50, 650, 50))
wall3 = pygame.Rect((750, 50, 50, 350))
wall4 = pygame.Rect((100, 150, 650, 50))
wall5 = pygame.Rect((50, 250, 650, 50))
wall6 = pygame.Rect((100, 350, 650, 50))

direction = "up"
player_pos = pygame.Vector2(50, 500)
level = 1

final_font = pygame.font.SysFont('Comic Sans MS', 30)
final_text = final_font.render("Congratulations!", True, (255, 255, 255))

title_font = pygame.font.SysFont('Comic Sans MS', 30)
title_text = title_font.render("Welcome to Mizard!", True, (255, 255, 255))

pygame.display.set_caption("Mizard")
pygame.display.set_icon(icon)

while running:
    if intro:
        screen.fill((0, 0, 0))
        if strange:
            screen.blit(title_text, (250, SCREEN_HEIGHT // 3))
            strange = False
        else:
            pygame.time.delay(2000)
            intro = False
    else:
        screen.blit(background, (0, 0))
        if direction == "right":
            if moving == True:
                if anim == 1:
                    screen.blit(right, (player_pos.x, player_pos.y))
                elif anim == 2:
                    screen.blit(right2, (player_pos.x, player_pos.y))
                elif anim == 3:
                    screen.blit(right3, (player_pos.x, player_pos.y))
            else:
                screen.blit(right, (player_pos.x, player_pos.y))
        elif direction == "left":
            if moving == True:
                if anim == 1:
                    screen.blit(left, (player_pos.x, player_pos.y))
                elif anim == 2:
                    screen.blit(left2, (player_pos.x, player_pos.y))
                elif anim == 3:
                    screen.blit(left3, (player_pos.x, player_pos.y))
            else:
                screen.blit(left, (player_pos.x, player_pos.y))
        elif direction == "up":
            if moving == True:
                if anim == 1:
                    screen.blit(img, (player_pos.x, player_pos.y))
                elif anim == 2:
                    screen.blit(img2, (player_pos.x, player_pos.y))
                elif anim == 3:
                    screen.blit(img3, (player_pos.x, player_pos.y))
            else:
                screen.blit(img, (player_pos.x, player_pos.y))
        elif direction == "down":
            if moving == True:
                if anim == 1:
                    screen.blit(down, (player_pos.x, player_pos.y))
                elif anim == 2:
                    screen.blit(down2, (player_pos.x, player_pos.y))
                elif anim == 3:
                    screen.blit(down3, (player_pos.x, player_pos.y))
            else:
                screen.blit(down, (player_pos.x, player_pos.y))
        
        anim_delay += 1
        if anim_delay == 5:
            anim_delay = 0
            anim += 1
            if anim > 3:
                anim = 1
        
        # Draw walls
        pygame.draw.rect(screen, (45, 30, 45), wall1)
        pygame.draw.rect(screen, (45, 30, 45), wall2)
        pygame.draw.rect(screen, (45, 30, 45), wall3)
        pygame.draw.rect(screen, (45, 30, 45), wall4)
        pygame.draw.rect(screen, (45, 30, 45), wall5)
        pygame.draw.rect(screen, (45, 30, 45), wall6)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                moving = True
            if event.type == pygame.KEYUP:
                moving = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_d]:  # Move right
            direction = "right"
            player_pos.x += level
            pygame.time.wait(level)
            if img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall1) or \
                    img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall2) or \
                    img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall3) or \
                    img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall4) or \
                    img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall5) or \
                    img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall6) or \
                    player_pos.x > 775 or player_pos.x < 0 or player_pos.y > 575 or player_pos.y < 0:
                player_pos.x -= 2
                running = False
        if keys[pygame.K_a]:
            direction = "left"
            player_pos.x -= level
            pygame.time.wait(level)
            if img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall1) or \
                    img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall2) or \
                    img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall3) or \
                    img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall4) or \
                    img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall5) or \
                    img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall6) or \
                    player_pos.x > 775 or player_pos.x < 0 or player_pos.y > 575 or player_pos.y < 0:
                player_pos.x += 2
                running = False
        if keys[pygame.K_w]:
            direction = "up"
            player_pos.y -= level
            pygame.time.wait(level)
            if img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall1) or \
                    img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall2) or \
                    img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall3) or \
                    img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall4) or \
                    img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall5) or \
                    img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall6) or \
                    player_pos.x > 775 or player_pos.x < 0 or player_pos.y > 575 or player_pos.y < 0:
                player_pos.y += 2
                running = False
        if keys[pygame.K_s]:
            direction = "down"
            player_pos.y += level
            pygame.time.wait(level)
            if img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall1) or \
                    img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall2) or \
                    img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall3) or \
                    img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall4) or \
                    img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall5) or \
                    img.get_rect(topleft=(player_pos.x, player_pos.y)).colliderect(wall6) or \
                    player_pos.x > 775 or player_pos.x < 0 or player_pos.y > 575 or player_pos.y < 0:
                player_pos.y -= 2
                running = False

        if player_pos.y <= 2:
            if level != 5:
                level += 1
                player_pos.y = 500
                print(level)
            else:
                screen.fill((0, 0, 0))
                if strange2:
                    screen.blit(final_text, (275, SCREEN_HEIGHT // 3))
                    strange2 = False
                else:
                    pygame.time.delay(2000)
                    running = False
    print(player_pos)
    pygame.display.update()

pygame.quit()