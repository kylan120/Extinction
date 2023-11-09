from sprite_object import *
from random import randint, random, choice


# Nicholas, Kylan, Harry
# 10/29/2023
# npc file with logic etc. for npc


class NPC(AnimatedSprite):

    def __init__(self, game, path='Resources/textures/Sprites/Enemies/0.png',
                 pos=(10.5, 5.5), scale=0.6, shift=0.38, animation_time=180):
        super().__init__(game, path, pos, scale, shift, animation_time)
        self.attack_images = self.get_images(self.path + '/attack')
        self.death_images = self.get_images(self.path + '/death')
        self.idle_images = self.get_images(self.path + '/idle')
        self.pain_images = self.get_images(self.path + '/pain')
        self.walk_images = self.get_images(self.path + '/walk')

        self.attack_dist = randint(3, 3)
        self.speed = 0.015
        self.size = 10
        self.health = 100
        self.attack_damage = 10
        self.accuracy = 0.19
        self.alive = True
        self.pain = False
        self.ray_cast_value = False
        self.frame_counter = 0
        self.player_search_trigger = False

    #update method in game loop
    def update(self):
        self.check_animation_time()
        self.get_sprite()
        self.run_logic()

    def check_wall(self, x, y):
        #checks if the given position is a wall or not
        return (x, y) not in self.game.map.world_map

    def check_wall_collision(self, dx, dy):
        #basically saying if theres a wall collision to go around it instead
        if self.check_wall(int(self.x + dx * self.size), int(self.y)):
            self.x += dx
        if self.check_wall(int(self.x), int(self.y + dy * self.size)):
            self.y += dy

    def movement(self):
        #usiNG Pathfinding to move the NPCs towards the player
        next_pos = self.game.pathfinding.get_path(self.map_pos, self.game.player.map_pos)
        next_x, next_y = next_pos

        if next_pos not in self.game.object_handler.npc_positions:
            angle = math.atan2(next_y + 0.5 - self.y, next_x + 0.5 - self.x)
            dx = math.cos(angle) * self.speed
            dy = math.sin(angle) * self.speed
            self.check_wall_collision(dx, dy)

    def animate_death(self):
        #This animates the death sequence if npc is not alive
        if not self.alive:
            if self.game.global_trigger and self.frame_counter < len(self.death_images) - 1:
                self.death_images.rotate(-1)
                self.image = self.death_images[0]
                self.frame_counter += 1

    def animate_pain(self):
        #animates the NPC's pain if they are hit.
        self.animate(self.pain_images)
        if self.animation_trigger:
            self.pain = False

    def check_hit_in_npc(self):
        #this checks if the player's shot hits the NPC or not
        if self.ray_cast_value and self.game.player.shot:
            if HALF_WIDTH - self.sprite_half_width < self.screen_x < HALF_WIDTH + self.sprite_half_width:
                self.game.sound.npc_pain.play()
                self.game.player.shot = False
                self.pain = True
                self.health -= self.game.weapon.damage
                self.check_health()

    def check_health(self):
        #If health is below zero, play death sound and set alive to false
        if self.health < 1:
            self.alive = False
            self.game.sound.npc_death.play()

    def run_logic(self):
        #Main NPC logic behavior
        if self.alive:
            self.ray_cast_value = self.ray_cast_player_npc()
            self.check_hit_in_npc()

            if self.pain:
                self.animate_pain()

            elif self.ray_cast_value:
                self.player_search_trigger = True

                if self.dist < self.attack_dist:
                    self.animate(self.attack_images)
                    self.attack()
                else:
                    self.animate(self.walk_images)
                    self.movement()

            elif self.player_search_trigger:
                self.animate(self.walk_images)
                self.movement()
            else:
                self.animate(self.idle_images)
        else:
            self.animate_death()

    def attack(self):
        #Attack the player
        if self.animation_trigger:
            self.game.sound.npc_attack.play()
            if random() < self.accuracy:
                self.game.player.get_damage(self.attack_damage)

    @property
    #Gets current NPC map position
    def map_pos(self):
        return int(self.x), int(self.y)

    def ray_cast_player_npc(self):
        #Ray-cast to see if the player is visible to the NPC
        if self.game.player.map_pos == self.map_pos:
            return True

        #Variables for vert and horizontal wall and player distances
        wall_dist_v, wall_dist_h, = 0, 0
        player_dist_v, player_dist_h, = 0, 0

        #Player and map's position
        ox, oy = self.game.player.pos
        x_map, y_map = self.game.player.map_pos

        #ray angle, sin, cosine
        ray_angle = self.theta
        sin_a = math.sin(ray_angle)
        cos_a = math.cos(ray_angle)

        if sin_a == 0: #Deals with /0
            return False  # division by zero

        #horizontal raycasting variables
        y_hor, dy = (y_map + 1, 1) if sin_a > 0 else (y_map - 1e-6, -1)

        depth_hor = (y_hor - oy) / sin_a
        x_hor = ox + depth_hor * cos_a

        delta_depth = dy / sin_a
        dx = delta_depth * cos_a

        #horizontal ray casting execution
        for i in range(MAX_DEPTH):
            tile_hor = int(x_hor), int(y_hor)
            if tile_hor == self.map_pos:
                player_dist_h = depth_hor
                break
            if tile_hor in self.game.map.world_map:
                wall_dist_h = depth_hor
                break
            x_hor += dx
            y_hor += dy
            depth_hor += delta_depth

        #vertical raycasting variables
        x_vert, dx = (x_map + 1, 1) if cos_a > 0 else (x_map - 1e-6, -1)

        depth_vert = (x_vert - ox) / cos_a
        y_vert = oy + depth_vert * sin_a

        delta_depth = dx / cos_a
        dy = delta_depth * sin_a

        #vertical ray casting execution
        for i in range(MAX_DEPTH):
            tile_vert = int(x_vert), int(y_vert)
            if tile_vert == self.map_pos:
                player_dist_v = depth_vert
                break
            if tile_vert in self.game.map.world_map:
                wall_dist_v = depth_vert
                break
            x_vert += dx
            y_vert += dy
            depth_vert += delta_depth

        #player and wall distance and checks visibility
        player_dist = max(player_dist_v, player_dist_h)
        wall_dist = max(wall_dist_v, wall_dist_h)

        #If player is within the wall distance, and there's no wall inbetween, then the player is visible.
        #otherwise, they are not visible
        if 0 < player_dist < wall_dist or not wall_dist:
            return True
        return False
