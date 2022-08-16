"""
File: Bouncing ball
Name: Max Huang
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval
from campy.graphics.gwindow import GWindow
from campy.gui.events.timer import pause
from campy.gui.events.mouse import onmouseclicked

VX = 3
VY = 0
DELAY = 10
GRAVITY = 1
SIZE = 20
REDUCE = 0.9
START_X = 30
START_Y = 40
click = 0

ball = GOval(SIZE, SIZE)

window = GWindow(800, 500, title='bouncing_ball.py')


def main():
    """
    This program simulates a bouncing ball at (START_X, START_Y)
    that has VX as x velocity and 0 as y velocity. Each bounce reduces
    y velocity to REDUCE of itself.
    """
    window.add(ball, x=START_X, y=START_Y)
    onmouseclicked(bouncing_ball)


def bouncing_ball(mouse):
    global VY, click
    if click == 0:  # First click of mouse will start bouncing.
        while True:
            click += 1  # Turn off the switch because click will never be zero again.
            VY += GRAVITY  # Y velocity will go faster according to GRAVITY.
            ball.move(VX, VY)
            if ball.y + SIZE - window.height >= 0:
                VY = -VY * REDUCE
                back_to_floor = ball.y - (window.height - SIZE)  # When bouncing, ball would have dropped to the floor.
                ball.move(0, -back_to_floor)  # Make the ball back to floor first or it will continue to time REDUCE.
            pause(DELAY)
            if ball.x - window.width > 0:  # Ball is bouncing out the window then break while loop.
                break
        window.add(ball, x=START_X, y=START_Y)  # Add a ball at start position.


if __name__ == "__main__":
    main()
