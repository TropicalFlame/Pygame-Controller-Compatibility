import sys
import pygame

#Please Read "ReadFirst.txt" Before Using

from pygame.locals import *
pygame.init()
pygame.display.set_caption('Controller Compatibility')
screen = pygame.display.set_mode((200, 200), 0, 32)
clock = pygame.time.Clock()

pygame.joystick.init()
joysticks = [pygame.joystick.Joystick(i) for i in range(pygame.joystick.get_count())]

keys = pygame.key.get_pressed()

while True:

    screen.fill((0, 0, 0))
    
    for event in pygame.event.get():
        if event.type == JOYBUTTONDOWN:
            print(event)
            if event.button == 0:
                print("A")
            if event.button == 1:
                print("B")
            if event.button == 2:
                print("X")
            if event.button == 3:
                print("Y")
            if event.button == 4:
                print("LB")
            if event.button == 5:
                print("RB")
            if event.button == 6:
                print("Screens")
            if event.button == 7:
                print("Lines")
            if event.button == 8:
                print("LAS")

        if event.type == JOYBUTTONDOWN:
            print("System Terminated")
            if event.button == 9:
                if event.type == QUIT:
                    pygame.quit()
                sys.exit()
                
        if event.type == KEYDOWN:
            print("System Terminated from PC")
            if event.key == K_ESCAPE:
                pygame.quit()
            sys.exit()
        
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.flip()
    pygame.display.update()
    clock.tick(60)
