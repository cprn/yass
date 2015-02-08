import sys
import pygame
import math
from pygame.locals import QUIT, MOUSEBUTTONDOWN

pygame.init()

screen = pygame.display.set_mode((800, 600))
stars = pygame.image.load('background.jpg').convert_alpha()
cross = pygame.image.load('crosshair.png').convert_alpha()
ship = pygame.image.load('spaceship.png').convert_alpha()
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)

while True:
    clock.tick(10)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONDOWN and event.button == 1:
            print('*pew pew!*')
        elif event.type == MOUSEBUTTONDOWN and event.button == 3:
            print('*swoosh!*')

    screen.blit(stars, (0, 0))
    pos = pygame.mouse.get_pos()
    screen.blit(cross, (pos))
    angle = 180+math.atan2(pos[0]-400, pos[1]-300)*180/math.pi
    print(round(angle))
    rotimage = pygame.transform.rotate(ship, angle)
    rect = rotimage.get_rect(center=(400, 300))
    screen.blit(rotimage, rect)
    pygame.display.update()
