import pygame
import sys
import time
from ship import Ship


def run_game():
    pygame.init()
    screen = pygame.display.set_mode((640,480))
    pygame.display.set_caption("Rocket Game")
    
    #Make a new ship
    ship = Ship(screen)


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        ship.blitme()
        pygame.display.flip()
run_game()
