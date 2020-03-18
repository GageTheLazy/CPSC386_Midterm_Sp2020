# Michael Gage Dimapindan CPSC 386 Midterm
# github account: GageTheLazy

import pygame
from pygame.locals import *
from pygame.sprite import Sprite
import pygame.time

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Vector ({}, {})".format(self.x, self.y)

    def __add__(self, other):
        xsum = self.x + other.x
        ysum = self.y + other.y
        return Vector(xsum, ysum)

    def __sub__(self, other):
        xdiff = self.x - other.x
        ydiff = self.y - other.y
        return Vector(xdiff, ydiff)

    def __rmul__(self, k: float):
        xprod1 = k.x * other.x
        yprod1 = k.y * other.y
        return Vector(xprod1, yprod1)

    def __mul__(self, k: float):
        xprod2 = k.x * self.x
        yprod2 = k.y * self.y
        return Vector(xprod2, yprod2)

    def __truediv__(self, k: float):
        xquot = k.x // self.x
        yquot = k.y // self.y
        return Vector(xquot, yquot)

    def __neg__(self):
        xneg = -1 * self.x
        yneg = -1 * self.y
        return Vector(xneg, yneg)

    def __eq__(self, other):
        xequals = self.x == other.x
        yequals = self.y == other.y
        return Vector(xequals, yequals)

@staticmethod
def test():
    v = Vector(x=5, y=5)
    u = Vector(x=4, y=4)

    print('v is {}'.format(v))
    print('u is {}'.format(u))
    print('u plus v is {}'.format(u+v))
    print('u minus v is {}'.format(u-v))
    print('ku is {}'.format(3*u))
    print('-u is {}'.format(-1*u))

def main():
    Vector.test()