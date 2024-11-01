# Michael DeVito II
# settings.py
# Settings screen for Archery game
# Also might store future settings (ex: # of rounds, wind enable/disable, etc.)

from graphics import *

def drawScreen(win):
    settingsText = Text(Point(25,45), "Settings")
    settingsText.draw(win)