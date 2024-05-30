import pygame

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
HUD_HEIGHT = 50
GAME_HEIGHT = SCREEN_HEIGHT - HUD_HEIGHT

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
ORANGE = (255, 165, 0)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GRAY = (169, 169, 169)

# Paddle
PADDLE_WIDTH = 100
PADDLE_HEIGHT = 10
PADDLE_SPEED = 7

# Ball
BALL_RADIUS = 10
BALL_SPEED_X = 5
BALL_SPEED_Y = -5
MIN_BALL_SPEED_Y = 2
SPEEDUP_THRESHOLD = 0.5  # Adjust this value as needed
MAX_BALL_SPEED_Y = 10  # Adjust this value as needed

# Bricks
BRICK_ROWS = 5
BRICK_COLS = 10
BRICK_WIDTH = SCREEN_WIDTH // BRICK_COLS
BRICK_HEIGHT = 30

# Brick colors by row
BRICK_COLORS = [RED, ORANGE, YELLOW, GREEN, BLUE]

# Font
pygame.font.init()
FONT = pygame.font.SysFont('Arial', 24)
