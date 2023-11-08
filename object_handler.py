#Name: Kylan, Harry, Nick
#Description: This is the object handler class
#Date: 11/08/2023

from sprite_object import *
from NPC import *
from sound import *

class ObjectHandler:
    def __init__(self, game):

        self.game = game
        self.sprite_list = []
        self.npc_list = []
        self.npc_sprite_path = 'Resources/textures/Sprites/Enemies/'
        self.static_sprite_path = 'Resources/textures/Sprites/static_sprites/'
        self.anim_sprite_path = 'Resources/textures/Sprites/animated_sprites/'
        self.add_sprite(SpriteObject(game))
        self.add_sprite(AnimatedSprite(game))
        add_sprite = self.add_sprite
        add_npc = self.add_npc
        self.npc_positions = {}

        add_sprite(SpriteObject(game, pos=(10.5, 4.0)))
        add_sprite(AnimatedSprite(game, pos=(4.5, 5.5)))

        # NPC map
        add_npc(NPC(game))
        add_npc(NPC(game, pos=(11.5, 4.5)))
        add_npc(NPC(game, pos=(14.6, 4.5)))
        add_npc(NPC(game, pos=(12.0, 4.5)))

    def update(self):
        self.npc_positions = {npc.map_pos for npc in self.npc_list if npc.alive}
        [sprite.update() for sprite in self.sprite_list]
        [npc.update() for npc in self.npc_list]
        self.check_win()

    def add_npc(self, npc):
        self.npc_list.append(npc)

    def add_sprite(self, sprite):
        self.sprite_list.append(sprite)

    def check_win(self):
        if not len(self.npc_positions):
            self.game.object_renderer.win()
            self.game.sound.theme.stop()
            pg.display.flip()
            pg.time.delay(1500)
            self.game.new_game()

