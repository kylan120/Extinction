from sprite_object import *
# NW from NPC import *


class ObjectHandler:
    def __init__(self, game):
        self.game = game
        self.sprite_list = []
        # NW self.npc_list = []
        # NW self.npc_sprite_path = 'resources/sprites/npc/'
        self.static_sprite_path = 'Resources/textures/Sprites/static_sprites/'
        self.anim_sprite_path = 'Resources/textures/Sprites/animated_sprites/'
        self.add_sprite(SpriteObject(game))
        self.add_sprite(AnimatedSprite(game))
        # NW add_npc = self.add_npc

        #Sprite Map

        #NPC map
        add_npc(NPC(game))

    def update(self):
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]

    # NW def add_npc(self, npc):
        # NW self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)
