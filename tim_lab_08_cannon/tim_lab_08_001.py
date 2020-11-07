# -*- coding: utf-8 -*-
"""
Created on Sat Nov  7 17:08:55 2020

@author: ccc
"""

#import pygame
#from random import randint # импорт функции randint, randint(start, end)
#from pygame.draw import * # чтобы не писать pygame.draw.circle а только circle
#pygame.init() # инициализация библиотеки

#fps = 30 # частота обновления экрана
#screen = pygame.display.set_mode((800, 800)) # создать окно


# цвета и список цветов
#red = (255, 0, 0) 
#blue = (0, 0, 255)
#yellow = (255, 255, 0)
#green = (0, 255, 0)
#magenta = (255, 0, 255)
#cyan = (0, 255, 255)
#black = (0, 0, 0)
#colors = [red, blue, yellow, green, magenta, cyan]

class Dog:
    def __init__(self, angry, count):
        self.angry = angry
        self.count = count
    
    def say_gaw(self):
        if self.angry:
            print('GAW-' * self.count)
        else:
            print('gaw-' * self.count)
    
    def ping(self):
        self.angry = True
    
    def feed(self, food_count):
        if food_count > 10:
            self.angry = False

my_dog = Dog(True, 3)
my_dog.say_gaw()
#my_dog.feed(20)
#my_dog.say_gaw()
#my_dog.ping()
#my_dog.say_gaw()
