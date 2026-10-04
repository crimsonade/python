import pygame

class Ship:
    """A class to manage ship"""

    def __init__(self,ai_game):


        """Initialize ship and starting position"""

        self.screen= ai_game.screen
        self.screen_rect= ai_game.screen.get_rect()
        self.settings = ai_game.settings
        

        #Load the image and its rect object

        raw_image= pygame.image.load(r"C:\Users\Isaac\Desktop\Python\project1\image\lucaboiii-space-3800434_1920.png")

        self.ship_image= pygame.transform.scale(raw_image, (60,60))
        self.ship_rect= self.ship_image.get_rect()

        #starting position of the ship
        self.ship_rect.midbottom= self.screen_rect.midbottom    

        self.x= float(self.ship_rect.x)     
        self.moving_right = False
        self.moving_left = False


    def update(self):
        """Update the ship's position based on the movement flag."""
        # 1. Update ships x position value (not its rect directly)
        
        if self.moving_right and self.ship_rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed 
            
        
        if self.moving_left and self.ship_rect.left > self.screen_rect.left:
            self.x -= self.settings.ship_speed

    
        self.ship_rect.x = int(self.x)


    def blit_ship(self):
        #draw ship image unto ship rect object screen
        self.screen.blit(self.ship_image, self.ship_rect)

   
