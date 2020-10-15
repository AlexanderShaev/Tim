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
    body_width = width // 3
    body_height = height // 2
    body_x = x
    body_y = y
    
    head_width = width
    head_height = width
    head_x = x
    head_y = y - height - head_height // 2
    
   
    draw_body(surface, body_x, body_y, body_width, body_height, color)
#    draw_head(surface, head_x, head_y, head_width, head_height, color)
#    draw_ear()
#    draw_leg()


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
    print('типа рисую тело зайца - ', surface, x, y, width, height, color)
    x = x - width // 2
    y = y - height
    print('проверка размеров - ', x, y, width, height)
    pygame.draw.ellipse(surface, color, (x, y, width, height))
                        
draw_here(screen, 200, 350, 150, 300, (255, 255, 255))

def draw_head(surface, x, y, width, height, color):
    '''
    

    Функция рисует голову зайца
    ----------
    surface : TYPE
        объект pygame.
    x : TYPE
        координата x - центра головы.
    y : TYPE
        координата y - центра головы.
    width : TYPE
        высота картинки.
    height : TYPE
        ширина картинки.
    color : TYPE
        цвет картинки.

    Returns
    -------
    Изображение головы зайца.

    '''
    print('типа рисую голову зайца - ', surface, x, y, width, height, color)
#    x = x - width // 2
#    y = y - height
#    print('проверка размеров - ', x, y, width, height)
#    pygame.draw.circle(surface, color, (x, y, width))
                        
draw_here(screen, 200, 350, 150, 300, (255, 255, 255))







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
