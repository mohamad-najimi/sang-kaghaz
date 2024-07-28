'''import pygame
import sys

# مقداردهی اولیه Pygame
pygame.init()

# تنظیمات صفحه
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("نمونه دکمه در Pygame")

# رنگ‌ها
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# تعریف فونت
font = pygame.font.Font(None, 36)

def draw_button(screen, rect, text):
    pygame.draw.rect(screen, BLUE, rect)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def main():
    button_rect = pygame.Rect(300, 250, 200, 50)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if button_rect.collidepoint(event.pos):
                    print("دکمه فشرده شد!")

        screen.fill(WHITE)
        draw_button(screen, button_rect, "دکمه من")

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
    '''
'''
# ۱ - Import library
import pygame
from pygame.locals import *
import sys

# ۲ - Initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

# رنگ‌ها
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# تعریف فونت
font = pygame.font.Font(None, 36)

def draw_button(screen, rect, text):
    pygame.draw.rect(screen, BLUE, rect)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def main():
    button_rect = pygame.Rect(220, 200, 200, 50)
    running = True            
    
    # ۴ - keep looping through
    while running:
        # ۵ - clear the screen before drawing it again
        screen.fill(WHITE)
        
        # ۶ - draw the screen elements
        draw_button(screen, button_rect, "play")
        
        # ۷ - update the screen
        pygame.display.flip()
        
        # ۸ - loop through the events
        for event in pygame.event.get():
            # check if the event is the X button 
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  
                if button_rect.collidepoint(event.pos):
                    print("دکمه فشرده شد!")
    
    # اگر خارج از حلقه `while` هستیم، بازی را خاتمه می‌دهیم
    pygame.quit()
    sys.exit(0)

if __name__ == "__main__":
    main()
'''
'''
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

'''



'''
#برنامه ای که پایتون نوشته
import pygame
from pygame.locals import *
import random
import sys

# ۲ - Initialize the game
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("بازی سنگ، کاغذ، قیچی")

# رنگ‌ها
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# تعریف فونت
font = pygame.font.Font(None, 36)

# تعریف گزینه‌های بازی
options = ["rock", "paper", "scissor"]

def draw_button(screen, rect, text):
    pygame.draw.rect(screen, BLUE, rect)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect(center=rect.center)
    screen.blit(text_surface, text_rect)

def get_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "equal!"
    elif (player_choice == "rock" and computer_choice == "scissor") or \
         (player_choice == "paper" and computer_choice == "rock") or \
         (player_choice == "scissor" and computer_choice == "paper"):
        return "you wins!"
    else:
        return "coputer wins !"

def main():
    button_rects = {
        "rock": pygame.Rect(50, 200, 150, 50),
        "paper": pygame.Rect(250, 200, 150, 50),
        "scissor": pygame.Rect(450, 200, 150, 50)
    }
    
    result = ""
    running = True            
    
    while running:
        screen.fill(WHITE)
        
        for option, rect in button_rects.items():
            draw_button(screen, rect, option)
        
        if result:
            result_surface = font.render(result, True, BLACK)
            result_rect = result_surface.get_rect(center=(width//2, height//2 + 100))
            screen.blit(result_surface, result_rect)
        
        pygame.display.flip()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:  
                for option, rect in button_rects.items():
                    if rect.collidepoint(event.pos):
                        player_choice = option
                        computer_choice = random.choice(options)
                        result = f" your choise: {player_choice},computer choice: {computer_choice}\n"
                        result += get_winner(player_choice, computer_choice)
    
    pygame.quit() 
    sys.exit(0)

if __name__ == "__main__":
    main()
'''

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
    
def play_game(player1):
    game_list = ["rock", "paper", "scissor"]
    player2 = random.choice(game_list)
    print(f"computer choice: {player2}")

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
        
running = True  

screen.fill (WHITE)





button_rect = pygame.Rect(220, 200, 200, 50)
draw_button(screen, button_rect, "Play")

pygame.display.flip()

def draw_images():
    screen.blit(img1 , rect1)
    screen.blit(img2 , rect2)
    screen.blit(img3 , rect3)
    #pygame.draw.rect(screen, BLUE, rect1, 1)
    #pygame.draw.rect(screen, BLUE, rect2, 2)
    #pygame.draw.rect(screen, BLUE, rect3, 3)

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
                print("The button was pressed")
                screen.fill(WHITE)
                draw_images()
                pygame.display.flip()
                playing = True
           else:    
            if rect1.collidepoint(event.pos):
                play_game("rock")
            elif rect2.collidepoint(event.pos):
                play_game("paper")
            elif rect3.collidepoint(event.pos):
                play_game("scissor")
