# Michael DeVito II
# storage.py
# All variables and objects necessary for archery.py

from graphics import *

win = GraphWin("Archery Game", 500, 500)
win.setCoords(0,0,500,500)
target = Image(Point(250,250), (os.path.join(os.path.dirname(__file__),"images/target.png")))
startCountdownText = Text(Point(250,300), "Begin in ... 5")
startCountdownText.setSize(30)
startCountdownText.setFill("Black")
timerSquare = Rectangle(Point(450,450), Point(500,500))
timerSquare.setFill("Brown")
timerCountdown = Text(Point(470.5, 470.5), "0")
timerCountdown.setFill("White")
timerCountdown.setSize(25)
timeout = 5  # default timer, can change

