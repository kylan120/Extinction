# Name: Kylan, Harry, Nick
# Description: This is the player class
# Date: 11/08/2023


from Settings import *
import pygame
import math


class Player:
    def __init__(self, game):
        #player attributes
        self.game = game
        self.x, self.y = PLAYER_POS
        self.angle = PLAYER_ANGLE
        self.shot = False
        self.health = PLAYER_MAX_HEALTH
        self.rel = 0

    def check_game_over(self):
        #Handles player death
        if self.health < 1:
            self.game.object_renderer.game_over()
            self.game.sound.theme.stop()
            pygame.display.flip()
            pygame.time.delay(1700)
            self.game.new_game()

    def get_damage(self, damage):
        #lowers player health, adds player pain sound
        self.health -= damage
        self.game.object_renderer.player_damage()
        self.check_game_over()
        self.game.sound.player_pain.play()

    def single_fire_event(self, event):         # makes 'self.shot' TRUE if mouse btn clicked
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and not self.shot and not self.game.weapon.reloading:
                self.game.sound.gun.play()
                self.shot = True
                self.game.weapon.reloading = True

    def movement(self):
        #player movement based on key inputs.
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        dx, dy = 0, 0
        speed = PLAYER_SPEED * self.game.delta_time
        speed_sin = speed * sin_a
        speed_cos = speed * cos_a

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            dx += speed_cos
            dy += speed_sin
        if keys[pygame.K_s]:
            dx += -speed_cos
            dy += -speed_sin
        if keys[pygame.K_a]:
            dx += speed_sin
            dy += -speed_cos
        if keys[pygame.K_d]:
            dx += -speed_sin
            dy += speed_cos

        self.check_wall_collision(dx, dy)

        if keys[pygame.K_LEFT]:
            self.angle -= PLAYER_ROT_SPEED * self.game.delta_time
        if keys[pygame.K_RIGHT]:
            self.angle += PLAYER_ROT_SPEED * self.game.delta_time
        self.angle %= math.tau

    def check_wall(self, x, y):
        #checks if wall is given position is a wall

        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        #checks if wall is given position is a wall and changes position if so
        scale = PLAYER_SIZE_SCALE / self.game.delta_time
        if self.check_wall(int(self.x + dx * scale), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * scale)):
            self.y += dy

    def draw(self):
        pygame.draw.circle(self.game.screen, 'green', (self.x * 100, self.y * 100), 15)

    def mouse_control(self):
        #mouse control for changing players view direction
        mx, my = pygame.mouse.get_pos()
        if mx < MOUSE_BORDER_LEFT or mx > MOUSE_BORDER_RIGHT:
            pygame.mouse.set_pos([HALF_WIDTH, HALF_HEIGHT])
        self.rel = pygame.mouse.get_rel()[0]
        self.rel = max(-MOUSE_MAX_REL, min(MOUSE_MAX_REL, self.rel))
        self.angle += self.rel * MOUSE_SENSITIVITY * self.game.delta_time

    def update(self):
        #updates players movement and inputs
        self.movement()
        self.mouse_control()

    @property
    def pos(self):
        #current player position
        return self.x, self.y

    @property
    def map_pos(self):
        #current player position on map
        return int(self.x), int(self.y)
