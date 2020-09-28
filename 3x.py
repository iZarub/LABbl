import pygame
from pygame.draw import *
import numpy as np
FPS = 60
pygame.init()
screen = pygame.display.set_mode((1200, 750))
screen.fill((117, 187, 253))
pygame.draw.rect(screen, (0, 187, 0), (0, 350, 1200, 600))


def ob(x, y, R):
    pygame.draw.circle(screen, (255, 255, 255), (x, y), R)
    pygame.draw.circle(screen, (0, 0, 0), (x, y), R, 1)


for x in range(1000, 1160, 40):
    ob(x,100, 40)
for x in range(1020, 1140, 40):
    ob(x, 60, 40)
for x in range(500, 620, 30):
    ob(x, 200, 20)
for x in range(520, 600, 30):
    ob(x, 180, 20)
for x in range(200, 360, 40):
    ob(x, 70, 40)
for x in range(230, 320, 40):
    ob(x, 40, 40)


ob(570, 70, 40)
ob(620, 50, 40)
for i in range(37):
    c = i * np.pi / 36
    polygon(screen, (255, 255, 0),[(int(70 + 70 * np.cos(c)), int(100 - 70 * np.sin(c))), (int(70 + 70 * np.cos(np.pi * 2 / 3 + c)), int(100 - 70 * np.sin(np.pi * 2 / 3 + c))), (int(70 + 70 * np.cos(np.pi * 4 / 3 + c)), int(100 - 70 * np.sin(np.pi * 4 / 3 + c)))])

pygame.draw.rect(screen, (101, 67, 33), (100, 260, 300, 200))
pygame.draw.rect(screen, (52, 28, 2), (203, 312, 95, 95))
pygame.draw.rect(screen, (0, 0, 150), (210, 320, 80, 80))
pygame.draw.line(screen, (0, 0, 0), [250, 320], [250, 400], 5)
pygame.draw.polygon(screen, (100, 100, 100), [(100, 260), (400, 260),(250, 100)])

pygame.draw.rect(screen, (101, 67, 33), (700, 360, 300, 150))
pygame.draw.rect(screen, (52, 28, 2), (803, 390, 95, 95))
pygame.draw.rect(screen, (0, 0, 150), (810, 398, 80, 80))
pygame.draw.line(screen, (0, 0, 0), [850, 398], [850, 478], 5)
pygame.draw.polygon(screen, (100, 100, 100), [(700, 360), (1000, 360), (850, 260)])


def tr(x, y, R):
    pygame.draw.circle(screen, (0, 255, 0), (x, y), R)
    pygame.draw.circle(screen, (0, 0, 0), (x, y), R, 1)


pygame.draw.line(screen, (0, 0, 0), (450, 600), (450, 400), 18)
pygame.draw.line(screen, (0, 0, 0), (1100, 500), (1100, 300), 18)

x = 30
for y in range(400, 550, 20):
    x += 20
    pygame.draw.polygon(screen, (0, 255, 0), [(450+x, y), (450 - x, y), (450, y-20)])



for y in range(320, 410, 40):
    tr(1120, y, 30)
for y in range(320, 410, 40):
    tr(1080, y, 30)

pygame.draw.line(screen, (0, 0, 0), (750, 700), (750, 600), 9)
for y in range(600,660, 20):
    tr(760, y , 15)
for y in range(600, 660, 20):
    tr(740, y, 15)



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()




























