import unittest
import pygame
from game import BreakoutGame
from constants import SCREEN_WIDTH, PADDLE_SPEED

class TestBreakout(unittest.TestCase):
    
    def setUp(self):
        self.game = BreakoutGame()
        self.game.reset_game()
        self.paddle, self.ball, self.bricks, self.ball_speed_x, self.ball_speed_y = self.game.get_game_state()
    
    def test_paddle_movement_left(self):
        initial_left = self.paddle.left
        keys = {pygame.K_LEFT: True, pygame.K_RIGHT: False}
        self._simulate_keypress(keys)
        self.assertEqual(self.paddle.left, max(0, initial_left - PADDLE_SPEED))
    
    def test_paddle_movement_right(self):
        initial_right = self.paddle.right
        keys = {pygame.K_LEFT: False, pygame.K_RIGHT: True}
        self._simulate_keypress(keys)
        self.assertEqual(self.paddle.right, min(SCREEN_WIDTH, initial_right + PADDLE_SPEED))
    
    def test_ball_collision_with_paddle(self):
        self.ball.x = self.paddle.x + self.paddle.width // 2
        self.ball.y = self.paddle.y - self.ball.height
        self._simulate_ball_movement()
        
        self.assertLess(self.ball_speed_y, 0)
    
    def test_ball_collision_with_wall(self):
        self.ball.x = 0
        self.ball_speed_x = -5
        self._simulate_ball_movement()
        
        self.assertGreater(self.ball_speed_x, 0)
    
    def test_ball_collision_with_brick(self):
        brick = self.bricks[0]
        self.ball.x = brick['rect'].x + brick['rect'].width // 2
        self.ball.y = brick['rect'].y + brick['rect'].height // 2
        self._simulate_ball_movement()
        
        self.assertNotIn(brick, self.bricks)
    
    def _simulate_keypress(self, keys):
        pygame.key.get_pressed = lambda: keys
        if keys.get(pygame.K_LEFT):
            if self.paddle.left > 0:
                self.paddle.left -= PADDLE_SPEED
        if keys.get(pygame.K_RIGHT):
            if self.paddle.right < SCREEN_WIDTH:
                self.paddle.right += PADDLE_SPEED

    def _simulate_ball_movement(self):
        self.ball.x += self.ball_speed_x
        self.ball.y += self.ball_speed_y
        
        if self.ball.left <= 0 or self.ball.right >= SCREEN_WIDTH:
            self.ball_speed_x *= -1
        if self.ball.top <= 0:
            self.ball_speed_y *= -1
        if self.ball.colliderect(self.paddle):
            self.ball_speed_y *= -1
        
        for brick in self.bricks[:]:
            if self.ball.colliderect(brick['rect']):
                self.ball_speed_y *= -1
                self.bricks.remove(brick)
                break

if __name__ == '__main__':
    unittest.main()
