"""
File: Draw line
Name: Max Huang
-------------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked


SIZE = 10

click = start_x = start_y = end_x = end_y = 0

window = GWindow(width=800, height=400, title='DrawLine')


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw_line)


def draw_line(mouse):
    global click, start_x, start_y, end_x, end_y
    click += 1
    point = GOval(SIZE, SIZE)
    window.add(point, x=mouse.x - SIZE / 2, y=mouse.y - SIZE / 2)  # Add a point at random place first.
    if click % 2 == 1:  # It's odd, means the user's first click.
        start_x = mouse.x  # Recorded the first point of the line.
        start_y = mouse.y
    else:  # It's even, means the user's second click.
        end_x = mouse.x  # Recorded the end point of the line.
        end_y = mouse.y
        line = GLine(start_x, start_y, end_x, end_y)
        window.add(line)
        original = window.get_object_at(start_x - SIZE / 2, start_y)  # Get first point's location then remove it.
        window.remove(original)
        window.remove(point)
        start_x = start_y = end_x = end_y = 0  # The restart to zero so the user can draw a new line.


if __name__ == "__main__":
    main()
