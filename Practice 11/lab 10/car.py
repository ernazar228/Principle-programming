import pygame
import random

pygame.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
x = 200
y = 200
score = 0
speed = 5
left_border = 120
right_border = 280
road = pygame.image.load("road.png").convert_alpha()
car = pygame.image.load("car.png").convert_alpha()
enemy = pygame.image.load("traffic.png").convert_alpha()
enemy = pygame.transform.scale(enemy, (50, 50))

road = pygame.transform.scale(road, (200, 800))
car = pygame.transform.scale(car, (50, 50))
enemy_x = random.choice([140, 200, 260])
enemy_rect = pygame.transform.scale(enemy, (50, 50))
enemy_y = -100
enemy_speed = 5
font = pygame.font.Font(None, 36)

road_rect = road.get_rect(center = (200,200))
car_rect = car.get_rect(center = (200,200))
mode = "choose"

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    clock.tick(60)
    enemy_y += enemy_speed
    if enemy_y > 800:
        score += 1
        enemy_y = -100
        enemy_x = random.choice([140, 200, 260])
    car_rect = pygame.Rect(x, y, 50, 50)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 50)
    if car_rect.colliderect(enemy_rect):
        run = False
    

    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT]:
         x -= speed
    if key[pygame.K_RIGHT]:
        x += speed
    if key[pygame.K_UP]:
        y -= speed
    if key[pygame.K_DOWN]:
        y += speed
    
    if x < 120:
        x = 120

    if x > 280:
        x = 280
    if x < left_border:
        x = left_border

    if x > right_border:
        x = right_border    
    car_rect.x = x
    car_rect.y = y

    screen.fill((255, 255, 255))
    screen.blit(road, road_rect)
    screen.blit(enemy, (enemy_x, enemy_y))
    screen.blit(car, car_rect)

    text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(text, (10, 10))

    pygame.display.update()
pygame.quit()