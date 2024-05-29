import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
hud_height = 50
game_height = screen_height - hud_height
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Breakout Clone')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (169, 169, 169)

# Paddle
paddle_width = 100
paddle_height = 10
paddle_speed = 7

# Ball
ball_radius = 10
ball_speed_x = 5
ball_speed_y = -5

# Bricks
brick_rows = 5
brick_cols = 10
brick_width = screen_width // brick_cols
brick_height = 30

# Score and Lives
score = 0
lives = 3
font = pygame.font.SysFont('Arial', 24)

# Game state
game_over = False

# Define game objects at the module level
paddle = None
ball = None
bricks = []


def reset_game():
    global paddle, ball, bricks, score, lives, ball_speed_x, ball_speed_y, game_over
    paddle = pygame.Rect((screen_width // 2) - (paddle_width // 2), game_height - 30, paddle_width, paddle_height)
    ball = pygame.Rect(screen_width // 2, game_height // 2, ball_radius * 2, ball_radius * 2)
    bricks = [pygame.Rect(col * brick_width, row * brick_height, brick_width, brick_height) for row in range(brick_rows)
              for col in range(brick_cols)]
    score = 0
    lives = 3
    ball_speed_x = 5
    ball_speed_y = -5
    game_over = False


def get_game_state():
    return paddle, ball, bricks, ball_speed_x, ball_speed_y


def draw_score_and_lives():
    score_text = font.render(f'Score: {score}', True, WHITE)
    lives_text = font.render(f'Lives: {lives}', True, WHITE)
    screen.blit(score_text, (10, screen_height - hud_height + 10))
    screen.blit(lives_text, (screen_width - 100, screen_height - hud_height + 10))


def draw_game_over():
    game_over_text = font.render('Game Over! Press R to Restart', True, WHITE)
    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2))


def main():
    global score, lives, ball_speed_x, ball_speed_y, game_over

    # Main game loop
    running = True
    clock = pygame.time.Clock()

    reset_game()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and game_over and event.key == pygame.K_r:
                reset_game()

        if not game_over:
            # Paddle movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and paddle.left > 0:
                paddle.left -= paddle_speed
            if keys[pygame.K_RIGHT] and paddle.right < screen_width:
                paddle.right += paddle_speed

            # Ball movement
            ball.x += ball_speed_x
            ball.y += ball_speed_y

            # Ball collision with walls
            if ball.left <= 0 or ball.right >= screen_width:
                ball_speed_x *= -1
            if ball.top <= 0:
                ball_speed_y *= -1
            if ball.colliderect(paddle):
                ball_speed_y *= -1

            # Ball collision with bricks
            for brick in bricks[:]:
                if ball.colliderect(brick):
                    ball_speed_y *= -1
                    bricks.remove(brick)
                    score += 10  # Update score
                    break

            # Ball falls below paddle
            if ball.bottom >= game_height:
                lives -= 1
                if lives == 0:
                    game_over = True  # Set game over state
                else:
                    ball.x, ball.y = screen_width // 2, game_height // 2
                    ball_speed_y *= -1

        # Drawing everything
        screen.fill(BLACK)

        # Draw game area
        pygame.draw.rect(screen, BLACK, pygame.Rect(0, 0, screen_width, game_height))
        pygame.draw.rect(screen, BLUE, paddle)
        pygame.draw.ellipse(screen, WHITE, ball)
        for brick in bricks:
            pygame.draw.rect(screen, RED, brick)

        # Draw HUD area
        pygame.draw.rect(screen, GRAY, pygame.Rect(0, game_height, screen_width, hud_height))
        draw_score_and_lives()  # Draw the score and lives

        if game_over:
            draw_game_over()  # Draw the game over text

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
