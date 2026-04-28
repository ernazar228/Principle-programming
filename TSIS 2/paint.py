import pygame
from datetime import datetime

pygame.init()

screen = pygame.display.set_mode((800, 800))
font = pygame.font.Font(None, 30)
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


def flood_fill(surface, x, y, new_color):
    target_color = surface.get_at((x, y))

    if target_color == new_color:
        return

    pixels = [(x, y)]

    while pixels:
        px, py = pixels.pop()

        if px < 0 or py < 0 or px >= surface.get_width() or py >= surface.get_height():
            continue

        if surface.get_at((px, py)) != target_color:
            continue

        surface.set_at((px, py), new_color)

        pixels.append((px + 1, py))
        pixels.append((px - 1, py))
        pixels.append((px, py + 1))
        pixels.append((px, py - 1))


brush_size = 5
size_input = False
size_text = ""

color = BLACK
screen.fill(WHITE)

run = True
mode = "pencil"

drawing = False
last_pos = None
start_pos = None
end_pos = None

# TEXT TOOL
text_input = False
text_value = ""
text_pos = None

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN: #the buttons

            # TEXT TOOL
            if text_input:
                if event.key == pygame.K_RETURN:
                    final_text = font.render(text_value, True, color)
                    screen.blit(final_text, text_pos)
                    text_input = False
                    text_value = ""

                elif event.key == pygame.K_ESCAPE:
                    text_input = False
                    text_value = ""

                elif event.key == pygame.K_BACKSPACE:
                    text_value = text_value[:-1]

                else:
                    text_value += event.unicode

                continue

            if size_input:
                if event.key == pygame.K_RETURN:
                    if size_text.isdigit():
                        brush_size = int(size_text)
                    size_input = False
                    size_text = ""

                elif event.key == pygame.K_BACKSPACE:
                    size_text = size_text[:-1]

                else:
                    size_text += event.unicode

            else:
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

                if event.key == pygame.K_5:
                    brush_size = 2
                if event.key == pygame.K_6:
                    brush_size = 5
                if event.key == pygame.K_7:
                    brush_size = 10

                if event.key == pygame.K_p:
                    mode = "pencil"

                # SAVE CANVAS: Ctrl + S
                if event.key == pygame.K_s and pygame.key.get_mods() & pygame.KMOD_CTRL:
                    filename = "paint_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".png"
                    pygame.image.save(screen, filename)
                    print("Saved:", filename)

                elif event.key == pygame.K_s:
                    mode = "square"

                if event.key == pygame.K_t:
                    mode = "right_triangle"
                if event.key == pygame.K_e:
                    mode = "equilateral_triangle"
                if event.key == pygame.K_r:
                    mode = "rhombus"
                if event.key == pygame.K_l:
                    mode = "line"
                if event.key == pygame.K_f:
                    mode = "fill"

                # TEXT TOOL
                if event.key == pygame.K_x:
                    mode = "text"

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = event.pos

            if 650 <= mouse_x <= 750 and 20 <= mouse_y <= 70:
                size_input = True
                size_text = ""

            elif mode == "pencil":
                drawing = True
                last_pos = event.pos

            elif mode == "fill":
                flood_fill(screen, mouse_x, mouse_y, color)

            # TEXT TOOL
            elif mode == "text":
                text_input = True
                text_value = ""
                text_pos = event.pos

            elif mode in ["square", "rhombus", "right_triangle", "equilateral_triangle", "line"]:
                drawing = True
                start_pos = event.pos
                end_pos = event.pos

        if event.type == pygame.MOUSEMOTION:
            if drawing and mode == "pencil":
                pygame.draw.line(screen, color, last_pos, event.pos, brush_size)
                last_pos = event.pos

            if drawing and mode in ["square", "rhombus", "right_triangle", "equilateral_triangle", "line"]:
                end_pos = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            if mode == "pencil":
                drawing = False
                last_pos = None

            elif mode == "square":
                drawing = False
                x = start_pos[0]
                y = start_pos[1]
                width = end_pos[0] - start_pos[0]
                height = end_pos[1] - start_pos[1]

                size = min(abs(width), abs(height))

                if width < 0:
                    x -= size
                if height < 0:
                    y -= size

                pygame.draw.rect(screen, color, (x, y, size, size), brush_size)

            elif mode == "rhombus":
                drawing = False
                x = start_pos[0]
                y = start_pos[1]
                width = end_pos[0] - start_pos[0]
                height = end_pos[1] - start_pos[1]

                points = [
                    (x + width // 2, y),
                    (x + width, y + height // 2),
                    (x + width // 2, y + height),
                    (x, y + height // 2)
                ]

                pygame.draw.polygon(screen, color, points, brush_size)

            elif mode == "right_triangle":
                drawing = False
                x = start_pos[0]
                y = start_pos[1]
                width = end_pos[0] - start_pos[0]
                height = end_pos[1] - start_pos[1]

                points = [
                    (x, y),
                    (x + width, y),
                    (x, y + height)
                ]

                pygame.draw.polygon(screen, color, points, brush_size)

            elif mode == "equilateral_triangle":
                drawing = False
                x = start_pos[0]
                y = start_pos[1]
                width = end_pos[0] - start_pos[0]
                height = end_pos[1] - start_pos[1]

                points = [
                    (x + width // 2, y),
                    (x, y + height),
                    (x + width, y + height)
                ]

                pygame.draw.polygon(screen, color, points, brush_size)

            elif mode == "line":
                drawing = False
                pygame.draw.line(screen, color, start_pos, end_pos, brush_size)

    text1 = font.render("1 - Black", True, BLACK)
    text2 = font.render("2 - Red", True, RED)
    text3 = font.render("3 - Blue", True, BLUE)
    text4 = font.render("4 - Green", True, GREEN)
    text5 = font.render("C - Clear", True, BLACK)

    text6 = font.render("P - Pencil", True, BLACK)
    text7 = font.render("S - Square", True, BLACK)
    text8 = font.render("T - Right Triangle", True, BLACK)
    text9 = font.render("E - Equilateral Triangle", True, BLACK)
    text10 = font.render("R - Rhombus", True, BLACK)
    text11 = font.render("L - Line", True, BLACK)
    text12 = font.render("F - Fill", True, BLACK)
    text13 = font.render("X - Text", True, BLACK)
    text14 = font.render("Ctrl+S - Save", True, BLACK)

    screen.blit(text1, (10, 10))
    screen.blit(text2, (10, 40))
    screen.blit(text3, (10, 70))
    screen.blit(text4, (10, 100))
    screen.blit(text5, (10, 130))

    screen.blit(text6, (10, 180))
    screen.blit(text7, (10, 210))
    screen.blit(text8, (10, 240))
    screen.blit(text9, (10, 270))
    screen.blit(text10, (10, 300))
    screen.blit(text11, (10, 330))
    screen.blit(text12, (10, 360))
    screen.blit(text13, (10, 390))
    screen.blit(text14, (10, 420))

    pygame.draw.rect(screen, BLACK, (650, 20, 100, 50), 2)

    if size_input:
        size_show = font.render("Size: " + size_text, True, BLACK)
    else:
        size_show = font.render(f"Size: {brush_size}", True, BLACK)

    screen.blit(size_show, (660, 35))

    # TEXT TOOL PREVIEW
    if text_input and text_pos is not None:
        preview = font.render(text_value, True, color)
        screen.blit(preview, text_pos)

    pygame.display.update()
    clock.tick(60)

pygame.quit()