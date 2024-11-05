# Michael DeVito
# archery.py
# An archery program designed for Theresa
# Version 1.0

import time, math, os
from graphics import *
import settings

# Initialize the window
win = GraphWin("Archery Game", 500, 500)
win.setCoords(0,0,500,500)
win.setBackground("green")

# Initialize all archery objects
openingText = Text(Point(250,450), "Theresa's Archery Game")
openingText.setSize(30)
startButton = Rectangle(Point(150,150),Point(350,250))
startButton.setFill("light green")
startText = Text(Point(200, 200), "Click to Start")
startText.setFill("Black")
startCountdownText = Text(Point(250,300), "Begin in ... 5")
startCountdownText.setSize(30)
startCountdownText.setFill("Black")
timerSquare = Rectangle(Point(450,450), Point(500,500))
timerSquare.setFill("Brown")
timerCountdown = Text(Point(470.5, 470.5), "0")
timerCountdown.setFill("White")
timerCountdown.setSize(25)
center = Point(250,250)
timeout = 5  # default timer, can change
score = 0
rounds = 3

def clear(win): # clears the window
    for item in win.items[:]:
        item.undraw()

def countToStart(): # function for countdown before start
    startCountdownText.draw(win)
    time.sleep(1)
    startCountdownText.setText("Begin in ... 4")
    time.sleep(1)
    startCountdownText.setText("Begin in ... 3")
    time.sleep(1)
    startCountdownText.setText("Begin in ... 2")
    time.sleep(1)
    startCountdownText.setText("Begin in ... 1")
    time.sleep(1)
    startCountdownText.setText("GO!")
    time.sleep(1)
    startCountdownText.undraw()

def pointCalculation(click):
    global target
    print(f"Mouse was clicked at ({click.x}, {click.y})") # troubeshooting only
    # the following 4 lines might be replaced with an image drawing that shows an arrow in the target. idk maybe
    x,y = round(click.x,0), round(click.y,0)
    spotClicked = Point(x,y)
    spotClicked.setFill("black")
    spotClicked.draw(win) # this line ends the code that may be replaced


def game():
    timerCountdown.setText(timeout) # sets timer text to timeout time 
    time.sleep(0.5)
    start_time = time.time()
    click = None
    global score
    while time.time() - start_time < timeout:
        click = win.checkMouse()
        remaining_time = int(timeout - (time.time() - start_time))
        timerCountdown.setText(f"{remaining_time}")
        time.sleep(0.1)
        if click:
            break
    if click:
        pointCalculation(click)
    else:
        print("Program was not clicked in time")

def main():
    # Welcome screen
    win.setBackground("light blue")
    openingText.draw(win)
    startButton.draw(win)
    startText.draw(win)
    currentDirectory = os.path.dirname(__file__)
    target = Image(center, (os.path.join(currentDirectory,"images/target.png")))
    arrows = dict()
    global rounds
    for i in range(1,rounds+1):
        arrows[i] = Image(Point(i * 2,45), (os.path.join(currentDirectory,"images/arrow.png")))



    while True:
        # try:
            mouse = win.getMouse()
            x = int(mouse.getX())
            y = int(mouse.getY())
            if (x >= 150) & (x <= 350):
                if (y >= 150) & (y <= 250):
                    break
        # except GraphicsError:
            # win.close()
            # print("Window closed prematurely.")
            # break
    # try:
    win.setBackground("light green")
    openingText.undraw()
    startText.undraw()
    startButton.undraw()
    countToStart()
    rounds = 3
    timerSquare.draw(win)
    timerCountdown.draw(win)
    target.draw(win)
    for i in range(1,rounds+1):
        game()
        arrows[i].undraw()
    # except:
        # print("Something went wrong. Please try again!")
      
    
# run the program!
if __name__ == "__main__":
    main()


# For Troubleshooting only
try:
    win.getMouse()
except GraphicsError:
    win.close()
    print("Window was closed prematurely")


# Version 1
    # welcome screen DONE
    # draw target DONE
    # 3 shots DONE
    # calculate points DONE
# Version 2 
    # timer DONE
    # 5 shots DONE
    # Show a visual of how many shots left
# Version 3
    # music?
    # wind factor
    # optimize clicking by making cooridnates = screen size (changing scaling)
# Version 4
    # different modes
    # easy, medium, hard concerns target distance (size)
    # all-out mode where you click as many targets as you can within 10 seconds

# REFERENCES:

# - Used Copilot for help with timer and distance function
# - https://stackoverflow.com/questions/45517677/graphics-py-how-to-clear-the-window
# - https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python 
# - https://improveyourarchery.com/target-size-calculator/ this might be useful