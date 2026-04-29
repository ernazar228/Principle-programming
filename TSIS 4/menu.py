import pygame
from db import get_top_scores
from settings import load_settings, save_settings

def leaderboard_screen(screen, font):
    back_btn = pygame.Rect(300, 700, 200, 50)

    while True:
        screen.fill((255, 255, 255))

        draw_text(screen, font, "TOP 10 LEADERBOARD", 250, 80)

        top_scores = get_top_scores()

        y = 150
        for i, row in enumerate(top_scores):
            name, score, level, played_at = row
            date = played_at.strftime("%Y-%m-%d")

            text = f"{i + 1}. {name} | {score} | Level {level} | {date}"
            draw_text(screen, font, text, 100, y)
            y += 45

        draw_button(screen, font, "Back", back_btn)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_btn.collidepoint(event.pos):
                    return "back"
def settings_screen(screen, font):
    settings = load_settings()

    grid_btn = pygame.Rect(300, 250, 200, 50)
    color_btn = pygame.Rect(300, 330, 200, 50)
    save_btn = pygame.Rect(300, 450, 200, 50)

    colors = [
        [0, 0, 0],
        [0, 255, 0],
        [0, 0, 255],
        [255, 0, 0],
        [255, 255, 0]
    ]

    color_index = 0

    while True:
        screen.fill((255, 255, 255))

        draw_text(screen, font, "SETTINGS", 330, 120)

        draw_button(screen, font, "Grid: " + str(settings["grid"]), grid_btn)
        draw_button(screen, font, "Change Color", color_btn)
        draw_button(screen, font, "Save & Back", save_btn)

        pygame.draw.rect(
            screen,
            settings["snake_color"],
            (370, 400, 60, 30)
        )

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:
                if grid_btn.collidepoint(event.pos):
                    settings["grid"] = not settings["grid"]

                if color_btn.collidepoint(event.pos):
                    color_index += 1
                    if color_index >= len(colors):
                        color_index = 0

                    settings["snake_color"] = colors[color_index]

                if save_btn.collidepoint(event.pos):
                    save_settings(settings)
                    return "back"

WIDTH = 800
HEIGHT = 800


def draw_text(screen, font, text, x, y):
    img = font.render(text, True, (0, 0, 0))
    screen.blit(img, (x, y))


def draw_button(screen, font, text, rect):
    pygame.draw.rect(screen, (200, 200, 200), rect)
    pygame.draw.rect(screen, (0, 0, 0), rect, 2)

    img = font.render(text, True, (0, 0, 0))
    img_rect = img.get_rect(center=rect.center)
    screen.blit(img, img_rect)


def main_menu(screen, font):
    username = ""

    play_btn = pygame.Rect(300, 300, 200, 50)
    leaderboard_btn = pygame.Rect(300, 370, 200, 50)
    settings_btn = pygame.Rect(300, 440, 200, 50)
    quit_btn = pygame.Rect(300, 510, 200, 50)

    while True:
        screen.fill((255, 255, 255))

        draw_text(screen, font, "SNAKE GAME", 310, 120)
        draw_text(screen, font, "Username:", 250, 210)
        draw_text(screen, font, username, 400, 210)

        draw_button(screen, font, "Play", play_btn)
        draw_button(screen, font, "Leaderboard", leaderboard_btn)
        draw_button(screen, font, "Settings", settings_btn)
        draw_button(screen, font, "Quit", quit_btn)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit", username

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_BACKSPACE:
                    username = username[:-1]
                elif len(username) < 20 and event.unicode.isprintable():
                    username += event.unicode

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_btn.collidepoint(event.pos) and username != "":
                    return "play", username

                if leaderboard_btn.collidepoint(event.pos):
                    return "leaderboard", username

                if settings_btn.collidepoint(event.pos):
                    return "settings", username

                if quit_btn.collidepoint(event.pos):
                    return "quit", username
def game_over_screen(screen, font, score, level, best_score):
    quit_btn = pygame.Rect(300, 590, 200, 50)

    while True:
        screen.fill((255, 255, 255))

        draw_text(screen, font, "GAME OVER", 320, 120)
        draw_text(screen, font, "Score: " + str(score), 300, 220)
        draw_text(screen, font, "Level: " + str(level), 300, 270)
        draw_text(screen, font, "Best Score: " + str(best_score), 300, 320)
        draw_button(screen, font, "Quit", quit_btn)

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "quit"

            if event.type == pygame.MOUSEBUTTONDOWN:

                if quit_btn.collidepoint(event.pos):
                    return "quit"