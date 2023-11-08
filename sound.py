import pygame


class Sound:
    def __init__(self, game):
        self.game = game
        pygame.mixer.init()
        self.path = 'Resources/sounds/'
        self.gun = pygame.mixer.Sound(self.path + 'pew.wav')
        self.theme = pygame.mixer.Sound(self.path + 'extinction_theme.wav')
        self.npc_pain = pygame.mixer.Sound(self.path + 'npc_pain.wav')
        self.npc_attack = pygame.mixer.Sound(self.path + 'npc_attack.wav')
        self.npc_death = pygame.mixer.Sound(self.path + 'npc_death.wav')
        self.player_pain = pygame.mixer.Sound(self.path + 'oof.wav')
