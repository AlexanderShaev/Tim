# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 18:57:25 2020

@author: ccc
"""

import pygame
from random import randint # импорт функции randint, randint(start, end)
from pygame.draw import * # чтобы не писать pygame.draw.circle а только circle
pygame.init() # инициализация библиотеки

fps = 1 # частота обновления экрана
screen = pygame.display.set_mode((800, 800)) # создать окно


# цвета и список цветов
red = (255, 0, 0) 
blue = (0, 0, 255)
yellow = (255, 255, 0)
green = (0, 255, 0)
magenta = (255, 0, 255)
cyan = (0, 255, 255)
black = (0, 0, 0)
colors = [red, blue, yellow, green, magenta, cyan]


def new_ball():
    '''
    функция рисует новый круг

    Returns 
    -------
    None.

    '''
    global x, y, r # глобальные переменные
    x = randint(100, 1100)
    y = randint(100, 900)
    r = randint(10, 100)
    color = colors[randint(0, 5)]
    circle(screen, color, (x, y), r)


def click(event):
    print(x, y, r)
    

def compare():
    '''
    функция сравнивает место клика мышью и радиус круга
    и определеет "Попал!!!" или "Промазал"

    Returns
    -------
    None.

    '''
    shot = event.pos
    print('Выстрел --------------------', shot)
    a = ((x-shot[0])**2+(y-shot[1])**2)**0.5
    print('Расстояние до центра круга -', a)
    if a <= r:
        print('Попал!!!')
    else:
        print('Промазал!!!')

pygame.display.update() # обновление экрана
clock = pygame.time.Clock() # создание счётчика времени
finished = False


# основной цикл
while not finished: # пока не завершилось делать:
    clock.tick(fps) # сделать один шаг fps?
    for event in pygame.event.get(): # забирает список событий из очереди
        if event.type == pygame.QUIT: # сравнение с константой "Закрытие окна"
            finished = True # завершение программы
        elif event.type == pygame.MOUSEBUTTONDOWN:
            click(event)
            print('Click -----------------', x, y, r)
            compare()
#            if event.x == 0:
#                print('Попал')
#            else:
#                print('Промазал')
                


    new_ball() # новый круг
    pygame.display.update() # обновить окно
#    screen.fill(black) # залить всё окно одним цветом
    click(event)
    

pygame.quit()






#a = randint(0, 10)
#print(a)
