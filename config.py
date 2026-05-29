import pygame

# SCREEN
WIDTH, HEIGHT = 700, 900

# GAME CONSTANT
GREEN = (0, 230, 0)
FONT_SIZE = 25

# TOP HUD (rules) 
TOP_HUD_HEIGHT = 100
TOP_HUD_MARGIN_X = 30
TOP_HUD_MARGIN_Y = 15
TEXT_SCORE_PADDING = 10

# BOTTOM HUD (rules)
BOTTOM_HUD_HEIGHT = 60
BOTTOM_HUD_MARGIN_X = 30
BOTTOM_HUD_PADDING_Y = 4
HUD_BOTTOM_Y = HEIGHT - BOTTOM_HUD_HEIGHT

LINE_WIDTH = 2
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
BULLET_SIZE = (2, 10)
BULLET_SPEED = 512

# Explosion
MISS_EXPLOSION_FX_SIZE = (20, 20)
ALIEN_EXPLOSION_FX_SIZE = (38, 28)

# Aliens
NUM_ALIENS = 11
ALIENS_SETUP = ('alien_1', 'alien_1', 'alien_2', 'alien_2', 'alien_3')
ALIEN_SCORE = {'alien_1': 10, 'alien_2': 20, 'alien_3': 30}
ALIEN_STEP = 20
ALIEN_SIZE = (36, 28)

DESCENT_STEP_Y = 25
ALIEN_TIMER = 0.025
FORMATION_VELOCITY = 512