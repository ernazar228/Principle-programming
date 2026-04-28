import pygame

pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
font = pygame.font.Font(None, 30)

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

screen.fill(WHITE)

color = BLACK
drawing = False
last_pos = None
mode = "pencil"
start_pos = None
end_pos = None
run = True

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
            if event.key == pygame.K_p:
                mode = "pencil"

            if event.key == pygame.K_s:
                mode = "square"

        if event.type == pygame.MOUSEBUTTONDOWN:
            if drawing and mode == "pencil":
                pygame.draw.line(screen, color, last_pos, event.pos, 5)
                last_pos = event.pos

    if drawing and mode == "square":
        end_pos = event.pos
        if event.type == pygame.MOUSEBUTTONUP:
            if mode == "pencil":
                drawing = False
                last_pos = None

            if mode == "square":
                drawing = False

                x = start_pos[0]
                y = start_pos[1]
                width = end_pos[0] - start_pos[0]
                height = end_pos[1] - start_pos[1]

                pygame.draw.rect(screen, color, (x, y, width, height), 3)
        if event.type == pygame.MOUSEMOTION:
            if drawing:
                pygame.draw.line(screen, color, last_pos, event.pos, 5)
                last_pos = event.pos

    text1 = font.render("1 - Black", True, BLACK)
    text2 = font.render("2 - Red", True, RED)
    text3 = font.render("3 - Blue", True, BLUE)
    text4 = font.render("4 - Green", True, GREEN)
    text5 = font.render("C - Clear", True, BLACK)

    screen.blit(text1, (10, 10))
    screen.blit(text2, (10, 40))
    screen.blit(text3, (10, 70))
    screen.blit(text4, (10, 100))
    screen.blit(text5, (10, 130))

    pygame.display.update()
    clock.tick(60)

pygame.quit()