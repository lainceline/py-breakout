import pygame
import sys

# Initialize pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Breakout Clone')

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Paddle
paddle_width = 100
paddle_height = 10
paddle_speed = 7
paddle = pygame.Rect((screen_width // 2) - (paddle_width // 2), screen_height - 30, paddle_width, paddle_height)

# Ball
ball_radius = 10
ball_speed_x = 5
ball_speed_y = -5
ball = pygame.Rect(screen_width // 2, screen_height // 2, ball_radius * 2, ball_radius * 2)

# Bricks
brick_rows = 5
brick_cols = 10
brick_width = screen_width // brick_cols
brick_height = 30
bricks = [pygame.Rect(col * brick_width, row * brick_height, brick_width, brick_height) for row in range(brick_rows) for
          col in range(brick_cols)]


def main():
    # Main game loop
    running = True
    clock = pygame.time.Clock()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

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
                break

        # Ball falls below paddle
        if ball.bottom >= screen_height:
            ball.x, ball.y = screen_width // 2, screen_height // 2
            ball_speed_y *= -1

        # Drawing everything
        screen.fill(BLACK)
        pygame.draw.rect(screen, BLUE, paddle)
        pygame.draw.ellipse(screen, WHITE, ball)
        for brick in bricks:
            pygame.draw.rect(screen, RED, brick)

        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
