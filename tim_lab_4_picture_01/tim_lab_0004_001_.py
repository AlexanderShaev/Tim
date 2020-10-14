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
pygame.draw.rect(screen, (255, 0, 255), (100, 100, 200, 200))
pygame.draw.rect(screen, (0, 0, 255), (100, 100, 200, 200), 5)
pygame.draw.polygon(screen, (255, 255, 0), [(100,100), (200,50),
                               (300,100), (100,100)])
pygame.draw.polygon(screen, (0, 0, 255), [(100,100), (200,50),
                               (300,100), (100,100)], 5)
pygame.draw.circle(screen, (0, 255, 0), (200, 175), 50)
pygame.draw.circle(screen, (255, 255, 255), (200, 175), 50, 5)


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
