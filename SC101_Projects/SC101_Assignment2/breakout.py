"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3			# Number of attempts


def main():
    graphics = BreakoutGraphics()
    # Add the animation loop here!
    vx = graphics.get_dx()  # Set start x velocity of the game.
    vy = graphics.get_dy()  # Set start y velocity of the game.
    live = NUM_LIVES        # Lives you have to play.
    bricks_number = graphics.brick_rows * graphics.brick_cols  # Total number of bricks, aim to remove all!
    while True:
        pause(FRAME_RATE)
        if live <= 0:  # When all lives is used, game over.
            break
        if graphics.is_moving and bricks_number != 0:  # When all bricks is removed, game over.
            graphics.ball.move(vx, vy)
            # Get four corner of the ball.
            top_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y)
            top_right = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width, graphics.ball.y)
            bottom_left = graphics.window.get_object_at(graphics.ball.x, graphics.ball.y + graphics.ball.height)
            bottom_right = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width,
                                                         graphics.ball.y + graphics.ball.height)
            if top_left is not None:
                if top_left == graphics.paddle:
                    graphics.back_to_paddle()
                    vy = -vy
                else:
                    graphics.window.remove(top_left)
                    bricks_number -= 1
                    vy = -vy
            elif top_right is not None:
                if top_right == graphics.paddle:
                    graphics.back_to_paddle()
                    vy = -vy
                else:
                    graphics.window.remove(top_right)
                    bricks_number -= 1
                    vy = -vy
            elif bottom_left is not None:
                if bottom_left == graphics.paddle:
                    graphics.back_to_paddle()
                    vy = -vy
                else:
                    graphics.window.remove(bottom_left)
                    bricks_number -= 1
                    vy = -vy
            elif bottom_right is not None:
                if bottom_right == graphics.paddle:
                    graphics.back_to_paddle()
                    vy = -vy
                else:
                    graphics.window.remove(bottom_right)
                    bricks_number -= 1
                    vy = -vy
            # If touch to right or left wall, ball will bounce.
            if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                vx = -vx
            # When touch to top, ball will bounce.
            if graphics.ball.y <= 0:
                vy = -vy
            # When ball go under bottom, lose one live and start again when click.
            if graphics.ball.y > graphics.window.height:
                live -= 1
                graphics.is_moving = False
                graphics.ball.x = (graphics.window.width - graphics.ball.width) / 2
                graphics.ball.y = (graphics.window.height - graphics.ball.height) / 2


if __name__ == '__main__':
    main()
