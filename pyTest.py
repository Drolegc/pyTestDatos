#!/usr/bin/python
# -*- coding: latin-1 -*-
import os, sys
import time
import random

from pynput.keyboard import Key, Controller

Keyboard = Controller()

# How to press -> Keyboard.press('a') AFTER Keyboard.release('a')

# Enter -> (Key.enter)

# Multiple -> Keyboard.type('Prueba')

# First - Execute main
print('pyTest -> rapido tipeo para las operaciones')



def switch():
    print("cambia a la ventana de Cines, en 3 segundos empieza la magic")
    altaCine()
    altaFuncion()
    return



def altaCine():
    global cines
    global salas
    print("creando cine...")
    cines +=1
    salas +=1
    com = '2 CineCalle 123 Maldo {} 12 {} 0'.format(cines,salas)
    time.sleep(3)
    Keyboard.type(com)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    return True

def altaFuncion():
    
    print("creando funcion...")
    global cines
    global salas
    com = '3 Avatar {} {} 12 12 2019 12 12'.format(cines,salas)
    Keyboard.type(com)
    Keyboard.press(Key.enter)
    Keyboard.release(Key.enter)
    return True


command = ''
cines = 0;
salas = 0;

switch()