"""
File: My drawing
Name: Max Huang
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GArc, GPolygon, GLine, GLabel
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Minion is cute.
    Minion is short, minion is dumb.
    And minion helps Gru fight bad people.
    """
    window = GWindow(width=800, height=400, title='Minion')
    top = GArc(200, 200, 0, 180)
    top.filled = True
    top.fill_color = 'yellow'
    top.color = 'yellow'
    window.add(top, x=(window.width-top.width)/2, y=window.height/2-170)
    middle = GRect(200, 200)
    middle.filled = True
    middle.fill_color = 'yellow'
    middle.color = 'yellow'
    window.add(middle, x=(window.width-middle.width)/2, y=window.height/2-125)
    button = GArc(200, 200, 0, -180)
    button.filled = True
    button.fill_color = 'navy'
    button.color = 'navy'
    window.add(button, x=(window.width-button.width)/2, y=window.height/2+25)
    eye = GOval(100, 100)
    eye.filled = True
    eye.fill_color = 'white'
    window.add(eye, x=(window.width-eye.width)/2, y=window.height/2-125)
    pupil = GOval(50, 50)
    pupil.filled = True
    window.add(pupil, x=(window.width-pupil.width)/2, y=window.height/2-100)
    glass_l = GRect(50, 20)
    glass_l.filled = True
    window.add(glass_l, x=window.width/2-glass_l.width*2, y=window.height/2-85)
    glass_r = GRect(50, 20)
    glass_r.filled = True
    window.add(glass_r, x=window.width / 2 + glass_r.width, y=window.height/2-85)
    mouth = GArc(100, 50, 0, -180)
    mouth.filled = True
    mouth.fill_color = 'pink'
    window.add(mouth, x=(window.width-mouth.width)/2, y=window.height/2-15)
    cloths = GRect(150, 50)
    cloths.filled = True
    cloths.fill_color = 'navy'
    cloths.color = 'navy'
    window.add(cloths, x=(window.width-cloths.width)/2, y=window.height/2+40)
    leg_l = GRect(30, 40)
    leg_l.filled = True
    leg_l.fill_color = 'navy'
    leg_l.color = 'navy'
    window.add(leg_l, x=window.width/2+15, y=window.height/2+120)
    leg_r = GRect(30, 40)
    leg_r.filled = True
    leg_r.fill_color = 'navy'
    leg_r.color = 'navy'
    window.add(leg_r, x=window.width/2-45, y=window.height/2+120)
    hand_l = GRect(90, 12)
    hand_l.filled = True
    hand_l.fill_color = 'yellow'
    hand_l.color = 'yellow'
    window.add(hand_l, x=210, y=180)
    hand_r1 = GPolygon()
    hand_r1.add_vertex((500, 180))
    hand_r1.add_vertex((500, 195))
    hand_r1.add_vertex((550, 235))
    hand_r1.add_vertex((550, 220))
    hand_r1.filled = True
    hand_r1.fill_color = 'yellow'
    hand_r1.color = 'yellow'
    window.add(hand_r1)
    hand_r2 = GPolygon()
    hand_r2.add_vertex((550, 220))
    hand_r2.add_vertex((550, 235))
    hand_r2.add_vertex((500, 275))
    hand_r2.add_vertex((500, 260))
    hand_r2.filled = True
    hand_r2.fill_color = 'yellow'
    hand_r2.color = 'yellow'
    window.add(hand_r2)
    palm_l = GOval(35, 30)
    palm_l.filled = True
    window.add(palm_l, x=185, y=165)
    finger = GArc(15, 100, 0, 180)
    finger.filled = True
    window.add(finger, x=205, y=150)
    palm_r = GOval(35, 30)
    palm_r.filled = True
    window.add(palm_r, x=500, y=250)
    feet_l = GArc(200, 70, 0, 90)
    feet_l.filled = True
    window.add(feet_l, x=365, y=355)
    feet_r = GArc(200, 70, 90, 90)
    feet_r.filled = True
    window.add(feet_r, x=335, y=355)
    hair1 = GLine(380, 30, 360, 0)
    window.add(hair1)
    hair2 = GLine(400, 30, 400, 0)
    window.add(hair2)
    hair3 = GLine(420, 30, 440, 0)
    window.add(hair3)
    symbol = GLabel('G')
    symbol.font = '-45'
    window.add(symbol, 380, 300)


if __name__ == '__main__':
    main()
