import pygame
import pygame.font
from constants import *
from utils import draw_score_and_lives, draw_game_over, draw_bricks, draw_hud

class BreakoutGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Breakout Clone')
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font(None, 36)
        self.reset_game()

    def reset_game(self):
        self.paddle = pygame.Rect((SCREEN_WIDTH // 2) - (PADDLE_WIDTH // 2), GAME_HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)
        self.ball = pygame.Rect(self.paddle.centerx - BALL_RADIUS, self.paddle.top - BALL_RADIUS * 2, BALL_RADIUS * 2, BALL_RADIUS * 2)
        self.bricks = [{'rect': pygame.Rect(col * BRICK_WIDTH, row * BRICK_HEIGHT, BRICK_WIDTH, BRICK_HEIGHT), 'color': BRICK_COLORS[row], 'points': (5 - row) * 10} for row in range(BRICK_ROWS) for col in range(BRICK_COLS)]
        self.score = 0
        self.lives = 3
        self.ball_speed_x = BALL_SPEED_X
        self.ball_speed_y = BALL_SPEED_Y
        self.game_over = False
        self.ball_attached = True

    def get_game_state(self):
        return self.paddle, self.ball, self.bricks, self.ball_speed_x, self.ball_speed_y

    def run(self):
        while self.running:
            self.handle_events()
            if not self.game_over:
                self.update()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if self.game_over and event.key == pygame.K_r:
                    self.reset_game()
                if self.ball_attached and event.key == pygame.K_SPACE:
                    self.ball_attached = False

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.paddle.left > 0:
            self.paddle.left -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and self.paddle.right < SCREEN_WIDTH:
            self.paddle.right += PADDLE_SPEED
    
        if self.ball_attached:
            self.ball.x = self.paddle.centerx - BALL_RADIUS
            self.ball.y = self.paddle.top - BALL_RADIUS * 2
        else:
            self.ball.x += self.ball_speed_x
            self.ball.y += self.ball_speed_y
    
            if self.ball.left <= 0 or self.ball.right >= SCREEN_WIDTH:
                self.ball_speed_x *= -1
                # Add code to modify the x-speed based on certain conditions
                if self.ball_speed_x > 0:
                    self.ball_speed_x += 1
                else:
                    self.ball_speed_x -= 1
            if self.ball.top <= 0:
                self.ball_speed_y *= -1
            if self.ball.colliderect(self.paddle):
                # Add English to the ball based on where it hit the paddle
                paddle_center = self.paddle.left + PADDLE_WIDTH / 2
                hit_position = (self.ball.centerx - paddle_center) / (PADDLE_WIDTH / 2)
                self.ball_speed_x = BALL_SPEED_X * hit_position
            
                # Increase the y-speed based on where the ball hit the paddle
                # The farther from the center, the faster the y-speed
                # Ensure the y-speed does not exceed a maximum value
                if abs(hit_position) > SPEEDUP_THRESHOLD:
                    self.ball_speed_y = min(MAX_BALL_SPEED_Y, abs(self.ball_speed_y * (1 + abs(hit_position))))
                self.ball_speed_y *= -1
    
            for brick in self.bricks[:]:
                if self.ball.colliderect(brick['rect']):
                    self.ball_speed_y *= -1
                    self.score += brick['points']
                    self.bricks.remove(brick)
                    break
    
            if self.ball.bottom >= GAME_HEIGHT:
                self.lives -= 1
                if self.lives == 0:
                    self.game_over = True
                else:
                    self.ball_attached = True
                    self.ball.x, self.ball.y = self.paddle.centerx - BALL_RADIUS, self.paddle.top - BALL_RADIUS * 2
                    self.ball_speed_y = -5
            if not self.bricks:
                self.game_over = True

    def draw(self):
        self.screen.fill(BLACK)
        pygame.draw.rect(self.screen, BLUE, self.paddle)
        pygame.draw.ellipse(self.screen, WHITE, self.ball)
        draw_bricks(self.screen, self.bricks)
        draw_hud(self.screen)
        draw_score_and_lives(self.screen, self.score, self.lives)
        if self.game_over:
            draw_game_over(self.screen)
        pygame.display.flip()

def main():
    game = BreakoutGame()
    game.run()

if __name__ == '__main__':
    main()
