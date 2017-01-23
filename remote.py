import curses
import os

screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)
screen.addstr("Hello World!!!")
screen.nodelay(1)
screen.refresh()

while True:
    c = screen.getch()
    screen.refresh()
    if c == curses.KEY_RIGHT:
        os.system("DISPLAY=:0 xdotool key space")
        print "right"
    if c == curses.KEY_LEFT:
        os.system("DISPLAY=:0 xdotool key Left")
        print "left"

curses.endwin()
