import pygame
import subprocess
pygame.init()

screen = pygame.display.set_mode((400, 400))
play = pygame.image.load("play.png").convert_alpha()
snake_menu = pygame.image.load("snake_menu.png").convert_alpha()
car_menu = pygame.image.load("car_menu.png").convert_alpha()
paint = pygame.image.load("paint.png").convert_alpha()
run = True
playing = False
mode = "choose"
snake_menu = pygame.transform.scale(snake_menu,(100, 100))
car_menu = pygame.transform.scale(car_menu,(100, 100))
play = pygame.transform.scale(play, (100, 100))
paint = pygame.transform.scale(paint, (100, 100))


snake_menu_rect = snake_menu.get_rect(topleft=(150, 150))
play_rect = play.get_rect(topleft=(150, 150))
car_menu_rect = car_menu.get_rect(topleft = (75, 75))
paint_rect = paint.get_rect(topleft = (250, 75))
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mode == "choose":
                if play_rect.collidepoint(event.pos):
                    mode = "menu"

            elif mode == "menu":
                if snake_menu_rect.collidepoint(event.pos):
                     subprocess.Popen(["python", "snake.py"])
                if car_menu_rect.collidepoint(event.pos):
                     subprocess.Popen(["python", "car.py"])
                if paint_rect.collidepoint(event.pos):
                     subprocess.Popen(["python", "paint.py"])
        
                    

        if mode == "choose":
            screen.fill((255, 255, 255))
            screen.blit(play, play_rect)
           
        elif mode == "menu":
             screen.fill((255, 255, 255))
             screen.blit(car_menu, car_menu_rect)
             screen.blit(snake_menu, snake_menu_rect)
             screen.blit(paint, paint_rect)
            


        pygame.display.update()
pygame.quit()

