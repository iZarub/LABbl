import pygame
from pygame.draw import *
from random import randint
pygame.init()
pygame.font.init()
myfont = pygame.font.SysFont('Comic Sans MS', 50)
screen = pygame.display.set_mode((1200, 900))

n = 0
FPS = 0.7


RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]



def new_ball(x,y,r):
    """
    :param x: координата центра шара по Ox
    :param y: координата центра шара по Oy
    :param r: радиус шара
     """
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click(event):
    """
    :param event: записывает координаты круга
    """
    print(x, y, r)


def score(pos, n, x, y, r):
    """
    :param pos: параметр, отвечающий за координаты нажатия мыши
    :param n: накопленные очки
    :param x: координата центра шара по Ox
    :param y: координата центра шара по Oy
    :param r: радиус шара
    :return: возвращает очки +1 или -2 в зависимости от попадания / не попадания
    """
    x1 = pos[0]
    y1 = pos[1]
    if (x - x1)**2 + (y - y1)**2 <= r**2:
        return 1
    else:
        textsurface1 = myfont.render('ПРОМАХ!', False, (255, 0, 0))
        screen.blit(textsurface1, (x, y))
        return -2



pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            click(event)
            n += score(event.pos, n, x, y, r)


    x = randint(100, 700)
    y = randint(100, 500)
    r = randint(30, 50)
    textsurface = myfont.render('Счет: ' + str(n), False, (255, 255, 255))
    screen.blit(textsurface, (10, 20))
    new_ball(x, y, r)
    pygame.display.update()
    screen.fill(BLACK)

pygame.quit()




























