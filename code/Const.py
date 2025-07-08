# E
import pygame

# C
C_LIGHT_BLUE = (180, 180, 200)
C_BRIGHT_RED = (200, 50, 50)
C_ORANGE = (255, 128, 0)
C_WHITE = (255, 255, 255)
C_YELLOW = (255, 255, 0)
C_GREEN = (0, 128, 0)
C_CYAN = (0, 128, 128)
C_RED = (120, 6, 6)
C_BLACK = (0, 0, 0)

ENTITY_SPEED = {
    'LevelBg0': 0,
    'LevelBg1': 1,
    'LevelBg2': 2,
    'LevelBg3': 3,
    'Obstacle0': 4,
    'Obstacle1': 3,
    'Obstacle2': 3,
}

ENTITY_HEALTH = {
    'LevelBg0': 1,
    'LevelBg1': 1,
    'LevelBg2': 1,
    'LevelBg3': 1,
    'Player': 150,
    'Obstacle0': 1,
    'Obstacle1': 1,
    'Obstacle2': 1
}

ENTITY_DAMAGE = {
    'Player': 0,
    'Obstacle0': 40,
    'Obstacle1': 30,
    'Obstacle2': 20
}

ENTITY_POINTS = {
    'Obstacle0': 50,
    'Obstacle1': 30,
    'Obstacle2': 15
}

EVENT_OBSTACLE = pygame.USEREVENT + 1

# G
GAME_FONT = 'Rockwell Condensed'

# M
MENU_OPTIONS = (
    'NEW GAME',
    'LEADERBOARD',
    'EXIT'
)

# S
SPAWN_TIME = 2000

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324
