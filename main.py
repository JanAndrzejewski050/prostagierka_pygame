import pygame
from classes import *
from statek_functions import *
from bullet_functions import *
from stars_functions import *
import sys
import time


pygame.init()
# ustawianie ekranu
width, height = 800, 600
screen = pygame.display.set_mode((width, height))


def main():

    statek_moving(statek, screen)
    bullet_spawn(statek)
    flying_bullets(screen)

    spawn_star(screen)
    star_fall(screen)
    text = draw_points()
    screen.blit(text, (10, 10))


# petla dzialania gierki
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    screen.fill((0, 0, 0))
    main()

    # odswiezenie ekranu
    pygame.display.flip()
    pygame.time.Clock().tick(60)
