import brickpi3
import pygame
import time
pygame.init()
screen = pygame.display.set_mode((600,400))
BP = brickpi3.BrickPi3()
try:
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    BP.set_motor_power(BP.PORT_C,100)
                    BP.set_motor_power(BP.PORT_B,100)
                if event.key == pygame.K_b:
                    BP.set_motor_power(BP.PORT_A,100)
                if event.key == pygame.K_p:
                    BP.set_motor_power(BP.PORT_C,100)
                    BP.set_motor_power(BP.PORT_B,100)
                    time.sleep(4)
                    BP.set_motor_power(BP.PORT_A,100)
                    time.sleep(6)
                    BP.set_motor_power(BP.PORT_C,-128)
                    BP.set_motor_power(BP.PORT_B,-128)
                    BP.set_motor_power(BP.PORT_A,-128)
                
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
