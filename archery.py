# Michael DeVito
# archery.py
# An archery program designed for Theresa
# Version 1.0

import time, math, os
from graphics import *
from storage import *

def settingsScreen():
    win.setBackground("light gray")
    for o in settingsObjects:
        o.draw(win)
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
    if buttonClicked == "GoBack":
        clear()
        data[0] = defaultColorEntry.getText() + '\n'
        data[1] = targetSizeEntry.getText() + '\n'
        with open(settingsPath, "w") as file:
            file.writelines(data)
        main()
    if buttonClicked == "HTP":
        clear()
        htpScreen()

def htpScreen():
    win.setBackground("light yellow")
    instructions.draw(win)
    backButton.draw(win)
    backText.setText("Go Back")
    backText.draw(win)
    while True:
        try:
            mouse = win.checkMouse()
            if mouse != None: 
                x = int(mouse.getX())
                y = int(mouse.getY())
                if (x >= 150) & (x <= 350):
                    if (y>=75) & (y<=125):
                        buttonClicked = "GoBackSettings"
                        break
        except GraphicsError:
            win.close()
            print("Window closed prematurely.")
            break
    if buttonClicked == "GoBackSettings":
        clear()
        backText.setText("Save and Exit")
        settingsScreen()

def choiceScreen():
    ## Initialize all local variables
    fsbox, tpbox, ffabox = Rectangle(Point(25,100),Point(165,400)), Rectangle(Point(180,100),Point(320,400)), Rectangle(Point(335,100),Point(475,400))
    fsbutton,tpbutton,ffabutton = Rectangle(Point(35,130),Point(155,180)), Rectangle(Point(190,130),Point(310,180)), Rectangle(Point(345,130),Point(465,180))
    fsbutton.setFill("gray"),tpbutton.setFill("gray"),ffabutton.setFill("gray")
    fsbtext,tpbtext,ffabtext = Text(Point(95,155),"Select"),Text(Point(250,155),"Select"),Text(Point(405,155),"Select")
    fstitle, tptitle, ffatitle = Text(Point(95,350),"Free Shoot"), Text(Point(250,350),"Target Practice"), Text(Point(405,350),"Free For All")
    fsimage,tpimage,ffaimage = Image(Point(95,250),(os.path.join(currentDirectory,"images/freeshoot.png"))),Image(Point(250,250),(os.path.join(currentDirectory,"images/targetpractice.png"))),Image(Point(405,250),(os.path.join(currentDirectory,"images/freeforall.png")))
    bigtitle = Text(Point(250,450),"Please Select Your Gamemode:")
    bigtitle.setFace("arial"), bigtitle.setSize(20)
    gamemode = ""
    # Help Button
    helpButton,helpText = Rectangle(Point(150,25),Point(350,75)), Text(Point(250,50),"Wait, what do these mean?")
    helpButton.setFill("gray"), helpText.setFill("Black")
    objects = [fsbox,tpbox,ffabox,fsbutton,tpbutton,ffabutton,fsbtext,tpbtext,ffabtext,fstitle,tptitle,ffatitle,fsimage,tpimage,ffaimage,helpButton,helpText,bigtitle]
    
    # Actual code
    win.setBackground("light green")
    for o in objects:
        o.draw(win)
    while gamemode == "":
        try:
            mouse = win.getMouse()
            x = int(mouse.getX())
            y = int(mouse.getY())
            if (y >= 130) & (y <= 180):
                if (x>=35) & (x<=155):
                    gamemode = "FS"
                if (x>=190) & (x<=310):
                    gamemode = "TP"
                if (x>=345) & (x<=465):
                    gamemode = "FFA"
            if (y>=25) & (y<=75):
                if(x>=150) & (x<=350):
                    gamemode = "HELP"
        except GraphicsError:
            win.close()
            print("Window closed prematurely.")
            break
    print(gamemode) # troubleshooting line
    clear()
    return gamemode

def reloadSettings():
    with open(settingsPath, 'r') as file:
        data = file.readlines()

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
    clear()

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
    distance = math.sqrt((x - targetX)**2 + (y - targetY)**2)
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
    win.redraw()
    reloadSettings()
    win.setBackground(data[0].replace('\n', ""))
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
    if buttonClicked == "Start":
        clear()
        gamemode = choiceScreen() 
        if gamemode == "HELP":
            htpScreen()
        else:
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
        clear()
        settingsScreen()
    
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