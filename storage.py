# Michael DeVito II
# storage.py
# All variables and objects necessary for archery.py

from graphics import *

currentDirectory = os.path.dirname(__file__)
center = Point(250,250)
score = 0
rounds = 3
targetSize = "Medium"
defaultBackgroundColor = "light green"
target = Image(center, (os.path.join(currentDirectory,"images/target.png")))
win = GraphWin("Archery Game", 500, 500)
win.setCoords(0,0,500,500)
openingText = Text(Point(250,450), "Theresa's Archery Game")
openingText.setSize(30)
startButton = Rectangle(Point(150,150),Point(350,250))
startButton.setFill("light green")
startText = Text(Point(250, 200), "Click to Start")
startText.setFill("Black")
settingsButton = Rectangle(Point(150,75),Point(350,125))
settingsButton.setFill("gray")
settingsText = Text(Point(250,100),"Settings/How-To-Play")
settingsText.setFill("Black")
startCountdownText = Text(Point(250,300), "Begin in ... 5")
startCountdownText.setSize(30)
startCountdownText.setFill("Black")
timerSquare = Rectangle(Point(450,450), Point(500,500))
timerSquare.setFill("Brown")
timerCountdown = Text(Point(470.5, 470.5), "0")
timerCountdown.setFill("White")
timerCountdown.setSize(25)
timeout = 5  # default timer, can change
arrows = dict()
for i in range(1,rounds+1):
    arrows[i] = Image(Point(i * 20,480), (os.path.join(currentDirectory,"images/arrow.png"))) # might need to make arrow.png larger