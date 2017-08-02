import brickpi3
import pygame
import time
pygame.init()
screen = pygame.display.set_mode((600,400))
BP = brickpi3.BrickPi3()
speed = 100
try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_s:
                    if speed == 50:
                        speed = 100
                    elif speed == 100:
                        speed = 50
                if event.key == pygame.K_SPACE: #Turn on rollers
                    BP.set_motor_power(BP.PORT_C,-speed)
                    BP.set_motor_power(BP.PORT_B,-speed)
                if event.key == pygame.K_b: #Turn on conveyor
                    BP.set_motor_power(BP.PORT_A,speed)
                if event.key == pygame.K_p: #Run 10 second demo program
                    BP.set_motor_power(BP.PORT_C,-speed)
                    BP.set_motor_power(BP.PORT_B,-speed)
                    time.sleep(4)
                    BP.set_motor_power(BP.PORT_A,speed)
                    time.sleep(6)
                    BP.set_motor_power(BP.PORT_C,-128)
                    BP.set_motor_power(BP.PORT_B,-128)
                    BP.set_motor_power(BP.PORT_A,-128)
                if event.key == pygame.K_q: #Hard shutoff
                    BP.set_motor_power(BP.PORT_A,0)
                    BP.set_motor_power(BP.PORT_C,0)
                    BP.set_motor_power(BP.PORT_B,0)
                    break;
                
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    BP.set_motor_power(BP.PORT_C,-128)
                    BP.set_motor_power(BP.PORT_B,-128)
                if event.key == pygame.K_b:
                    BP.set_motor_power(BP.PORT_A,-128)
        
except KeyboardInterrupt:
    BP.reset_all()
finally:
    BP.reset_all()
