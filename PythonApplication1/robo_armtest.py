import pygame
import time
import brickpi3

CLOCK = pygame.time.Clock()
clock_speed = 20

positions = {0,0,0} # Declare an array size of 3 to hold the positions of the 3 motors
running = True
pygame.init()

BP= brickpi3.BrickPi3()

WIDTH=600
HEIGHT=480
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Movement of the Base right and left using the left and right arrow key
            if event.key == pygame.K_LEFT:
                BP.set_motor_power(BP.PORT_A,20)
                print("left")
            elif event.key == pygame.K_RIGHT:
                BP.set_motor_power(BP.PORT_A,-20)
                print("right")
            elif event.key == pygame.K_UP:
                BP.set_motor_power(BP.PORT_B,20)
                print("Up")
            elif event.key == pygame.K_DOWN:
                BP.set_motor_power(BP.PORT_B,20)
                print("Down")
            elif event.key == pygame.K_2:
                BP.set_motor_power(BP.PORT_C,20)
                print("close")
            elif event.key == pygame.K_1:
                BP.set_motor_power(BP.PORT_C,20)
                print("Open")
            elif event.key == pygame.K_q:
                running = False
            else:
                print("unrecognized key")
        if event.type == pygame.KEYUP:
            BP.reset_all()
            print("OFF")
           

        #set clock speed to limit cpu usage
        CLOCK.tick(clock_speed)
pygame.quit()
print("QUIT")
BP.reset_all()
