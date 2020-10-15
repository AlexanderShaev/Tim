# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 22:45:10 2020

@author: ccc
"""

import pygame
pygame.init() # инициализация библиотеки

fps = 30 # переменная - задаёт время обновления в главном цикле

screen = pygame.display.set_mode((400, 400)) # создание окна

# здесь будут рисоваться фигуры
def draw_here(surface, x, y, width, height, color):
    '''
    Функция рисует зайца
    ----------
    surface : TYPE
        объект pygame.
    x : TYPE
        координата x - жопы зайца.
    y : TYPE
        координата y - жопы зайца.
    width : TYPE
        высота картинки.
    height : TYPE
        ширина картинки.
    color : TYPE
        цвет картинки.

    Returns
    -------
    Изображение зайца.

    '''
    body_width = width // 2
    body_height = height // 2
    body_x = x
    body_y = y
    
    
    draw_body(body_x, body_y, body_width, body_width)
    draw_head()
    draw_ear()
    draw_leg()


def draw_body(surface, x, y, width, height, color):
    '''
    

    Функция рисует тело зайца
    ----------
    surface : TYPE
        объект pygame.
    x : TYPE
        координата x - жопы зайца.
    y : TYPE
        координата y - жопы зайца.
    width : TYPE
        высота картинки.
    height : TYPE
        ширина картинки.
    color : TYPE
        цвет картинки.

    Returns
    -------
    Изображение тела зайца.

    '''
    pygame.draw.ellipse(surface, color, (x - width // 2, y - height // 2,
                                         width, height)


def draw_head(surface, x, y, width, height, color):
    print('типа рисую голову')
#    pygame.draw.circle(surface, color, (x, y), height // 2)


def draw_ear(surface, x, y, width, height, color):
    '''

    Функция рисует ухо зайца
    ----------
   surface : TYPE
        объект pygame.
    x : TYPE
        координата x - нижней точки центра уха.
    y : TYPE
        координата y - нижней точки уха.
    width : TYPE
        высота картинки.
    height : TYPE
        ширина картинки.
    color : TYPE
        цвет картинки.

    Returns
    -------
    Изображение уха зайца.

    '''
    pygame.draw.ellipse(surface, color, (x - width // 2, y - height // 2,
                                         width, height)


def draw_leg(surface, x, y, width, height, color):
    '''
    

    Функция рисует ногу зайца
    ----------
   surface : TYPE
        объект pygame.
    x : TYPE
        координата x - нижней точки центра ноги.
    y : TYPE
        координата y - нижней точки ноги.
    width : TYPE
        высота картинки.
    height : TYPE
        ширина картинки.
    color : TYPE
        цвет картинки.

    Returns
    -------
    Изображение ноги зайца.

    '''
    pygame.draw.ellipse(surface, color, (x - width // 2, y - height // 2,
                                         width, height)


draw_here(screen, 200, 380, 350, 150, (255, 255, 255))





#pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 200), 2)
#pygame.draw.polygon(screen, (255, 255, 0),
#                    [(100,100), (200,50), (300,100)], 2)
#pygame.draw.circle(screen, (0, 255, 0), (200, 175), 50, 2)
'''
x1 = 100
y1 = 100
x2 = 300
y2 = 200
N = 10
color = (255, 255, 255)
pygame.draw.rect(screen, color, (x1, y1, x2-x1, y2-y1), 2)

h = (x2 - x1) // (N+1)
print(h)
x = x1 + h
print(x)
for i in range (N):
    pygame.draw.line(screen, color, (x, y1), (x, y2))
    x += h
'''

# конец блока рисования


# обновление экрана
pygame.display.update()
# эту же каманду нужно повторять
# если на экране происходят изменения


# основной цикл, в котором будут отслеживаться
# происходящие события
clock = pygame.time.Clock() # создание счётчика времени

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            clock.tick(fps) # задание FPS
            pygame.quit()


#finished = False
