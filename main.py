#Name: Kylan, Harry, and Nick
#Descripiton: This is the main class, that implements all the classes to the game
#Date: 10/25/2023

import pygame
import sys
from Settings import *
from map import *
from player import *


# This is the main class for the game
class Game:
    def __init__(self):
        self.map = Map(self)
        self.player = Player(self)
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        pygame.display.set_caption("Extinction")
        self.clock = pygame.time.Clock()
        self.delta_time = 1

#This updates the player
    def update(self):
        self.player.update()
        self.draw()
        self.delta_time = self.clock.tick(FPS)

#This will draw out the player
    def draw(self):
        self.screen.fill((0, 0, 0))
        self.map.draw()
        self.player.draw()
        pygame.display.flip()

#This check if the user hits any escape button to close the program
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()

#This happens while everything is running it'll run the program
    def main(self):
        while True:
            self.check_events()
            self.player.update()
            self.draw()

#This sets the main to the game
if __name__ == '__main__':
    game = Game()
    game.main()
