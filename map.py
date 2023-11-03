# Name: Kylan, Harry, Nick
# Description: This is the map class where we can layout our map
# Date: 10/18/2023
import pygame as pg

# This makes the mini map using 1 and _ for layout
_ = False
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, _, _, _, _, _, _, _, _, _, _, _, _, 1, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, _, _, 2, _, _, _, 2, 2, _, _, _, 2, _, _, 1],
    [1, _, _, _, _, _, _, 3, 3, _, _, _, _, _, _, 1],
    [1, _, _, 2, _, _, _, 2, 2, _, _, _, 2, _, _, 1],
    [1, _, _, _, _, _, _, _, _, _, _, _, _, _, _, 1],
    [1, 1, _, _, _, _, _, _, _, _, _, _, _, _, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]


# This creates the map class and initialize it the class itself and game
class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()

    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    def draw(self):
        for pos in self.world_map:
            pg.draw.rect(self.game.screen, (255, 0, 0), (pos[0] * 100, pos[1] * 100, 100, 100), 1)
