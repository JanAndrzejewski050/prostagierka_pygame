import pygame
import sys


class statek_class:
    def __init__(self, size, color, speed, x, y):
        self.size = size
        self.color = color
        self.speed = speed
        self.x = x
        self.y = y

    def move_left_right(self, keyboard_input):
        if keyboard_input[pygame.K_a]:
            self.x -= self.speed
        elif keyboard_input[pygame.K_d]:
            self.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))

    def fire_bullet(self, bullet_size, bullet_color, bullet_speed):
        bullet = bullet_class(bullet_size, bullet_color, bullet_speed, self.x + (self.size//2), self.y)

    def collision(self, object):
        if object.x-self.size <= self.x <= object.x+self.size and object.y >= self.y:
            pygame.quit()


class bullet_class:
    def __init__(self, size, color, speed, x, y):
        self.size = size
        self.color = color
        self.speed = speed
        self.x = x
        self.y = y

    def flying(self):
        self.y -= self.speed

    def collision(self, object):
        if object.x <= self.x <= object.x + object.size and object.y+object.size > self.y:
            return True

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))


class star_class:
    def __init__(self, size, color, speed, x, y):
        self.size = size
        self.color = color
        self.speed = speed
        self.x = x
        self.y = y

    def fall(self):
        self.y += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.size, self.size))
