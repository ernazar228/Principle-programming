import pygame
import random
from db import save_result, get_personal_best
from settings import load_settings
from menu import main_menu, leaderboard_screen, settings_screen, game_over_screen

pygame.init()
snake_body = []
length = 1





screen = pygame.display.set_mode((800, 800))
lose = pygame.image.load("kindpng_3943771.png").convert_alpha()
shield_img = pygame.image.load("shield.png").convert_alpha()
clock = pygame.time.Clock()

x = 80
y = 80
score = 0
snake = 20
speed = 5
level = 1
obstacles = []

lose = pygame.transform.scale(lose,(100, 100))
shield_img = pygame.transform.scale(shield_img, (20, 20))
shield = False


font = pygame.font.Font(None, 36)
while True:
    action, username = main_menu(screen, font)

    if action == "quit":
        pygame.quit()
        exit()

    if action == "leaderboard":
        leaderboard_screen(screen, font)

    if action == "play":
        break
    if action == "settings":
        settings_screen(screen, font)

best_score = get_personal_best(username)

settings = load_settings()
def draw_grid():
    if settings["grid"]:
        for i in range(0, 800, snake):
            pygame.draw.line(screen, (230, 230, 230), (i, 0), (i, 800))
            pygame.draw.line(screen, (230, 230, 230), (0, i), (800, i))


power_x = random.randrange(0, 800, snake)
power_y = random.randrange(0, 800, snake)

power_type = random.choice(["speed", "slow", "shield"])
power_timer = pygame.time.get_ticks()

shield = False
effect_start = 0
effect_type = None
food_weight = random.choice([1, 2, 3])
food_timer = pygame.time.get_ticks()
food_lifetime = 5000  
poison_x = random.randrange(0, 800, snake)
poison_y = random.randrange(0, 800, snake)
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
        if shield:
            shield = False
            x = 80
            y = 80
            snake_body = [[x, y]]
            direction = "RIGHT"
        else:
            run = False
    if x < 0 or x >= 800 or y < 0 or y >= 800:
        if shield:
            shield = False
            x = 80
            y = 80
            snake_body = [[x, y]]
            direction = "RIGHT"
        else:
            run = False
    if [x, y] in obstacles:
        if shield:
            shield = False
            x = 80
            y = 80
            snake_body = [[x, y]]
            direction = "RIGHT"
        else:
            run = False
         
    
    for part in snake_body:
            pygame.draw.rect(screen, settings["snake_color"], (part[0], part[1], snake, snake))
    snake_rect = pygame.Rect(x, y, snake, snake)
    food_rect = pygame.Rect(food_x, food_y, snake, snake)
    poison_rect = pygame.Rect(poison_x, poison_y, snake, snake)
    power_rect = pygame.Rect(power_x, power_y, snake, snake)
    
    text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(text, (10, 10))
    best_text = font.render("Best: " + str(best_score), True, (0, 0, 0))
    screen.blit(best_text, (10, 40))
    pygame.display.update()
    #здесь еда
    if pygame.time.get_ticks() - food_timer > food_lifetime:
        food_x = random.randrange(0, 800, snake)
        food_y = random.randrange(0, 800, snake)
        food_weight = random.choice([1, 2, 3])
        food_timer = pygame.time.get_ticks()
    #здесь бусты
    if pygame.time.get_ticks() - power_timer > 8000:
        power_x = random.randrange(0, 800, snake)
        power_y = random.randrange(0, 800, snake)
        power_type = random.choice(["speed", "slow", "shield"])
        power_timer = pygame.time.get_ticks()
    

    
    clock.tick(60)
    if snake_rect.colliderect(food_rect):
        print("eat")
        score += food_weight
        new_level = score // 5 + 1
        if new_level > level:
            level = new_level
            if level >= 3:
                obstacles = []
                for i in range(level + 2):
                    ox = random.randrange(0, 800, snake)
                    oy = random.randrange(0, 800, snake)
                    if abs(ox - x) > 60 or abs(oy - y) > 60:
                        obstacles.append([ox, oy])
        length += food_weight * 5
        food_x = random.randrange(0, 800, snake)
        food_y = random.randrange(0, 800, snake)
        color = random.choice([(255, 0, 0), (0, 0, 255), (0, 255, 0)])
        food_weight = random.choice([1, 2, 3])
        food_timer = pygame.time.get_ticks()
    
    if snake_rect.colliderect(poison_rect):
        length -= 2
        poison_x = random.randrange(0, 800, snake)
        poison_y = random.randrange(0, 800, snake)
        if length <= 1:
            run = False
    
    if snake_rect.colliderect(power_rect):
    
        if power_type == "speed":
            speed = 10
            effect_type = "speed"
            effect_start = pygame.time.get_ticks()

        elif power_type == "slow":
            speed = 3
            effect_type = "slow"
            effect_start = pygame.time.get_ticks()

        elif power_type == "shield":
            shield = True
            power_x = random.randrange(0, 800, snake)
            power_y = random.randrange(0, 800, snake)
            power_type = random.choice(["speed", "slow", "shield"])
            power_timer = pygame.time.get_ticks()
    if effect_type in ["speed", "slow"]:
        if pygame.time.get_ticks() - effect_start > 5000:
            speed = 5
            effect_type = None
    
    screen.fill((255, 255, 255))
    draw_grid()
    snake_rect = pygame.Rect(x, y, snake, snake)
    food_rect = pygame.Rect(food_x, food_y, snake, snake)
    power_rect = pygame.Rect(power_x, power_y, snake, snake)
    
    
    

    
    pygame.draw.rect(screen, settings["snake_color"], (x, y, snake, snake))

    

    pygame.draw.rect(screen, color, (food_x, food_y, snake, snake))
    pygame.draw.rect(screen, (100, 0, 0), (poison_x, poison_y, snake, snake))
    for block in obstacles:
        pygame.draw.rect(screen, (80, 80, 80), (block[0], block[1], snake, snake))
    

    level_text = font.render("Level: " + str(level), True, (0, 0, 0))
    screen.blit(level_text, (10, 70))

    if power_type == "speed":
        power_color = (255, 0, 255)
    elif power_type == "slow":
        power_color = (0, 150, 255)
    else:
        screen.blit(shield_img, (power_x, power_y))


    

pygame.display.update()
save_result(username, score, level)

result = game_over_screen(screen, font, score, level, best_score)

if result == "quit":
    pygame.quit()
    exit()
    
pygame.quit()