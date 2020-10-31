# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 22:58:56 2020

@author: ccc
"""

import pygame
from pygame.draw import * # чтобы не писать pygame.draw.circle а только circle
pygame.init() # инициализация библиотеки

fps = 30 # частота обновления экрана
screen = pygame.display.set_mode((800, 800)) # создать окно

red = (255, 0, 0) 
blue = (0, 0, 255)

pygame.display.update() # обновление экрана
clock = pygame.time.Clock() # создание счётчика времени
finished = False
# основной цикл - проверяет наступление событий
while not finished: # пока не завершилось делать:
    clock.tick(fps) # сделать один шаг fps?
    for event in pygame.event.get(): # забирает список событий из очереди
        if event.type == pygame.QUIT: # сравнение с константой "Закрытие окна"
            finished = True # завершение программы 
        elif event.type == pygame.MOUSEBUTTONDOWN: # сравнение "Нажатие"
            if event.button == 1: # левая кнопка
                circle(screen, red, event.pos, 20) # рисовать круг
                pygame.display.update() # обновить экран
            elif event.button == 3: # правая кнопка
                circle(screen, blue, event.pos, 50)
                pygame.display.update() # обновоить экран

pygame.quit()