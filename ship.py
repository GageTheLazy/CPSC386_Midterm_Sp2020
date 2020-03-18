# Michael Gage Dimapindan CPSC 386 Midterm
# github account: GageTheLazy

import pygame
from pygame.locals import *
from pygame.sprite import Sprite
import pygame.time
from vector import Vector

class Ship:
    def __init__(self, game, vector=Vector()):
        self.game = game
        self.screen = game.screen
        self.velocity = vector
        self.screen_rect = game.screen.get_rect()
        self.image = pygame.draw.rect(screen, (255, 255, 255), (200, 150, 100, 50))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.lasers = pygame.sprite.Group()

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom

    def fire(self):
        laser = Laser(game=self.game)  # assuming Laser class has been made and is a sub-class of Sprite class
        self.lasers.add(laser)

    def remove_lasers(self):
        self.lasers.remove()

    def move(self):
        if self.velocity == Vector():
            return
        self.rect.left += self.velocity.x
        self.rect.top += self.velocity.y
        self.game.limit_on_screen(self.rect)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.draw()
        self.move()