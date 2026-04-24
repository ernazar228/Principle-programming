import pygame
import random

pygame.init()
snake_body = []
length = 1



screen = pygame.display.set_mode((800, 800))
lose = pygame.image.load("kindpng_3943771.png").convert_alpha()
clock = pygame.time.Clock()
x = 80

y = 80
score = 0
snake = 20
speed = 5
lose = pygame.transform.scale(lose,(100, 100))
font = pygame.font.Font(None, 36)

lose_rect = lose.get_rect(topleft=(75, 75))
food_x = 300
food_y = 200
direction = "RIGHT"
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            
    
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            if event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            if event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
    if direction == "LEFT":
        x -= speed
    if direction == "RIGHT":
        x += speed
    if direction == "UP":
        y -= speed
    if direction == "DOWN":
        y += speed
    snake_body.append([x, y])
    if len(snake_body) > length:
                snake_body.pop(0)
    if x < 0 or x >= 800 or y < 0 or y >= 800:
        run = False
         
    
    for part in snake_body:
            pygame.draw.rect(screen, (0, 0, 0), (part[0], part[1], snake, snake))
    snake_rect = pygame.Rect(x, y, snake, snake)
    food_rect = pygame.Rect(food_x, food_y, snake, snake)
    text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(text, (10, 10))
    pygame.display.update()
    
    clock.tick(60)
    if snake_rect.colliderect(food_rect):
        if snake_rect.colliderect(food_rect):
            print("eat")
            score += 1
        length += 8
        food_x = random.randrange(0, 800, snake)
        food_y = random.randrange(0, 800, snake)
    
    screen.fill((255, 255, 255))
    snake_rect = pygame.Rect(x, y, snake, snake)
    food_rect = pygame.Rect(food_x, food_y, snake, snake)
    

    
    pygame.draw.rect(screen, (0, 0, 0),(x, y, snake, snake))
    pygame.draw.rect(screen, (255, 0, 0), (food_x, food_y, snake, snake))
    

    pygame.display.update()
    
pygame.quit()