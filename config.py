import pygame

# SCREEN
WIDTH, HEIGHT = 672, 768

# GAME CONSTANT
GREEN = (0, 230, 0)
FONT_SIZE = 25

# TOP HUD (rules) 
TOP_HUD_HEIGHT = 130
TOP_HUD_MARGIN_X = 30
TOP_HUD_MARGIN_Y = 20
TEXT_SCORE_PADDING = 10

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
PLAYER_SIZE = (32, 22)
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
SHIELD_BLOCK_SIZE = (3, 3)
SPACE_BETWEEN = 144
NUM_SHIELDS = 4

# Line
NUM_LINES = 224
LINE_SIZE = (3, 3)

# Bullet
PLAYER_BULLET_SIZE = (2, 10)
BULLET_SPEED = 600

# Explosion
MISS_EXPLOSION_FX_SIZE = (30, 30)
ALIEN_EXPLOSION_FX_SIZE = (38, 28)
EXPLOSION_RADIUS = 196
DIRECTION_DESTROY_CHANCE = 8
EDGE_DESTROY_CHANCE = 6
MISS_ALIEN_EXPLOSION_FX_SIZE = (18, 32)

# ALIENS
ALIENS_FORMATION = {
    'num_aliens': 11,
    'layout': ('alien_1', 'alien_1', 'alien_2', 'alien_2', 'alien_3'),
    'scores': {
        'alien_1': 10,
        'alien_2': 20,
        'alien_3': 30,
    },
    'size': (30, 22),
    'spacing': 18,
    'margin': 32,
}

ALIENS_MOVEMENT = {
    "horizontal_step": 6,
    "vertical_step": 32,
    "timer": 0.03125
}

# ALIENS BULLET
ALIENS_SHOOTING = {
    'speed': 256,
    'frames_time': 0.078125,
    'size': (8, 24)
}

# UFO
UFO = {
    'speed': 100,
    'spawn_timer': 25.6,
    'start_y': PLAY_AREA.top + 11,
    'start_x': (25, WIDTH - 25),
    'score_values': [
        100, 50, 50, 100, 150, 100, 100, 50,
        300, 100, 100, 100, 50, 150, 100, 50
    ]
}

# Menu
LETTER_TIMER = 0.0625

# Advance Table
ADVANCE_TABLE_TRANSITION_TIMER = 0.75