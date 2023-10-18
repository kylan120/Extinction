import pygame as pg
import sys
from Settings import *

# This is the main class for the game
class Game:
    # This represents the object of the class itself
    def __init__(self):
        self.init()

    def init(self):
        pg.init()
        self.screen = pg.display.set_mode(RES)
        self.clock = pg.time.Clock()

    def new_game(self):
        pass

    def update(self):
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'FPS: {self.clock.get_fps():.1f}')

    # This will draw out the screen
    def draw(self):
        self.screen.fill((0, 0, 0))

    # This will check the events such as clicking exit or clicking the close button
    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    # This will run the game
    def run(self):
        while True:
            self.check_events()
            self.draw()
            self.update()

# This makes sure the game runs
if __name__ == '__main__':
    game = Game()
    game.run()
