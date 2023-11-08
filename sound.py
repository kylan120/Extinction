import pygame


class Sound:
    def __init__(self, game):
        self.game = game
        pygame.mixer.init()
        self.path = 'Resources/sounds/'
        self.gun = pygame.mixer.Sound(self.path + 'pew.wav')



