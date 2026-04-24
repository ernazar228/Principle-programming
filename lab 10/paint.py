import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
font = pygame.font.Font(None, 30)

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

color = BLACK
brush_size = 8

screen.fill(WHITE)

run = True
drawing = False

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            drawing = True

        if event.type == pygame.MOUSEBUTTONUP:
            drawing = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                color = BLACK
            if event.key == pygame.K_2:
                color = RED
            if event.key == pygame.K_3:
                color = BLUE
            if event.key == pygame.K_4:
                color = GREEN
            if event.key == pygame.K_c:
                screen.fill(WHITE)

    if drawing:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        pygame.draw.circle(screen, color, (mouse_x, mouse_y), brush_size)
    
    text1 = font.render("1 - Black", True, (0, 0, 0))
    text2 = font.render("2 - Red", True, (255, 0, 0))
    text3 = font.render("3 - Blue", True, (0, 0, 255))
    text4 = font.render("4 - Green", True, (0, 255, 0))
    text5 = font.render("C - Clear", True, (0, 0, 0))

    screen.blit(text1, (10, 10))
    screen.blit(text2, (10, 40))
    screen.blit(text3, (10, 70))
    screen.blit(text4, (10, 100))
    screen.blit(text5, (10, 130))

    pygame.display.update()
    clock.tick(60)

pygame.quit()