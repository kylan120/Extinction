#Name: Kylan, Harry, and Nick
#Description: This is the palyers class
#Date: 10/19/2023

import pygame
import math
from Settings import *

class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE

#This is the for the movement function
    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

#This happens when the player presses the keys
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pygame.K_s]:
            dx -= speed_cos
            dy -= speed_sin
        if keys[pygame.K_a]:
            dx += speed_sin
            dy -= speed_cos
        if keys[pygame.K_d]:
            dx -= speed_sin
            dy += speed_cos
        self.x += dx
        self.y += dy

        if keys[pygame.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pygame.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= 2 * math.pi

#This draws the player
    def draw(self):
        end_pos = (self.x + WIDTH * math.cos(self.angle), self.y + WIDTH * math.sin(self.angle))
        pygame.draw.line(self.game.screen, (255, 255, 0), (int(self.x), int(self.y)), (int(end_pos[0]), int(end_pos[1])), 2)
        pygame.draw.circle(self.game.screen, (0, 255, 0), (int(self.x), int(self.y)), 10)

    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
