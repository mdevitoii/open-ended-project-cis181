# Michael DeVito
# archery.py
# An archery program designed for Theresa
# Version 1.0

import time, math, os
from graphics import *
from settings import *

def defineAll(): # Initialize EVERYTHING
    global openingText, startButton, startText, settingsButton, settingsText, startCountdownText, timerCountdown, timerSquare, center, timeout, target, score, currentDirectory, win, arrows
    currentDirectory = os.path.dirname(__file__)
    center = Point(250,250)
    score = 0
    target = Image(center, (os.path.join(currentDirectory,"images/target.png")))
    win = GraphWin("Archery Game", 500, 500)
    win.setCoords(0,0,500,500)
    win.setBackground("green")
    win.setBackground("light blue")
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

def settingsScreen():
    backButton.draw(win)
    backText.draw(win)
    htpButton.draw(win)
    htpText.draw(win)

    while True:
        try:
            mouse = win.getMouse()
            x = int(mouse.getX())
            y = int(mouse.getY())
            if (x >= 150) & (x <= 350):
                if (y>=75) & (y<=125):
                    buttonClicked = "GoBack"
                    break
                if (y>=400) & (y<=450):
                    buttonClicked = "HTP"
                    break
            
        except GraphicsError:
            win.close()
            print("Window closed prematurely.")
            break
    
    try:
        if buttonClicked == "GoBack":
            win.close()
            main()
        if buttonClicked == "HTP":
            clear()
            htpScreen()


    except:
        print("Something went wrong! Exit code: GOBACK win.close")

def htpScreen():
    win.setBackground("light yellow")
    

def clear(): # clears the window
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
    clear(win)

def pointCalculation(click):
    global score
    # print(f"Mouse was clicked at ({click.x}, {click.y})") # troubeshooting only
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
    # print(f'dist x = {distanceX}')
    # print(f'dist y = {distanceY}')
    distanceX, distanceY = int(distanceX), int(distanceY)
    distance = math.sqrt((x - targetX)**2 + (y - targetY)**2)
    # print(f'Distance from center: {distance}')

    # Get the width of the target image to calculate its radius
    imgWidth = target.getWidth()
    radius = imgWidth/2

    # Calculate the distance ratio
    distance_ratio = distance/radius
    
    # Use distance ratio to determine the score
    if 0.9 < distance_ratio <= 1.0:
        print("You hit White1! +1 point")
        score += 1
    elif 0.8 < distance_ratio <= 0.9:
        print("You hit White2! +2 points")
        score += 2
    elif 0.7 < distance_ratio <= 0.8:
        print("You hit Black1! +3 points")
        score += 3
    elif 0.6 < distance_ratio <= 0.7:
        print("You hit Black2! +4 points")
        score += 4
    elif 0.5 < distance_ratio <= 0.6:
        print("You hit Blue1! +5 points")
        score += 5
    elif 0.4 < distance_ratio <= 0.5:
        print("You hit Blue2! +6 point")
        score += 6
    elif 0.3 < distance_ratio <= 0.4:
        print("You hit Red1! +7 points")
        score += 7
    elif 0.2 < distance_ratio <= 0.3:
        print("You hit Red2! +8 points")
        score += 8
    elif 0.1 < distance_ratio <= 0.2:
        print("You hit Yellow1! +9 points")
        score += 9
    elif 0.0 < distance_ratio <= 0.1:
        print("You hit Bullseye! +10 points")
        score += 10
    return score

def game(): # 1 round of game
    global score
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
    openingText.draw(win)
    startButton.draw(win)
    startText.draw(win)
    settingsButton.draw(win)
    settingsText.draw(win)
    buttonClicked = ""
    
    # checks what option the user chooses and sends them to desired option
    while True:
        try:
            mouse = win.getMouse()
            x = int(mouse.getX())
            y = int(mouse.getY())
            if (x >= 150) & (x <= 350):
                if (y >= 150) & (y <= 250):
                    buttonClicked = "Start"
                    break
                elif (y>=75) & (y<=125):
                    buttonClicked = "Settings"
                    break
            
        except GraphicsError:
            win.close()
            print("Window closed prematurely.")
            break

    try:
        if buttonClicked == "Start":
            win.setBackground("light green")
            clear()
            countToStart()
            timerSquare.draw(win)
            timerCountdown.draw(win)
            target.draw(win)
            for i in arrows:
                arrows[i].draw(win)
            for i in range(1,rounds+1):
                game()
                arrows[i].undraw() 
            print(f"Your final score is: {score}\nClick to Quit.")
            clear()
        elif buttonClicked == "Settings":
            win.setBackground("light gray")
            clear()
            settingsScreen()

    except:
        print("Something went wrong. Please try again!")
      
    
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
    # Show a visual of how many shots left DONE
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
# - Also used Copilot for help with distance_ratio
# - https://stackoverflow.com/questions/45517677/graphics-py-how-to-clear-the-window
# - https://stackoverflow.com/questions/7165749/open-file-in-a-relative-location-in-python 
# - https://improveyourarchery.com/target-size-calculator/ this might be useful