import pygame

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((400, 400))
clock = pygame.time.Clock()
play = pygame.image.load("play.png").convert_alpha()
stop = pygame.image.load("stop.png").convert_alpha()
next = pygame.image.load("next song.png").convert_alpha()


play = pygame.transform.scale(play, (100, 100))
next = pygame.transform.scale(next,(100, 100))
stop = pygame.transform.scale(stop,(100, 100))
play_rect = play.get_rect(topleft=(150, 150))
stop_rect = stop.get_rect(topleft=(150, 150))
next_rect = next.get_rect(topright=(300, 300))

playing = False
current_song = 0
songs = ["Goku black theme.mp3", "want_you.mp3"]

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_rect.collidepoint(event.pos):
                if not playing:
                    pygame.mixer.music.load(songs[current_song])
                    pygame.mixer.music.play()
                    playing = True
                else:
                    pygame.mixer.music.stop()
                    playing = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if next_rect.collidepoint(event.pos):
                current_song +=1
                if current_song >= len(songs):
                    current_song = 0
                pygame.mixer.music.load(songs[current_song])
                pygame.mixer.music.play()
                playing = True



    screen.fill((255, 255, 255))
    clock.tick(60)
    if playing:
        screen.blit(stop, (stop_rect))
    else:
        screen.blit(play, (play_rect))
    screen.blit(next, (next_rect))





    
    
    pygame.display.flip()
pygame.quit()