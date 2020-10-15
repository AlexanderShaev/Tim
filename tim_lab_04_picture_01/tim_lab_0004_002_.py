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
#pygame.draw.rect(screen, (255, 0, 0), (100, 100, 200, 200), 2)
#pygame.draw.polygon(screen, (255, 255, 0),
#                    [(100,100), (200,50), (300,100)], 2)
#pygame.draw.circle(screen, (0, 255, 0), (200, 175), 50, 2)

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
