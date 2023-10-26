import pygame
import sys
from Settings import *
from map import Map
from player import Player
from raycasting import *

# This is the main class for the game
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.new_game()
        pygame.display.set_caption("Extinction")  # Set the window title

    # This updates the game state
    def update(self):
        self.player.update()
        self.raycasting.update()
        self.delta_time = self.clock.tick(FPS)

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting = RayCasting(self)

    # This will draw the game elements
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.map.draw()
        self.player.draw()
        pygame.display.flip()

    # This checks if the user hits any escape button to close the program
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

    # This runs the main game loop
    def main(self):
        while True:
            self.check_events()
            self.update()
            self.draw()

# This sets the main to the game
if __name__ == '__main__':
    game = Game()
    game.main()
