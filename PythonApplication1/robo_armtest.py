import pygame
import time
#screen = pygame.display.set_mode((600,400))

CLOCK = pygame.time.Clock()
clock_speed = 20

positions = {0,0,0} # Declare an array size of 3 to hold the positions of the 3 motors

running = True
pygame.init()
base_move_right = False
base_move_left = False
arm_move_up = False
arm_move_down = False
claw_move_close = False
claw_move_open = False

while running:
    for event in pygame.event.get():
        print('loop')
        if event.type == pygame.KEYDOWN:

            # Movement of the Base right and left using the left and right arrow key
            if event.key == pygame.K_LEFT:
                print("left")
            elif event.key == pygame.K_RIGHT:
                print("right")
            elif event.key == pygame.K_UP:
                print("Up")
            elif event.key == pygame.K_DOWN:
                print("Down")
            elif event.key == pygame.K_2:
                print("close")
            elif event.key == pygame.K_1:
                print("Open")
            elif event.key == pygame.K_q:
                running = False
        if event.type == pygame.KEYUP:
            print("OFF")
           

        #set clock speed to limit cpu usage
        CLOCK.tick(clock_speed)
print("QUIT")
#BP.set_motor_position(PORT_A,0)
#BP.set_motor_position(PORT_B,0)
#BP.set_motor_position(PORT_C,0)