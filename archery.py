# Michael DeVito
# archery.py
# An archery program designed for Theresa
# Version 1.0

import time, math, os, settings
from graphics import *

def defineAll(): # Initialize EVERYTHING
    global openingText, startButton, startText, startCountdownText, timerCountdown, timerSquare, center, timeout, rounds, target, score, currentDirectory, win
    currentDirectory = os.path.dirname(__file__)
    center = Point(250,250)
    score = 0
    rounds = 3
    target = Image(center, (os.path.join(currentDirectory,"images/target.png")))
    win = GraphWin("Archery Game", 500, 500)
    win.setCoords(0,0,500,500)
    win.setBackground("green")
    win.setBackground("light blue")
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
    timeout = 5  # default timer, can change

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
    print(f"Mouse was clicked at ({click.x}, {click.y})") # troubeshooting only
    # the following 4 lines might be replaced with an image drawing that shows an arrow in the target. idk maybe
    x,y = round(click.x,0), round(click.y,0)
    spotClicked = Point(x,y)
    spotClicked.setFill("black")
    spotClicked.draw(win) # this line ends the code that may be replaced
    targetCenter = target.getAnchor()
    targetX = targetCenter.getX()
    targetY = targetCenter.getY()
    distanceX = abs(x - targetX)
    distanceY = abs(y - targetY)
    print(f'dist x = {distanceX}')
    print(f'dist y = {distanceY}')
    distanceX, distanceY = int(distanceX), int(distanceY)
    distance = math.sqrt((x - targetX)**2 + (y - targetY)**2)
    print(distance)
    distance = int(distance)
    if distance <= 200 and distance >= 181:
        print("white1, 1 point")
    elif distance <= 180 and distance >= 161:
        print("white2, 2 points")
    elif distance <= 160 and distance >= 141:
        print("black1, 3 points")
    elif distance <= 140 and distance >= 121:
        print("black2, 4 points")
    elif distance <= 120 and distance >= 101:
        print("blue1, 5 points")
    elif distance <= 100 and distance >= 81:
        print("blue2, 6 points")
    elif distance <= 80 and distance >= 61:
        print("red1, 7 points")
    elif distance <= 60 and distance >= 41:
        print("red2, 8 points")
    elif distance <= 40 and distance >= 21:
        print("yellow1, 9 points")
    elif distance <= 20 and distance >= 10:
        print("yellow2, 10 points")
    elif distance <= 9 and distance >= 0:
        print("bullseye! 10 points")




    


def game(): # 1 round of game
    timerCountdown.setText(timeout) # sets timer text to timeout time 
    time.sleep(0.5)
    start_time = time.time()
    click = None
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

def main(): # main method
    defineAll()
    '''
    openingText.draw(win)
    startButton.draw(win)
    startText.draw(win)
    arrows = dict()
    rounds = 3
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
    '''
    rounds = 20
    timerSquare.draw(win)
    timerCountdown.draw(win)
    target.draw(win)
    for i in range(1,rounds+1):
        game()
        # arrows[i].undraw() UNCOMMENT
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