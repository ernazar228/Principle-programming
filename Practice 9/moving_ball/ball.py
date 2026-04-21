import pygame

pygame.init()
screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
radius = 20
x = 100
y = 100
speed = 20


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x - radius:
        x -= speed
    if keys[pygame.K_RIGHT] and x + radius < 400:
        x += speed
    if keys[pygame.K_UP] and y - radius:
        y -= speed
    if keys[pygame.K_DOWN] and y + radius < 400:
        y += speed
    screen.fill((255, 255, 255))
    clock.tick(60)
    pygame.draw.circle(screen,(250, 0, 0), (x, y), radius)

        
    
    pygame.display.flip()
pygame.quit()
