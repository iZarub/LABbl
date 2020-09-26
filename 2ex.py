import pygame
from pygame.draw import *
import numpy as np
list = [(400, 400), (450, 350), (450, 450)]
FPS = 60
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.draw.rect(screen, (117, 187, 253), (0, 0, 800, 600))
pygame.draw.rect(screen, (0, 187, 0), (0, 350, 800, 600))
pygame.draw.rect(screen, (101, 67, 33), (100, 260, 300, 200))

pygame.draw.rect(screen, (52, 28, 2), (203, 312, 95, 95))
pygame.draw.rect(screen, (0, 0, 150), (210, 320, 80, 80))
pygame.draw.line(screen, (0, 0, 0), [250, 320], [250, 400], 5)
pygame.draw.polygon(screen, (100, 100, 100), [(100, 260), (400, 260),(250, 100)])


def ob(x, y):
    pygame.draw.circle(screen, (255, 255, 255), (x, y), 30)
    pygame.draw.circle(screen, (0, 0, 0), (x, y), 30, 1)


for x in range(480, 580, 30):
    ob(x, 80)
for x in range(500, 560, 40):
    ob(x, 50)
pygame.draw.line(screen, (0, 0, 0), (600, 500), (600, 400), 18)


def tr(x, y):
    pygame.draw.circle(screen, (0, 255, 0), (x, y), 30)


for y in range(300, 400, 25):
    tr(600, y)
tr(650, 350)
tr(550, 350)
tr(630, 310)
tr(580, 310)
pygame.draw.circle(screen, (255, 255, 0), (700, 100), 50)







pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()































