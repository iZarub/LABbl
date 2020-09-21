import pygame
from pygame.draw import *

FPS = 60
pygame.init()
screen = pygame.display.set_mode((600, 600))
rect(screen, (0, 0, 255), [0, 0, 600, 600])
circle(screen, (255, 255, 0), (300, 300), 150)
circle(screen, (255, 0, 0), (220, 250), 30)
circle(screen, (0, 0, 0), (220, 250), 15)
circle(screen, (255, 0, 0), (380, 260), 20)
circle(screen, (0, 0, 0), (380, 260), 10)
line(screen, (0, 0, 0), [260, 250], [150, 140], 10)
line(screen, (0, 0, 0), [350, 260], [420, 180], 8)
line(screen, (0, 0, 0), [220,400], [380, 400], 17)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()





























