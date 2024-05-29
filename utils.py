import pygame
from constants import WHITE, FONT, SCREEN_HEIGHT, HUD_HEIGHT, GRAY

def draw_score_and_lives(screen, score, lives):
    score_text = FONT.render(f'Score: {score}', True, WHITE)
    lives_text = FONT.render(f'Lives: {lives}', True, WHITE)
    screen.blit(score_text, (10, SCREEN_HEIGHT - HUD_HEIGHT + 10))
    screen.blit(lives_text, (screen.get_width() - 100, SCREEN_HEIGHT - HUD_HEIGHT + 10))

def draw_game_over(screen):
    game_over_text = FONT.render('Game Over! Press R to Restart', True, WHITE)
    screen.blit(game_over_text, (screen.get_width() // 2 - game_over_text.get_width() // 2, screen.get_height() // 2))

def draw_bricks(screen, bricks):
    for brick in bricks:
        pygame.draw.rect(screen, brick['color'], brick['rect'])
        pygame.draw.rect(screen, WHITE, brick['rect'], 2)  # Outline

def draw_hud(screen):
    pygame.draw.rect(screen, GRAY, pygame.Rect(0, SCREEN_HEIGHT - HUD_HEIGHT, screen.get_width(), HUD_HEIGHT))
