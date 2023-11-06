from sprite_object import *
import pygame
from Settings import *


class Weapon(AnimatedSprite):

    def __init__(self, game, path='Resources/Weapons/0t.png', scale=4.0, animation_time=60):
        super().__init__(game=game, path=path, scale=scale, animation_time=animation_time)
        self.images = deque(
            [pygame.transform.smoothscale(img, (self.image.get_width() * scale, self.image.get_height() * scale))
             for img in self.images])
        # Weapon position scale
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height())
        self.reloading = False  # Sets reload to false
        self.num_images = len(self.images)
        self.frame_counter = 0
        self.damage = 50  # Weapon Damage

    def animate_shot(self):
        if self.reloading:
            self.game.player.shot = False
            if self.animation_trigger:
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frame_counter += 1
                if self.frame_counter == self.num_images:
                    self.reloading = False
                    self.frame_counter = 0

    def draw(self):
        self.game.screen.blit(self.images[0], self.weapon_pos)

    def update(self):
        self.check_animation_time()
        self.animate_shot()
