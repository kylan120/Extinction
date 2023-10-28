import pygame
import sys
from Settings import *
from map import *
from player import *
from raycasting import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode(RES)
        self.clock = pygame.time.Clock()
        self.delta_time = 1
        self.game_started = False #Flags to check if the game has started
        self.new_game()

    def new_game(self):
        self.map = Map(self)
        self.player = Player(self)
        self.raycasting = RayCasting(self)

    def update(self):
        if self.game_started:
            self.player.update()
            self.raycasting.update()
        else:
            self.check_start_button_clicked() #Checks for start button click

            pygame.display.set_caption("Extinction")
            pygame.display.flip()
            self.delta_time = self.clock.tick(FPS)

    def draw(self):
        self.screen.fill((0, 0, 0))
        if not self.game_started:
            self.check_start_button_clicked() #Draws the start button if the gamestart hasn't been called

    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                pygame.quit()
                sys.exit()
            elif not self.game_started and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                self.check_start_button_clicked() #Checks for start btn click

    def check_start_button_clicked(self):
        #Checks if the start button is clicked
        mouse_pos = pygame.mouse.get_pos()
        button_rect = pygame.Rect(450, 175, 200, 100)#Button Position

        if button_rect.collidepoint(mouse_pos):
            print("Button clicked") #DEBUG
            self.game_started = True
            if not self.game_started:
                self.new_game()   #only calls new game if it hasn't started yet

        #Draws button
        pygame.draw.rect(self.screen, (255, 255, 255), button_rect)#Button Border
        font = pygame.font.Font(None, 35)
        text = font.render("Start Game", True, (0, 0, 0))
        text_rect = text.get_rect(center=button_rect.center)
        self.screen.blit(text, text_rect)  # draws button text

    def run(self):
        while True:
            self.check_events()
            self.draw()
            self.update()


if __name__ == '__main__':
    game = Game()
    game.run()
