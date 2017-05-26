import pygame
import time


CLOCK = pygame.time.Clock()
clock_speed = 20

positions = {0,0,0} # Declare an array size of 3 to hold the positions of the 3 motors
running = True
pygame.init()
print ('initialized')


pygame.init()

screen = pygame.display.set_mode((600,400))


while running:
    keys = pygame.key.get_pressed()
    pygame.display.update()

    if keys[pygame.K_LEFT]:
        positions[0] += 5  # Increase the positon of the base by 5 degrees
        #BP.set_motor_position(PORT_A,postions[0])
        print ('Base postion: ', positions[0])
    if keys[pygame.K_RIGHT]:
        positions[0] -= 5  # Decrease the positon of the base by 5 degrees
        #BP.set_motor_position(PORT_A,postions[0])
        print ("Base postion: ", positions[0])
    if keys[pygame.K_UP]:
        positions[1] += 5
        #BP.set_motor_position(PORT_B,postions[1])
        print ("Arm position: ", positions[1])
    if keys[pygame.K_DOWN]:
        positions[1] -= 5
        #BP.set_motor_position(PORT_B,postions[1])
        print ("Arm position: ", positions[1])
    if keys[pygame.K_1]:
        print ('1')
    CLOCK.tick(clock_speed)