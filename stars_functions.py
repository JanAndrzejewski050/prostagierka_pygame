import pygame
from classes import star_class
import random
from bullet_functions import bullets_list
from statek_functions import statek
import time


pygame.init()

how_often_spawn = 5
stars_list = []
points = 0
font = pygame.font.Font(None, 30)


def spawn_star(screen):
    if random.randint(0, how_often_spawn) == 1:
        star = star_class(size=40, color=(0, 0, 255), speed=8, x=random.randint(0, screen.get_width()), y=0)
        stars_list.append(star)


def star_fall(screen):
    for star in stars_list:
        star.fall()
        star_del(star, screen.get_height())
        statek.collision(star)
        star.draw(screen)
    draw_points()


def star_del(star, height):
    if star.y > height or got_destroyed(star) is True:
        stars_list.remove(star)


def got_destroyed(star):
    global points
    for bullet in bullets_list:
        if bullet.collision(star) is True:
            points += 1
            return True


def draw_points():
    text = font.render(f"Points: {points}", True, (255, 255, 255))
    return text