# Name: Kylan, Nick, Harry
# Description: This stores the main game settings
# Date: 10/19/2023
import math

# This sets the resolution of the screen
RES = WIDTH, HEIGHT = 1300, 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60  # Set the FPS to a reasonable value

# Adjust the player position to be within the screen's bounds
PLAYER_POS = 150, 150

# This sets the player's speed, angle, and rotation speed
PLAYER_ANGLE = 0
PLAYER_SPEED = 1
PLAYER_ROT_SPEED = 0.01

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
