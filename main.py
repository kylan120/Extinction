#Name: Kylan, Harry, Nick
#Descripiton: This is the main class
#Date: 11/08/2023

import pygame
import sys
from Settings import *
from map import *
from player import *
from raycasting import *
from object_renderer import *
from sprite_object import *
from object_handler import *
from weapon import *
from pathfinding import *
from sound import *
from pygame import gfxdraw
from random import randint


class Game:
    def __init__(self):
        pygame.init()
        pygame.mouse.set_visible(False)
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.global_trigger = False
        self.global_event = pg.USEREVENT + 0
        pg.time.set_timer(self.global_event, 50)  # 50 millisecond death animation time
        self.new_game()
        self.fire = Fire(self)

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.object_renderer = ObjectRenderer(self)
        self.raycasting = RayCasting(self)
        self.object_handler = ObjectHandler(self)
        self.weapon = Weapon(self)
        self.pathfinding = PathFinding(self)
        self.sound = Sound(self)
        self.sound.theme.play(loops=-1)

    def update(self):
        self.fire.update()
        self.player.update()
        self.raycasting.update()
        self.object_handler.update()
        self.weapon.update()
        pygame.display.set_caption("Extinction (fps: " + f'{self.clock.get_fps() :.1f}' + ")")
        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)

    def draw(self):
        self.object_renderer.draw()
        self.fire.draw_fire()
        self.weapon.draw()

    def check_events(self):
        self.global_trigger = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif event.type == self.global_event:
                self.global_trigger = True
            self.player.single_fire_event(event)

    def run(self):
        while True:
            self.check_events()
            self.draw()
            self.update()


class Fire:
    def __init__(self, game):
        self.game = game
        self.palette = self.get_palette()
        self.fire_array = self.get_fire_array()

    def do_fire(self):
        for x in range(FIRE_WIDTH):
            for y in range(1, FIRE_HEIGHT):
                color_index = self.fire_array[y][x]
                if color_index:
                    rnd = randint(0, 3)
                    self.fire_array[y - 1][(x - rnd + 1) % FIRE_WIDTH] = color_index - rnd % 2
                else:
                    self.fire_array[y - 1][x] = 0

    def draw_fire(self):
        for y, row in enumerate(self.fire_array):
            for x, color_index in enumerate(row):
                if color_index:
                    color = self.palette[color_index]
                    gfxdraw.box(self.game.screen, (x * PIXEL_SIZE, y * PIXEL_SIZE, PIXEL_SIZE,
                                                   PIXEL_SIZE), color)

    def get_fire_array(self):
        fire_array = [[0 for i in range(FIRE_WIDTH)] for j in range(FIRE_HEIGHT)]
        for i in range(FIRE_WIDTH):
            fire_array[FIRE_HEIGHT - 1][i] = len(self.palette) - 1
        return fire_array

    @staticmethod
    def get_palette():
        palette = [(0, 0, 0)]
        for i, color in enumerate(COLORS[:-1]):
            c1, c2 = color, COLORS[i + 1]
            for step in range(STEPS_BETWEEN_COLORS):
                c = pygame.Color(c1).lerp(c2, (step + 0.5) / STEPS_BETWEEN_COLORS)
                palette.append(c)
        return palette

    def update(self):
        self.do_fire()

    def draw(self):
        self.draw_fire()


if __name__ == '__main__':
    game = Game()
    game.run()
