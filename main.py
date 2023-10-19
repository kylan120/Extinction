import pygame
import sys
from Settings import *
from map import *

# This is the main class for the game
class Game:
    # This represents the object of the class itself
    def __init__(self):
        self.init()

    def init(self):
        pg.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.new_game()
    def new_game(self):
        self.map = Map(self)

    def update(self):
        pygame.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption("Extinction")

    # This will draw out the screen
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.map.draw()

    # This will check the events such as clicking exit or clicking the close button
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
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
