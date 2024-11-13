# Michael DeVito II
# storage.py
# All variables and objects necessary for archery.py

from graphics import *

currentDirectory = os.path.dirname(__file__)
center = Point(250,250)
score = 0
rounds = 3
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
settingsPath = os.path.join(currentDirectory, 'settings.txt') 
with open(settingsPath, 'r') as file:
    data = file.readlines()
defaultBackgroundColor = data[0].replace('\n', "")
targetSize = data[1].replace('\n', "")

### Everything for Settings Screen and How-to-Play Screen
howToPlay = (
    f"Welcome to Archery! A game created by Michael DeVito\n"
    f"Dedicated to Theresa <3\n\n\n"
    f"Archery can be played by either using the arrow keys or the Mouse.\nYou can configure which input you use via the settings screen.\n\n"
    f"The goal is to shoot as close to the center ring as you can.\nThe closer you are, the higher the point value!\n\n"
    f"The game defaults to 3 shots per round with 5 seconds to shoot each shot.\nThese values can be configured via the settings screen.\n\n"
    f"Gameplay too boring? \nTry out the difficulties and different gamemodes in the settings screen!\n\n"
    f"Thank you for playing, and have fun!"
)
backButton = Rectangle(Point(150,75),Point(350,125))
backButton.setFill("gray")
backText = Text(Point(250,100),"Save and Exit")
backText.setFill("Black")
htpButton = Rectangle(Point(150,400),Point(350,450))
htpButton.setFill("Light green")
htpText = Text(Point(250,425), "How to Play")
instructions = Text(Point(250,300),howToPlay)
instructions.setSize(10)
targetSizeText = Text(Point(200,300),"Target Size: (Small, Medium, Large)")
targetSizeEntry = Entry(Point(375,300),8)
targetSizeEntry.setText(targetSize)
defaultColorText = Text(Point(200,275),"Background Color:")
defaultColorEntry = Entry(Point(325,275),10)
defaultColorEntry.setText(defaultBackgroundColor)