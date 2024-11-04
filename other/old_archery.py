# Michael DeVito
# archery.py
# An archery program designed for Theresa
# Version 1.0


# Note: THIS VERSION HAS BEEN ARCHIVED.
# A new version can be found at my github
# https://github.com/mdevitoii/open-ended-project-cis181 



import time
import math
from graphics import *
import settings

# Initialize the window
win = GraphWin("Archery Game", 500, 500)
win.setCoords(0,0,50,50)
win.setBackground("green")

# Initialize all archery objects
openingText = Text(Point(25,45), "Theresa's Archery Game")
openingText.setSize(30)
startButton = Rectangle(Point(15,15),Point(35,25))
startButton.setFill("light green")
startText = Text(Point(25, 20), "Click to Start")
startText.setFill("Black")
startCountdownText = Text(Point(25,30), "Begin in ... 5")
startCountdownText.setSize(30)
startCountdownText.setFill("Black")
timerSquare = Rectangle(Point(45,45), Point(50,50))
timerSquare.setFill("Brown")
timerCountdown = Text(Point(47.5, 47.5), "0")
timerCountdown.setFill("White")
timerCountdown.setSize(25)
center = Point(25,25)
white1 = Circle(center,19.5)
white1.setFill("white")
white1.setOutline("black")
white2 = Circle(center,17.5)
white2.setFill("white")
white2.setOutline("black")
black1 = Circle(center,15.5)
black1.setFill("black")
black1.setOutline("white")
black2 = Circle(center,13.5)
black2.setFill("black")
black2.setOutline("white")
blue1 = Circle(center,11.5)
blue1.setFill("light blue")
blue1.setOutline("black")
blue2 = Circle(center,9.5)
blue2.setFill("light blue")
blue2.setOutline("black")
red1 = Circle(center,7.5)
red1.setFill("red")
red1.setOutline("black")    
red2 = Circle(center,5.5)
red2.setFill("red")
red2.setOutline("black")
yellow1 = Circle(center,3.5)
yellow1.setFill("yellow")
yellow1.setOutline("black")
bull = Circle(center,1.5)
bull.setFill("yellow")
bull.setOutline("black")

# initialize other variables
timeout = 5  # default timer, can change
score = 0
rounds = 3

# initialize sprites (images)
arrows = dict()
for i in range(1,rounds+1):
    arrows[i] = Image(Point(i * 2,45), "images/arrow.png")

def is_inside_circle(click_point, circle): # checks if a clicked point is inside a circle
    circle_center = circle.getCenter()
    radius = circle.getRadius()
    distance = math.sqrt((click_point.x - circle_center.x)**2 + (click_point.y - circle_center.y)**2)
    return distance <= radius

def drawTarget(): # function to draw target
    white1.draw(win)
    white2.draw(win)
    black1.draw(win)
    black2.draw(win)
    blue1.draw(win)
    blue2.draw(win)
    red1.draw(win)
    red2.draw(win)
    yellow1.draw(win)
    bull.draw(win)
    for i in range(1,rounds+1):
        arrows[i].draw(win)

def undrawTarget():
    white1.undraw()
    white2.undraw()
    black1.undraw()
    black2.undraw()
    blue1.undraw()
    blue2.undraw()
    red1.undraw()
    red2.undraw()
    yellow1.undraw()
    bull.undraw()

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

def main():
    # Welcome screen
    win.setBackground("light blue")
    openingText.draw(win)
    startButton.draw(win)
    startText.draw(win)
    while True:
        try:
            mouse = win.getMouse()
            x = int(mouse.getX())
            y = int(mouse.getY())
            if (x >= 15) & (x <= 35):
                if (y >= 15) & (y <= 25):
                    break
        except GraphicsError:
            win.close()
            print("Window closed prematurely.")
            break
    try:
        win.setBackground("light green")
        openingText.undraw()
        startText.undraw()
        startButton.undraw()
        countToStart()
        drawTarget()
        timerSquare.draw(win)
        timerCountdown.draw(win)
        global rounds
        for i in range(1,rounds+1):
            game()
            arrows[i].undraw()
    except:
        print("Something went wrong. Please try again!")

    # undrawTarget()
    

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
        print(f"Mouse was clicked at ({click.x}, {click.y})")
        x,y = round(click.x,0), round(click.y,0)
        spotClicked = Point(x,y)
        spotClicked.setFill("black")
        spotClicked.draw(win)
        if is_inside_circle(click,bull) == True:
            print("Bullseye! +10 Points")
            score += 10
        elif is_inside_circle(click,yellow1) == True:
            print("Hit! +9 Points")
            score += 9
        elif is_inside_circle(click,red2) == True:
            print("Hit! +8 Points")
            score += 8
        elif is_inside_circle(click,red1) == True:
            print("Hit! +7 Points")
            score += 7
        elif is_inside_circle(click,blue2) == True:
            print("Hit! +6 Points")
            score += 6
        elif is_inside_circle(click,blue1) == True:
            print("Hit! +5 Points")
            score += 5
        elif is_inside_circle(click,black2) == True:
            print("Hit! +4 Points")
            score += 4
        elif is_inside_circle(click,black1) == True:
            print("Hit! +3 Points")
            score += 3
        elif is_inside_circle(click,white2) == True:
            print("Hit! +2 Points")
            score += 2
        elif is_inside_circle(click,white1) == True:
            print("Hit! +1 Point")
            score += 1
        else:
            print("Miss! No point change.")
    else:
        print("Program was not clicked in time")


    
        
                
# run the program!
if __name__ == "__main__":
    main()

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

# - Used Copilot for help with timer
# - stole distance function directly from Copilot