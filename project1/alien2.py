import pygame, sys
from settings import Settings
from ship import Ship
from bullet import Bullet

class AlienInvasion:
    def __init__(self):
        """Initialize the game, screen, and settings."""
        pygame.init()
        self.settings = Settings()

        # 1. Create the game display window surface
        #full screen mode
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        #self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Alien Invasion")

        # 2. Setup the ship asset
        self.ship = Ship(self)
        self.bullets= pygame.sprite.Group()
    def run_game(self):
        """Start the main game loop."""
        # This loop must run continuously until you manually close it!
        while True:
            # Look for system events
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()
            
    
    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)


    def _check_keydown_events(self,event):

            if event.key == pygame.K_RIGHT:
                #move ship to the right
                self.ship.moving_right= True
        
            elif event.key ==pygame.K_LEFT:
                #move ship to the left
                self.ship.moving_left = True

            elif event.key == pygame.K_q:
                pygame.quit()
                sys.exit()

            elif event.key == pygame.K_SPACE:
                self._fire_bullet()

    def _check_keyup_events(self,event):
            
            if event.key == pygame.K_RIGHT:
                self.ship.moving_right= False
        
            elif event.key == pygame.K_LEFT:
                self.ship.moving_left= False

    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        new_bullet= Bullet(self)
        self.bullets.add(new_bullet)


    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.background)
                    
        # Draw ship onto the surface
        self.ship.blit_ship()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        # Push updates to your monitor display
        pygame.display.flip()
        
        


# CRUCIAL: Ensure there are no spaces or indents before 'if'
if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()
