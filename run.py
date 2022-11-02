import pygame
import sys

from pygame.locals import *

pygame.joystick.init()
print("Initialized", pygame.joystick.get_init())
no_of_controllers = pygame.joystick.get_count()
print("controllers",no_of_controllers)

joysticks = [pygame.joystick.Joystick(x) for x in range(pygame.joystick.get_count())]
print("no of controllers:",len(joysticks))

axis = {}
button = {}

# these are the identifiers for the PS4's accelerometers
AXIS_X = 3
AXIS_Y = 4

# variables we'll store the rotations in, initialised to zero
rot_x = 0.0
rot_y = 0.0

# main loop
while True:

    # copy rot_x/rot_y into axis[] in case we don't read any
    axis[AXIS_X] = rot_x
    axis[AXIS_Y] = rot_y

    # retrieve any events ...
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.JOYAXISMOTION:
            axis[event.axis] = round(event.value,2)
        elif event.type == pygame.JOYBUTTONDOWN:
            button[event.button] = True
        elif event.type == pygame.JOYBUTTONUP:
            button[event.button] = False

    rot_x = axis[AXIS_X]
    rot_y = axis[AXIS_Y]
