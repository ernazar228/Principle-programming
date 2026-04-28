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
screen.fill(WHITE)

run = True
mode = "square"

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

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

            if event.key == pygame.K_s:
                mode = "square"
            if event.key == pygame.K_t:
                mode = "right_triangle"
            if event.key == pygame.K_e:
                mode = "equilateral_triangle"
            if event.key == pygame.K_r:
                mode = "rhombus"

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            if mode == "square":
                pygame.draw.rect(screen, color, (mouse_x, mouse_y, 60, 60))

            if mode == "right_triangle":
                pygame.draw.polygon(screen, color, [
                    (mouse_x, mouse_y),
                    (mouse_x + 60, mouse_y),
                    (mouse_x, mouse_y + 60)
                ])

            if mode == "equilateral_triangle":
                pygame.draw.polygon(screen, color, [
                    (mouse_x, mouse_y - 50),
                    (mouse_x - 50, mouse_y + 50),
                    (mouse_x + 50, mouse_y + 50)
                ])

            if mode == "rhombus":
                pygame.draw.polygon(screen, color, [
                    (mouse_x, mouse_y - 40),
                    (mouse_x + 50, mouse_y),
                    (mouse_x, mouse_y + 40),
                    (mouse_x - 50, mouse_y)
                ])

    text1 = font.render("1 - Black", True, BLACK)
    text2 = font.render("2 - Red", True, RED)
    text3 = font.render("3 - Blue", True, BLUE)
    text4 = font.render("4 - Green", True, GREEN)
    text5 = font.render("C - Clear", True, BLACK)

    text6 = font.render("S - Square", True, BLACK)
    text7 = font.render("T - Right Triangle", True, BLACK)
    text8 = font.render("E - Equilateral Triangle", True, BLACK)
    text9 = font.render("R - Rhombus", True, BLACK)

    screen.blit(text1, (10, 10))
    screen.blit(text2, (10, 40))
    screen.blit(text3, (10, 70))
    screen.blit(text4, (10, 100))
    screen.blit(text5, (10, 130))

    screen.blit(text6, (10, 180))
    screen.blit(text7, (10, 210))
    screen.blit(text8, (10, 240))
    screen.blit(text9, (10, 270))

    pygame.display.update()
    clock.tick(60)

pygame.quit()