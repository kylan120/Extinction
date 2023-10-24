#Name: Kylan, Harry, Nick
#Descripiton: This is the player class
#Date: 10/19/2023

import math
import pygame
import sys
from Settings import *
from map import *


class Player:
    def __init__(self, game):
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.speed = PLAYER_SPEED

#This is for when the player moves
    def movement(self):
        keys = pygame.key.get_pressed()

        move_x, move_y = 0, 0

        if keys[pygame.K_a]:
            move_x -= self.speed * self.game.delta_time
        if keys[pygame.K_d]:
            move_x += self.speed * self.game.delta_time
        if keys[pygame.K_w]:
            move_y -= self.speed * self.game.delta_time
        if keys[pygame.K_s]:
            move_y += self.speed * self.game.delta_time
        if keys[pygame.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pygame.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= 2 * math.pi

        self.check_wall_collision(move_x, move_y)

#This is when the player collides with the wall
    def check_wall_collision(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        player_rect = pygame.Rect(new_x, new_y, 10, 10)

        for wall_pos in self.game.map.world_map:
            wall_rect = pygame.Rect(wall_pos[0] * 100, wall_pos[1] * 100, 100, 100)

            if player_rect.colliderect(wall_rect):
                return

        self.x = new_x
        self.y = new_y

    def draw(self):
        pygame.draw.circle(self.game.screen, (255, 255, 255), (int(self.x), int(self.y)), 10)
        pygame.draw.line(self.game.screen, (255, 255, 255), (int(self.x), int(self.y)),
                         (int(self.x + 50 * math.cos(self.angle)), int(self.y + 50 * math.sin(self.angle))), 2)

    def update(self):
        self.movement()

    @property
    def pos(self):
        return self.x, self.y

    @property
    def map_pos(self):
        return int(self.x), int(self.y)
