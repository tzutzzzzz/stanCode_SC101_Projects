"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao.

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing
BRICK_WIDTH = 40       # Height of a brick (in pixels)
BRICK_HEIGHT = 15      # Height of a brick (in pixels)
BRICK_ROWS = 10        # Number of rows of bricks
BRICK_COLS = 10        # Number of columns of bricks
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels)
BALL_RADIUS = 10       # Radius of the ball (in pixels)
PADDLE_WIDTH = 75      # Width of the paddle (in pixels)
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels)
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels)
INITIAL_Y_SPEED = 7    # Initial vertical speed for the ball
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH, paddle_height=PADDLE_HEIGHT,
                 paddle_offset=PADDLE_OFFSET, brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS, brick_width=BRICK_WIDTH,
                 brick_height=BRICK_HEIGHT, brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING, title='Breakout'):
        self.brick_rows = brick_rows
        self.brick_cols = brick_cols
        self.paddle_offset = paddle_offset
        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)
        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle, x=(self.window.width - self.paddle.width) / 2,
                        y=self.window.height - self.paddle.height - self.paddle_offset)
        # Center a filled ball in the graphical window
        self.ball = GOval(ball_radius * 2, ball_radius * 2)
        self.ball.filled = True
        self.window.add(self.ball, x=self.window.width / 2 - ball_radius, y=self.window.height / 2 - ball_radius)
        # Default initial velocity for the ball
        self.__dx = random.randint(1, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        if random.random() > 0.5:
            self.__dx = -self.__dx
        # Initialize our mouse listeners
        self.is_moving = False
        onmousemoved(self.reset_paddle)
        onmouseclicked(self.start_game)
        # Draw bricks
        for i in range(self.brick_rows):
            for j in range(self.brick_cols):
                self.brick = GRect(brick_width, brick_height)
                self.brick.filled = True
                self.window.add(self.brick, x=j * (brick_width + brick_spacing),
                                y=brick_offset + i * (brick_height + brick_spacing))
                if i < 2:
                    self.brick.fill_color = 'red'
                elif 2 <= i < 4:
                    self.brick.fill_color = 'orange'
                elif 4 <= i < 6:
                    self.brick.fill_color = 'yellow'
                elif 6 <= i < 8:
                    self.brick.fill_color = 'green'
                else:
                    self.brick.fill_color = 'blue'

    def reset_paddle(self, mouse):
        """
        Paddle will move according to mouse location,
        and paddle's center will always as same as mouse location.
        """
        if mouse.x - self.paddle.width / 2 < 0:
            self.paddle.x = 0
        elif mouse.x + self.paddle.width / 2 > self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        else:
            self.paddle.x = mouse.x - self.paddle.width / 2
        self.paddle.y = self.window.height - self.paddle.height - self.paddle_offset

    def start_game(self, mouse):
        self.is_moving = True

    def back_to_paddle(self):
        """
        When ball move it may go under the paddle but we can't see.
        This function will let the ball move back to the paddle surface.
        """
        back_to_paddle = self.ball.y - (self.window.height - self.paddle_offset - self.paddle.height - self.ball.height)
        self.ball.move(0, -back_to_paddle)

    def get_dx(self):
        return self.__dx

    def get_dy(self):
        return self.__dy
