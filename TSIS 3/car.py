import pygame
import random
import json
import os

pygame.init()

def load_leaderboard():
    if os.path.exists("leaderboard.json"):
        with open("leaderboard.json", "r") as file:
            return json.load(file)
    return []


def save_leaderboard(name, score, distance):
    leaderboard = load_leaderboard()

    leaderboard.append({
        "name": name,
        "score": score,
        "distance": distance
    })

    leaderboard = sorted(
        leaderboard,
        key=lambda x: x["score"],
        reverse=True
    )

    leaderboard = leaderboard[:10]

    with open("leaderboard.json", "w") as file:
        json.dump(leaderboard, file, indent=4)


def show_game_over(screen, font, score, distance):
    screen.fill((255, 255, 255))

    title = font.render("GAME OVER", True, (255, 0, 0))
    score_text = font.render("Score: " + str(score), True, (0, 0, 0))
    distance_text = font.render("Distance: " + str(distance), True, (0, 0, 0))
    info = font.render("Press ESC to quit", True, (0, 0, 0))

    screen.blit(title, (100, 100))
    screen.blit(score_text, (100, 160))
    screen.blit(distance_text, (100, 210))
    screen.blit(info, (60, 280))

    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False

player_name = input("Enter your name: ")
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()

x = 200
y = 300
score = 0
distance = 0
finish_distance = 1000
speed = 5

left_border = 120
right_border = 280
under = 300

shield = pygame.image.load("shield.png").convert_alpha()
road = pygame.image.load("road.png").convert_alpha()
car = pygame.image.load("car.png").convert_alpha()
enemy = pygame.image.load("traffic.png").convert_alpha()

enemy = pygame.transform.scale(enemy, (50, 50))
shield = pygame.transform.scale(shield, (50, 50))
road = pygame.transform.scale(road, (200, 800))
car = pygame.transform.scale(car, (50, 50))

enemy_x = random.choice([140, 200, 260])
enemy_y = -100
enemy_speed = 5

font = pygame.font.Font(None, 36)

road_rect = road.get_rect(center=(200, 200))

coin_x = random.choice([140, 200, 260])
coin_y = -300
coin_speed = 4
coin_weight = random.choice([1, 2, 3])
coin_timer = pygame.time.get_ticks()
coin_lifetime = 5000
coin_color = (255, 255, 0)

# OBSTACLE
obstacle_x = random.choice([140, 200, 260])
obstacle_y = -500
obstacle_speed = 4
obstacle_color = (60, 60, 60)

# POWER UP
power_x = random.choice([140, 200, 260])
power_y = -700
power_speed = 4
power_type = random.choice(["shield", "nitro", "repair"])

