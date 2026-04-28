import pygame
from datetime import datetime

pygame.init()
screen = pygame.display.set_mode((400, 400))

background = pygame.image.load("Mickey.png").convert_alpha()
minute = pygame.image.load("left_hand.png").convert_alpha()
second = pygame.image.load("right_hand.png").convert_alpha()

minute = pygame.transform.scale(minute, (250, 250))
second = pygame.transform.scale(second, (250, 250))
background = pygame.transform.scale(background, (250, 250))
center = (200, 200)

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False

    screen.fill((255, 255, 255))
    screen.blit(background, (75, 75))

    t = datetime.now()
    m = t.minute
    s = t.second

    m_rot = pygame.transform.rotate(minute, -m * 6)
    s_rot = pygame.transform.rotate(second, -s * 6)

    m_rect = m_rot.get_rect(center=center)
    s_rect = s_rot.get_rect(center=center)

    screen.blit(m_rot, m_rect)
    screen.blit(s_rot, s_rect)

    pygame.display.update()

pygame.quit()