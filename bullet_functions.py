import pygame
from classes import bullet_class


bullets_list = []
bullets_counter = 0
mouse_hold = False


def bullet_spawn(statek):
    global mouse_hold

    mouse_input = pygame.mouse.get_pressed()

    if mouse_input[0] is True and mouse_hold is False:   # lewy przycisk myszy
        bullet = bullet_class(size=7, color=(255, 255, 0), speed=13, x=statek.x + (statek.size//2), y=statek.y)
        bullets_list.append(bullet)
        mouse_hold = True
    elif mouse_input[0] is False:
        mouse_hold = False


def del_bullet(bullet):
    if bullet.y < 0 - bullet.size:
        bullets_list.remove(bullet)


def flying_bullets(screen):
    for bullet in bullets_list:
        bullet.flying()
        bullet.draw(screen)
        del_bullet(bullet)
