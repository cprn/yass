import sys
import pygame
import math
from pygame.locals import QUIT, MOUSEBUTTONDOWN, KEYDOWN, K_ESCAPE

W = 800
H = 600

pygame.init()

screen = pygame.display.set_mode((W, H))

stars = pygame.image.load('background.jpg').convert_alpha()
cross = pygame.image.load('crosshair.png').convert_alpha()
ship = pygame.image.load('spaceship.png').convert_alpha()
clock = pygame.time.Clock()

pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

while True:
    clock.tick(60)
    for e in pygame.event.get():
        if e.type == QUIT or (e.type == KEYDOWN and e.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        elif e.type == MOUSEBUTTONDOWN and e.button == 1:
            print('*pew pew!*')
        elif e.type == MOUSEBUTTONDOWN and e.button == 3:
            print('*swoosh!*')

    screen.blit(stars, (0, 0))
    pos = pygame.mouse.get_pos()
    screen.blit(cross, (pos))
    angle = math.atan2(pos[0]-W/2, pos[1]-H/2)*180/math.pi
    player = pygame.transform.rotate(ship, angle)
    rect = player.get_rect(center=(W/2, H/2))
    screen.blit(player, rect)
    pygame.display.update()
