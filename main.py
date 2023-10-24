import pygame
import sys
from Settings import *
from map import *
from player import *


# This is the main class for the game
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        pygame.display.set_caption("Extinction")
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)

    def update(self):
        self.player.update()
        self.draw()
        self.delta_time = self.clock.tick(FPS)

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.map.draw()
        self.player.draw()
        pygame.display.flip()

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()


    def main(self):
        while True:
            self.check_events()
            self.player.update()  # Call the update method here
            self.draw()  # Call the draw method here



if __name__ == '__main__':
    game = Game()
    game.main()
