# ۱ - Import library
import pygame
from pygame.locals import *
import sys


# ۲ - Initialize the game
pygame.init()
width, height = 640, 480
screen=pygame.display.set_mode((width, height))

# رنگ‌ها
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)


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

def draw_button(screen, rect, text):
    pygame.draw.rect(screen, BLUE, rect)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)
    
    

button_rect = pygame.Rect(220, 200, 200, 50)
running = True  

# ۴ - keep looping through
while running:
# ۵ - clear the screen before drawing it again
    screen.fill(WHITE)
    screen.blit(img1 , rect1)
    screen.blit(img2 , rect2)
    screen.blit(img3 , rect3)

# ۶ - draw the screen elements
#screen.blit(player, (100,100))
    draw_button(screen, button_rect, "Play")
# ۷ - update the screen
    pygame.display.flip()
# ۸ - loop through the events
    for event in pygame.event.get():
    # check if the event is the X button 
        if event.type==pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:  
            if button_rect.collidepoint(event.pos):
                print("The button was pressed")


        # if it is quit the game
pygame.quit() 
sys.exit(0)


#قوانین بازی
import random

game_list = ["rock", "paper", "scissor"]


player1 = input("Enter your decision: ")


player2 = random.choice(game_list)
print(f"camputer choice: {player2}")

if player1 == player2:
    print ("equal")
elif player1 == "rock":
    if player2 == "scissor":
        print ("player1 wins")
    else :
        print ("computer wins")
elif player1 == "paper":
    if player2 == "rock":
        print("player1 wins")
    else:
        print("computer wins")
elif player1 == "scissor":
    if player2 == "paper":
        print("player1 wins")
    else:
        print("computer wins")
else:
    print("invalid input!")