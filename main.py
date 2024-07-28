# ۱ - Import library
import pygame
from pygame.locals import *
import sys
import random

# ۲ - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))

# رنگ‌ها
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255 , 0 , 0)
YELLOW = (255 , 255 , 0)
GREEN = (0 , 128 , 0)
# تعریف فونت
font = pygame.font.Font(None, 36)

try:
    img1 = pygame.transform.scale(pygame.image.load('pictur/01.png') , [125 , 125])
    img1 = img1.convert()
    rect1 = img1.get_rect()
    rect1.topleft = (100 , 350)

    img2 = pygame.transform.scale(pygame.image.load("pictur/02.png") ,[125 , 125])
    img2 = img2.convert()
    rect2 = img2.get_rect()
    rect2.bottomright = (380 , 473)

    img3 = pygame.transform.scale(pygame.image.load("pictur/03.png") , [125 , 125])
    img3 = img3.convert()
    rect3 = img3.get_rect()
    rect3.center = (470, 410)
except pygame.error as e:
    print(f"Failed to load image: {e}")
    sys.exit(1)

def draw_button(screen, rect, color, textcolor, text):
    pygame.draw.rect(screen, color, rect)
    text_surface = font.render(text, True, textcolor)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)


def play_game(player1):
    game_list = ["rock", "paper", "scissor"]

    button_rect = pygame.Rect (50 , 180 , 160 , 50)
    draw_button (screen , button_rect , GREEN , WHITE , player1)

    
    computer = random.choice(game_list)
    button_rect = pygame.Rect (425 , 180 , 160 , 50)
    draw_button (screen , button_rect , GREEN , WHITE , computer)



    if player1 == computer:
        button_rect = pygame.Rect(230, 265, 180, 50)
        draw_button(screen, button_rect , RED , BLUE, "equal")
    elif player1 == "rock":
        if computer == "scissor":
            button_rect = pygame.Rect(230, 265, 180, 50)
            draw_button(screen, button_rect , RED , BLUE, "player wins")
        else :
            button_rect = pygame.Rect(230, 265, 180, 50)
            draw_button(screen, button_rect , RED , BLUE, "computer wins")
    elif player1 == "paper":
        if computer == "rock":
            button_rect = pygame.Rect(230, 265, 180, 50)
            draw_button(screen, button_rect , RED , BLUE, "player wins")
        else:
            button_rect = pygame.Rect(230, 265, 180, 50)
            draw_button(screen, button_rect , RED , BLUE, "computer wins")
    elif player1 == "scissor":
        if  computer == "paper":
            button_rect = pygame.Rect(230, 265, 180, 50)
            draw_button(screen, button_rect , RED , BLUE, "player wins")
        else:
            button_rect = pygame.Rect(230, 265, 180, 50)
            draw_button(screen, button_rect , RED , BLUE, "computer wins")
    else:
        button_rect = pygame.Rect(230, 265, 180 , 50)
        draw_button(screen, button_rect , RED , BLUE, "invalid input!")  
    pygame.display.flip()      
running = True  

screen.fill(WHITE)


#pygame.draw.rect(screen, BLUE, rect1, 1)
#pygame.draw.rect(screen, BLUE, rect2, 2)
#pygame.draw.rect(screen, BLUE, rect3, 3)

button_rect = pygame.Rect(220, 200, 200, 50)
draw_button(screen, button_rect , BLUE , YELLOW, "Play")


pygame.display.flip()


def draw_images():
    screen.blit(img1 , rect1)
    screen.blit(img2 , rect2)
    screen.blit(img3 , rect3)

playing = False
while running:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN:  
            if not playing:
                if button_rect.collidepoint(event.pos):
                    print("The play button was pressed")
                    screen.fill(WHITE)
                    draw_images()
                    button_rect = pygame.Rect(243, 265, 160, 50)
                    draw_button(screen, button_rect , RED , BLUE, "play")

                    button_rect = pygame.Rect(230, 265, 180 , 50)
                    draw_button(screen, button_rect , RED , BLUE ,"" )  

                    button_rect = pygame.Rect (50 , 180 , 160 , 50)
                    draw_button (screen , button_rect , GREEN , WHITE , "player")

                    button_rect = pygame.Rect (425 , 180 , 160 , 50)
                    draw_button (screen , button_rect , GREEN , WHITE , "computer")

                    button_rect = pygame.Rect(0 , 0 , 150 , 50)
                    draw_button(screen , button_rect , GREEN , BLUE ,"score")

                    button_rect = pygame.Rect(490 , 0 , 150 , 50)
                    draw_button (screen , button_rect , GREEN , BLUE , "score")

                    pygame.display.flip()
                    playing = True
            else:
                if rect1.collidepoint(event.pos):
                    play_game("rock")
                elif rect2.collidepoint(event.pos):
                    play_game("paper")
                elif rect3.collidepoint(event.pos):
                    play_game("scissor")