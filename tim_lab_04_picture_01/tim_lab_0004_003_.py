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


# объявление функций


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
    
    head_width = width // 3
    head_height = width // 3
    head_x = x
    head_y = y - (height // 2) - (head_height // 2)
    
    ear_width = width // 3 // 3
    ear_height = height // 2 - head_height // 2
    ear_x = x
    ear_y = y - (height // 2) - (head_height // 2) 

    leg_width = width // 3
    leg_height = leg_width // 2
    leg_x = x
    leg_y = y  


    # тело
    draw_body(surface, body_x, body_y, body_width, body_height, color)


    # голова
    draw_head(surface, head_x, head_y, head_width, head_height, color)


    # левое ухо    
    ear_left_x = ear_x - head_width // 4
    draw_ear(surface, ear_left_x, ear_y, ear_width, ear_height, color)


    # правое ухо
    ear_right_x = ear_x + head_width // 4
    draw_ear(surface, ear_right_x, ear_y, ear_width, ear_height, color)


    # левая нога
    leg_left_x = leg_x - body_width
    draw_leg(surface, leg_left_x, leg_y, leg_width, leg_height, color)      
    
    
    # правая нога
    leg_right_x = leg_x + body_width
    draw_leg(surface, leg_right_x, leg_y, leg_width, leg_height, color)     
    

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
        высота всей картинки, с ушами.
    height : TYPE
        ширина всей картинки, по краям лап.
    color : TYPE
        цвет картинки.

    Returns
    -------
    Изображение тела зайца.

    '''
    print('типа рисую тело зайца - ', surface, x, y, width, height, color)
    x = x - width // 2
    y = y - height
    print('проверка размеров тела - ', x, y, width, height)
    pygame.draw.ellipse(surface, color, (x, y, width, height))
                        

def draw_head(surface, x, y, width, height, color):
    '''
    

    Функция рисует голову зайца в виде круга
    ----------
    surface : TYPE
        объект pygame.
    x : TYPE
        координата x - центра головы.
    y : TYPE
        координата y - центра головы.
    width : TYPE
        высота головы.
    height : TYPE
        ширина головы, равна высоте, т.к. рисуем круг.
    color : TYPE
        цвет картинки.

    Returns
    -------
    Изображение головы зайца.

    '''
    print('типа рисую голову зайца - ', surface, x, y, width, height, color)
    width = width // 2
    print('проверка размеров головы - ', surface, color, x, y, width)
    pygame.draw.circle(surface, color, (x, y), width)


def draw_ear(surface, x, y, width, height, color):
    '''
    

    Функция рисует ухо зайца
    ----------
    surface : TYPE
        объект pygame.
    x : TYPE
        координата x - низа уха.
    y : TYPE
        координата y - низа уха.
    width : TYPE
        высота уха.
    height : TYPE
        ширина уха.
    color : TYPE
        цвет картинки.

    Returns
    -------
    Изображение уха зайца.

    '''
    print('типа рисую ухо зайца - ', surface, x, y, width, height, color)
    x = x - width // 2
    y = y - height
    print('проверка размеров уха - ', x, y, width, height)
    pygame.draw.ellipse(surface, color, (x, y, width, height))


def draw_leg(surface, x, y, width, height, color):
    '''
    

    Функция рисует ногу зайца
    ----------
    surface : TYPE
        объект pygame.
    x : TYPE
        координата x - центра низа ноги.
    y : TYPE
        координата y - низа ноги.
    width : TYPE
        высота ноги.
    height : TYPE
        ширина ноги.
    color : TYPE
        цвет картинки.

    Returns
    -------
    Изображение ноги зайца.

    '''
    print('типа рисую ногу зайца - ', surface, x, y, width, height, color)
    x = x - width // 2
    y = y - height
    print('проверка размеров ноги - ', x, y, width, height)
    pygame.draw.ellipse(surface, color, (x, y, width, height))


# выполняю функции
                        
draw_here(screen, 200, 350, 200, 300, (255, 0, 255))


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
