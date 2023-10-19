#Name: Kylan, Harry, Nick
#Description: This is the map class where we can layout our map
#Date: 10/18/2023
import pygame as pg

#This makes the mini map using 1 and 0 for layout
mini_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 1, 1, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

#This creates the map class and initiliaze it the class itself and game
class Map:
    def __init__(self, game):
        self.game = game
        self.mini_map = mini_map
        self.world_map = {}
        self.get_map()


    #This will get the map
    def get_map(self):
        for j, row in enumerate(self.mini_map):
            for i, value in enumerate(row):
                if value:
                    self.world_map[(i, j)] = value

    #This will draw the layout of the map
    def draw(self):
        for pos in self.world_map:
            pg.draw.rect(self.game.screen, 'red', (pos[0] * 100, pos[1] * 100, 100, 100), 1)
