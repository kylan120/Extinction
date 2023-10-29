#FilePath is resources/sprites/weapon/shotgun/
from sprite_object import *
import pygame
from Settings import *

class Weapon(AnimatedSprite):
                                    #Path, scale, and time of animation
    def __init__(self, game, path='resources/sprites/weapon/shotgun/0.png', scale=0.4, animation_time=90):
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
        self.images = deque(
            [pygame.transform.scmoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height()) #Weapon position scale
        self.reloading = False  #Sets reload to false
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 50 #Weapon Damage

    def draw(self): #Draw method that draws weapon
        self.game.screen.blit(self.images[0], self.weapon_pos)

    def update(self):
        pass