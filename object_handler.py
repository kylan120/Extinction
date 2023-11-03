from sprite_object import *


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        self.static_sprite_path = 'Resources/textures/Sprites/static_sprites/'
        self.anim_sprite_path = 'Resources/textures/Sprites/animated_sprites/'
        self.add_sprite(SpriteObject(game))
        self.add_sprite(AnimatedSprite(game))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