shield_active = False
nitro_active = False
nitro_start_time = 0
nitro_duration = 4000

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    clock.tick(60)

    enemy_y += enemy_speed
    coin_y += coin_speed
    obstacle_y += obstacle_speed
    power_y += power_speed

    # DISTANCE
    distance += 1

    if distance >= finish_distance:
        run = False

    if power_y > 800:
        power_y = -700
        power_x = random.choice([140, 200, 260])
        power_type = random.choice(["shield", "nitro", "repair"])

    if coin_y > 800:
        coin_y = -300
        coin_x = random.choice([140, 200, 260])
        coin_weight = random.choice([1, 2, 3])
        coin_timer = pygame.time.get_ticks()

    if pygame.time.get_ticks() - coin_timer > coin_lifetime:
        coin_y = -300
        coin_x = random.choice([140, 200, 260])
        coin_weight = random.choice([1, 2, 3])
        coin_timer = pygame.time.get_ticks()

    if enemy_y > 800:
        score += 1
        enemy_y = -100
        enemy_x = random.choice([140, 200, 260])

    if obstacle_y > 800:
        obstacle_y = -500
        obstacle_x = random.choice([140, 200, 260])

    car_rect = pygame.Rect(x, y, 50, 50)
    enemy_rect = pygame.Rect(enemy_x, enemy_y, 50, 50)
    coin_rect = pygame.Rect(coin_x, coin_y, 25, 25)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, 40, 40)
    power_rect = pygame.Rect(power_x, power_y, 30, 30)

    # ENEMY COLLISION WITH SHIELD
    if car_rect.colliderect(enemy_rect):
        if shield_active:
            shield_active = False
            enemy_y = -100
            enemy_x = random.choice([140, 200, 260])
        else:
            run = False

    if car_rect.colliderect(coin_rect):
        score += coin_weight
        enemy_speed += 0.5

        coin_y = -300
        coin_x = random.choice([140, 200, 260])
        coin_weight = random.choice([1, 2, 3])
        coin_timer = pygame.time.get_ticks()

    # POWER UP COLLECT
    if car_rect.colliderect(power_rect):
        if power_type == "shield":
            shield_active = True

        elif power_type == "nitro":
            nitro_active = True
            nitro_start_time = pygame.time.get_ticks()

        elif power_type == "repair":
            obstacle_y = -500
            score += 2

        power_y = -700
        power_x = random.choice([140, 200, 260])
        power_type = random.choice(["shield", "nitro", "repair"])

    # SPEED LOGIC
    if car_rect.colliderect(obstacle_rect):
        speed = 2
    else:
        speed = 5

    # NITRO EFFECT
    if nitro_active:
        speed = 9

        if pygame.time.get_ticks() - nitro_start_time > nitro_duration:
            nitro_active = False

    key = pygame.key.get_pressed()

    if key[pygame.K_LEFT]:
        x -= speed
    if key[pygame.K_RIGHT]:
        x += speed
    if key[pygame.K_UP]:
        y -= speed
    if key[pygame.K_DOWN]:
        y += speed

    if x < left_border:
        x = left_border
    if x > right_border:
        x = right_border
    if y > under:
        y = under
    if y < 0:
        y = 0

    car_rect.x = x
    car_rect.y = y

    screen.fill((255, 255, 255))
    screen.blit(road, road_rect)

    screen.blit(enemy, (enemy_x, enemy_y))

    pygame.draw.circle(screen, coin_color, (coin_x + 25, coin_y + 25), 12)
    pygame.draw.rect(screen, obstacle_color, obstacle_rect)

    # POWER UP DRAW
    if power_type == "shield":
        screen.blit(shield, (power_x, power_y))
    else:
        if power_type == "nitro":
            power_color = (255, 0, 255)
        else:
            power_color = (0, 255, 0)

        pygame.draw.circle(screen, power_color, (power_x + 15, power_y + 15), 15)

    screen.blit(car, car_rect)

    text = font.render("Score: " + str(score), True, (0, 0, 0))
    screen.blit(text, (10, 10))

    shield_text = font.render("Shield: " + str(shield_active), True, (0, 0, 0))
    screen.blit(shield_text, (10, 40))

    nitro_text = font.render("Nitro: " + str(nitro_active), True, (0, 0, 0))
    screen.blit(nitro_text, (10, 70))

    distance_text = font.render(
        "Distance: " + str(distance) + "/" + str(finish_distance),
        True,
        (0, 0, 0)
    )
    screen.blit(distance_text, (10, 100))

    pygame.display.update()

def show_leaderboard(screen, font):
    screen.fill((255, 255, 255))

    leaderboard = load_leaderboard()

    title = font.render("TOP 10 SCORES", True, (0, 0, 0))
    screen.blit(title, (60, 30))

    y = 80

    for i, player in enumerate(leaderboard):
        line = font.render(
            str(i + 1) + ". " +
            player["name"] +
            " Score: " + str(player["score"]) +
            " Dist: " + str(player["distance"]),
            True,
            (0, 0, 0)
        )

        screen.blit(line, (20, y))
        y += 35

    info = font.render("Press ESC to exit", True, (255, 0, 0))
    screen.blit(info, (70, 350))

    pygame.display.update()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                waiting = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False
save_leaderboard(player_name, score, distance)
show_game_over(screen, font, score, distance)
show_leaderboard(screen, font)
pygame.quit()