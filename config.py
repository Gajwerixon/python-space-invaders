import pygame

# SCREEN
WIDTH, HEIGHT = 672, 768

# COLORS
GREEN = (0, 230, 0)

# FONT
FONT_SIZE = 25

# TOP HUD
TOP_HUD = {
    'height': 110,
    'margin_x': 30,
    'margin_y': 20,
    'score_padding': 10,
}

# BOTTOM HUD
BOTTOM_HUD = {
    'height': 60,
    'margin_x': 100,
    'padding_y': 10,
    'ship_size': (36, 24),
    'ship_offset': 45,
}

# PLAY AREA
PLAY_AREA = pygame.Rect(
    0, 
    TOP_HUD['height'],
    WIDTH,
    HEIGHT - TOP_HUD['height'] - BOTTOM_HUD['height']
)

# PLAYER
PLAYER = {
    'size': (36, 24),
    'speed': 150,
    'start_x': 80,
    'start_y_offset': 54 
}

# SHIELDS
SHIELDS = {
    'count': 4,
    'spacing': 144,
    'block_size': (3, 3),
    'shape': [[0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0],
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
}

# LINES
LINES = {
    'count': 224,
    'size': (3, 3),
}

# PLAYER BULLETS
PLAYER_BULLETS = {
    'speed': 578,
    'size': (2, 8),
}

# EXPLOSIONS
EXPLOSIONS = {
    'player_bullet_miss_size': (24, 24),
    'alien_size': (36, 24),
    'alien_bullet_miss_size': (16, 24),

    'line_damage_mask': [1 if i % 2 == 0 else 0 for i in range(LINES['count'])],
    'line_damage_offsets': [-4, -3, -2, -1, 0, 1, 2, 3, 4],

    'shield_cache_shape': {
        'player': [
            (-1, -3), (0, -3), (1, -3),
            (-2, -2), (-1, -2), (0, -2), (1, -2), (2, -2),
            (-3, -1), (-2, -1), (-1, -1), (0, -1), (1, -1), (2, -1),
            (-3, 0), (-2, 0), (-1, 0), (0, 0), (1, 0), (2, 0), (3, 0),
            (-3, 1), (-2, 1), (-1, 1), (0, 1), (1, 1), (2, 1), (3, 1),
            (-2, 2), (-1, 2), (0, 2), (1, 2), (2, 2),
            (0, 3),
        ],
        
        'alien': [
            (-1, 0), (0, 0), (0, 1), 
            (-3, 1), (-1, 1), (0, 1), (1, 1), (3, 1),
            (-2, 2), (-1, 2), (0, 2), (1, 2), (2, 2),
            (-3, 3), (-1, 3), (0, 3), (1, 3), (3, 3),
            (-2, 4), (-1, 4), (0, 4), (1, 4), (2, 4),
            (-3, 5), (-1, 5), (0, 5), (1, 5), (3, 5),
            (-2, 6), (0, 6), (2, 6),
        ],
    },
}

# ALIENS
ALIENS_FORMATION = {
    'num_aliens': 11,
    'layout': ('alien_1', 'alien_1', 'alien_2', 'alien_2', 'alien_3'),
    'scores': {
        'alien_1': 10,
        'alien_2': 20,
        'alien_3': 30,
    },
    'size': (32, 24),
    'spacing': 18,
    'margin': 32,
}

ALIENS_MOVEMENT = {
    "horizontal_step": 8,
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
    'size': (48, 21),
    'dead_size': (48, 21),
    'speed': 128,
    'spawn_timer': 25.6,
    'start_y': PLAY_AREA.top,
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