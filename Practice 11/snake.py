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



food_weight = random.choice([1, 2, 3])
food_timer = pygame.time.get_ticks()
food_lifetime = 5000  
color = (255, 0, 0)
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
    
    head = snake_body[-1]
    snake_body[:-1]
    
    if head in snake_body[:-1]:
        run = False
    if x < 0 or x >= 800 or y < 0 or y >= 800:
        run = False
         
    
    for part in snake_body:
            pygame.draw.rect(screen, (0, 0, 0), (part[0], part[1], snake, snake))
    snake_rect = pygame.Rect(x, y, snake, snake)
    food_rect = pygame.Rect(food_x, food_y, snake, snake)
    text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(text, (10, 10))
    pygame.display.update()
    if pygame.time.get_ticks() - food_timer > food_lifetime:
        food_x = random.randrange(0, 800, snake)
        food_y = random.randrange(0, 800, snake)
        food_weight = random.choice([1, 2, 3])
        food_timer = pygame.time.get_ticks()

    
    clock.tick(60)
    if snake_rect.colliderect(food_rect):
        print("eat")
        score += food_weight
        length += food_weight * 5
        food_x = random.randrange(0, 800, snake)
        food_y = random.randrange(0, 800, snake)
        color = random.choice([(255, 0, 0), (0, 0, 255), (0, 255, 0)])
        food_weight = random.choice([1, 2, 3])
        food_timer = pygame.time.get_ticks()
    
    screen.fill((255, 255, 255))
    snake_rect = pygame.Rect(x, y, snake, snake)
    food_rect = pygame.Rect(food_x, food_y, snake, snake)
    

    
    pygame.draw.rect(screen, (0, 0, 0),(x, y, snake, snake))

    

    pygame.draw.rect(screen, color, (food_x, food_y, snake, snake))
    
    pygame.display.update()
    
pygame.quit()