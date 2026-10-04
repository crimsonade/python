"""A setting class to store all settings."""

class Settings:
    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.background = (0, 0, 255) # Restored to light gray for visibility
        
        # ADD THIS LINE: Make sure the spelling matches perfectly
        self.ship_speed = 1.5

        # bullet settings
        self.bullet_speed = 1.5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)