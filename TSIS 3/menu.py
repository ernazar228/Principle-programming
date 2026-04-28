import pygame
import sys
import subprocess

pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Main Menu")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (80, 140, 255)

font = pygame.font.Font(None, 50)

play_button = pygame.Rect(300, 220, 200, 60)
exit_button = pygame.Rect(300, 320, 200, 60)


def draw_text(text, x, y, color):
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def main_menu():
    running = True

    while running:
        screen.fill(WHITE)

        draw_text("MAIN MENU", 400, 130, BLACK)

        pygame.draw.rect(screen, BLUE, play_button)
        pygame.draw.rect(screen, BLUE, exit_button)

        draw_text("PLAY", 400, 250, WHITE)
        draw_text("EXIT", 400, 350, WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(event.pos):
                    pygame.quit()
                    subprocess.run([sys.executable, "car.py"])
                    sys.exit()

                if exit_button.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()