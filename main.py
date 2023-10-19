#Name: Kylan, Harry, Nick
#Description: This is the main class, it implements all the classes
#Date: 10/19/2023


import pygame
import sys
from Settings import *
from map import *
from player import *


# This is the main class for the game
class Game:
    def __init__(self):
        self.init()

    def init(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)

    def update(self):
        self.player.update()
        pygame.display.flip()
        self.delta_time = self.clock.tick(FPS)
        pygame.display.set_caption("Extinction")

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.map.draw()
        self.player.draw()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    def run(self):
        while True:
            self.check_events()
            self.draw()
            self.update()


if __name__ == '__main__':
    game = Game()
    game.run()
