import pygame, sys
from  settings import Settings
from ship import Ship
from pygame.locals import *

class AlienInvaion:
    def __init__(self):
        pygame.init()
       
        self.settings= Settings()

        self.screen= pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        self.ship= Ship(self)
        
    def run_game(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill(self.settings.background)
            self.ship.blit_ship()

            pygame.display.flip()


if __name__ == '__main__':
    ai= AlienInvaion()
    ai.run_game()
        
