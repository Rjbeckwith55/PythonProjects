import pygame

class Ship():
    def __init__(self,screen):
        self.screen=screen

        self.image = pygame.image.load('images/rocket.png')
        pygame.transform.scale(self.image,(20,20))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
    def blitme(self):
        self.screen.blit(self.image,self.rect)
    def handle_keys(self):
        
                if event.key == pygame.K_UP:
                    ship.move_x(5)
                    print("up")
    def move_x(self,speed):
        
        
