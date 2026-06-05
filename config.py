import pygame

# SCREEN
WIDTH, HEIGHT = 672, 768

# GAME CONSTANT
GREEN = (0, 230, 0)
FONT_SIZE = 25

# TOP HUD (rules) 
TOP_HUD_HEIGHT = 130
TOP_HUD_MARGIN_X = 30
TOP_HUD_MARGIN_Y = 30
TEXT_SCORE_PADDING = 14

# BOTTOM HUD (rules)
BOTTOM_HUD_HEIGHT = 60
BOTTOM_HUD_MARGIN_X = 30
BOTTOM_HUD_PADDING_Y = 10
HUD_BOTTOM_Y = HEIGHT - BOTTOM_HUD_HEIGHT

LINE_WIDTH = 4
SHIP_IMG_SIZE = (36, 24)
SHIP_IMG_OFFSET = 45

# PLAY AREA
PLAY_AREA = pygame.Rect(
    0, 
    TOP_HUD_HEIGHT,
    WIDTH,
    HEIGHT - TOP_HUD_HEIGHT - BOTTOM_HUD_HEIGHT
)

# PLAYER
PLAYER_SIZE = (36, 24)
PLAYER_SPEED = 150

# SHIELD
SHIELD_SHAPE = [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0],
                [0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0],
                [0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0],
                [0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
                [1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1],
]
SHIELD_BLOCK_SIZE = (4, 4)
SPACE_BETWEEN = 150
NUM_SHIELDS = 4

# Bullet
PLAYER_BULLET_SIZE = (2, 10)
BULLET_SPEED = 600
ALIEN_BULLET_SPEED = 256
BULLET_SIZE = (8, 24)

# Explosion
MISS_EXPLOSION_FX_SIZE = (30, 30)
ALIEN_EXPLOSION_FX_SIZE = (38, 28)
EXPLOSION_RADIUS = 196
DIRECTION_DESTROY_CHANCE = 8
EDGE_DESTROY_CHANCE = 6
MISS_ALIEN_EXPLOSION_FX_SIZE = (18, 32)

# Aliens
NUM_ALIENS = 11
ALIENS_SETUP = ('alien_1', 'alien_1', 'alien_2', 'alien_2', 'alien_3')
ALIEN_SCORE = {'alien_1': 10, 'alien_2': 20, 'alien_3': 30}
ALIEN_STEP = 20
ALIEN_SIZE = (36, 28)
ALIEN_SHOOT_TIMER = 0.875

ALIEN_TIMER = 0.03125
HORIZONTAL_STEP = 6
VERTICAL_STEP = 32
FORMATION_MARGIN = 32

# Menu
LETTER_TIMER = 0.0625