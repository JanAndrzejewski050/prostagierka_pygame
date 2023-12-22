import pygame
from classes import statek_class


statek = statek_class(size=40, color=(255, 0, 0), speed=10, x=400, y=560)  # punkt (0, 0) jest lewym górnym rogiem, pozycja to lewy górny róg kwadratu


def statek_is_on_screen(width, size, x):
    if x < 0:
        return False
    elif x > width - size:
        return False
    return True


def statek_moving(statek, screen):
    keyboard_input = pygame.key.get_pressed()

    if statek_is_on_screen(screen.get_width(), statek.size, statek.x) is True:
        statek.move_left_right(keyboard_input)
    else:
        if statek.x > screen.get_width()-statek.size:
            statek.x -= statek.speed
        else:
            statek.x += statek.speed
    statek.draw(screen)