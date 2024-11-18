# Michael DeVito
# archery.py
# An archery program designed for Theresa <3
# Version 1.2

from time import sleep, time
from math import sqrt
from os import path
from random import randint
from graphics import *
from storage import *

def settingsScreen():
    # initalize local variables
    settingsPath = os.path.join(os.path.dirname(__file__), 'settings.mike') 
    defaultColorText, modeText = Text(Point(175,275),"Background Color:"), Text(Point(175,250),"Controls: (Mouse or Arrows)")
    defaultColorEntry, modeEntry = Entry(Point(350,275),10),Entry(Point(350,250),10)
    backButton = Rectangle(Point(150,75),Point(350,125))
    backButton.setFill("gray")
    backText = Text(Point(250,100),"Save and Exit")
    backText.setFill("Black")
    htpButton = Rectangle(Point(150,400),Point(350,450))
    htpButton.setFill("Light green")
    htpText = Text(Point(250,425), "How to Play")
    settingsObjects = [backButton,backText,htpButton,htpText,defaultColorText,defaultColorEntry,modeText,modeEntry]





    with open(settingsPath, 'r') as file:
        data = file.readlines()
        if defaultColorEntry.getText() == "":
            data[0] = "pink\n"
        elif modeEntry.getText() == "":
            data[1] = "mouse\n"
        defaultColorEntry.setText(data[0].replace('\n', ""))
        modeEntry.setText(data[1].replace('\n', ""))
    
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
        if defaultColorEntry.getText() == "":
            data[0] = "pink\n"
        elif modeEntry.getText() == "":
            data[1] = "mouse\n"
        else:
            data[0] = defaultColorEntry.getText() + '\n'
            data[1] = modeEntry.getText()
        with open(settingsPath, "w") as file:
            file.writelines(data)
        main()
    if buttonClicked == "HTP":
        clear()
        htpScreen()

def htpScreen():
    backButton = Rectangle(Point(150,75),Point(350,125))
    backButton.setFill("gray")
    backText = Text(Point(250,100),"Save and Exit")
    backText.setFill("Black")
    howToPlay = (
    f"Welcome to Archery! A game created by Michael DeVito\n"
    f"Dedicated to Theresa <3\n\n"
    f"Archery can be played by either using the arrow keys or the Mouse.\nYou can configure which input you use via the settings screen.\n\n"
    f"The goal is to shoot as close to the center ring as you can.\nThe closer you are, the higher the point value!\n\n"
    f"There are three gamemodes: Free Shoot, Target Practice, and Free For All\n\n"
    f"Free Shoot: Freely shoot the target for 3 shots, with\n5 seconds per shot. No wind or moving target\n\n"
    f'Target Practice: Shoot the target for 3 shots, but with wind\nand possibly moving target. Difficulties are Easy, Medium, Hard, and Extreme.\n\n'
    f'Free For All: So many targets! Shoot as many as you can within 15 seconds!\n\n'
    f"Thank you for playing, and have fun!"
)
    instructions, backButton= Text(Point(250,300),howToPlay), Rectangle(Point(150,75),Point(350,125))
    backButton.setFill("gray"), instructions.setSize(10), win.setBackground("light yellow"), backText.setText("Go Back")
    instructions.draw(win), backButton.draw(win), backText.draw(win)
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
    fsimage,tpimage,ffaimage = Image(Point(95,250),(os.path.join(os.path.dirname(__file__),"images/freeshoot.png"))),Image(Point(250,250),(os.path.join(os.path.dirname(__file__),"images/targetpractice.png"))),Image(Point(405,250),(os.path.join(os.path.dirname(__file__),"images/freeforall.png")))
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
    settingsPath = os.path.join(os.path.dirname(__file__), 'settings.mike') 
    with open(settingsPath, 'r') as file:
        data = file.readlines()
    try:
        if data[0] == "":
            data[0] = "pink\n"
        elif data[1] == "":
            data[1] = "mouse\n"
    except IndexError:
        data = ['pink\n','mouse\n']
        with open(settingsPath, "w") as file:
            file.writelines(data)
    return data

def clear(): # clears the window
    for item in win.items[:]:
        item.undraw()

def countToStart(): # function for countdown before start
    startCountdownText.draw(win)
    sleep(1)
    startCountdownText.setText("Begin in ... 4")
    sleep(1)
    startCountdownText.setText("Begin in ... 3")
    sleep(1)
    startCountdownText.setText("Begin in ... 2")
    sleep(1)
    startCountdownText.setText("Begin in ... 1")
    sleep(1)
    startCountdownText.setText("GO!")
    sleep(1)
    clear()
    timerSquare.draw(win)
    timerCountdown.draw(win)
    target.draw(win)
    for i in arrows:
        arrows[i].draw(win)

def pointCalculation(click,difficulty,wind):
    global score
    # print(f"Mouse was clicked at ({click.x}, {click.y})") # troubeshooting only
    # the following 4 lines might be replaced with an image drawing that shows an arrow in the target. idk maybe
    x,y = round(click.x,0), round(click.y,0)
    if difficulty in "EMH":
        if wind[1] == "N":
            y += (wind[0]*20)
        elif wind[1] == "NE":
            x += ((wind[0]) * 20)
            y += ((wind[0]) * 20)
        elif wind[1] == "E":
            x += (wind[0]*20)
        elif wind[1] == "SE":
            x += ((wind[0]) * 20)
            y -= ((wind[0]) * 20)
        elif wind[1] == "S":
            y -= (wind[0]*20)
        elif wind[1] == "SW":
            x -= ((wind[0]) * 20)
            y -= ((wind[0]) * 20)
        elif wind[1] == "W":
            x -= ((wind[0]) * 20)
        elif wind[1] == "NW":
            x -= ((wind[0]) * 20)
            y += ((wind[0]) * 20)

    spotClicked = Point(x,y)
    spotClicked.setFill("black")
    spotClicked.draw(win) # this line ends the code that may be replaced
    targetCenter = target.getAnchor()
    targetX = targetCenter.getX()
    targetY = targetCenter.getY()
    distance = sqrt((x - targetX)**2 + (y - targetY)**2)
    imgWidth = target.getWidth()
    radius = imgWidth/2
    # Calculate the distance ratio
    distance_ratio = distance/radius
    print(distance_ratio) # troubleshooting
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
    elif 0.0 <= distance_ratio <= 0.1:
        print("You hit Bullseye! +10 points")
        score += 10
    else:
        print("You missed!")
    return score

def freeShootRound(): # 1 round of game, Free shoot gamemode
    timerCountdown.setText(timeout) # sets timer text to timeout time 
    sleep(0.5)
    start_time = time.time()
    click = None
    difficulty, wind = "N", "N"
        
    while time.time() - start_time < timeout:
        click = win.checkMouse()
        remaining_time = int(timeout - (time.time() - start_time))
        timerCountdown.setText(f"{remaining_time}")
        sleep(0.1)
        if click:
            break
    if click:
        pointCalculation(click,difficulty,wind)
    else:
        print("Program was not clicked in time")

def targetPracticeRound(difficulty,mode,currentPOS): # 1 round of game, Target Practice gamemode
    # local variables
    wind_speed, wind_direction = 0,0
    windbox = Rectangle(Point(450,350),Point(500,450))
    windbox.setFill("light blue")
    windText = Text(Point(475,425),"Wind:")
    directionsText = ["N","NE","E","SE","S","SW","W","NW"]
    if currentPOS == None:
        currentPOS = Point(250,250)
    crosshair = Image(currentPOS,(os.path.join(os.path.dirname(__file__),"images/crosshair.png")))
    if mode == "arrows":
        crosshair.draw(win)
    elif mode == "mouse":
        click = None
    directions = [
        Image(Point(475,375),(os.path.join(os.path.dirname(__file__),"images/windN.png"))),
        Image(Point(475,375),(os.path.join(os.path.dirname(__file__),"images/windNE.png"))),
        Image(Point(475,375),(os.path.join(os.path.dirname(__file__),"images/windE.png"))),
        Image(Point(475,375),(os.path.join(os.path.dirname(__file__),"images/windSE.png"))),
        Image(Point(475,375),(os.path.join(os.path.dirname(__file__),"images/windS.png"))),
        Image(Point(475,375),(os.path.join(os.path.dirname(__file__),"images/windSW.png"))),
        Image(Point(475,375),(os.path.join(os.path.dirname(__file__),"images/windW.png"))),
        Image(Point(475,375),(os.path.join(os.path.dirname(__file__),"images/windNW.png")))
        ]

    if difficulty == "E": # Easy
        wind_speed = randint(0,3)
        wind_direction = randint(0,7) # 0 = North, 7 = NW
        if randint(1,5) == 1: # 10% chance of being cut in half
            if wind_speed != 0:
                wind_speed /= 2
    
    windText.setText(f'Wind:\n{wind_speed} {directionsText[wind_direction]}')
    windbox.draw(win), directions[wind_direction].draw(win), windText.draw(win)
    timerCountdown.setText(timeout) # sets timer text to timeout time 
    sleep(0.5)
    start_time = time.time()
    while time.time() - start_time < timeout:
        if mode == "mouse":
            click = win.checkMouse()
            remaining_time = int(timeout - (time.time() - start_time))
            timerCountdown.setText(f"{remaining_time}")
            sleep(0.1)
            if click:
                break
        elif mode == "arrows":
            key = win.checkKey()
            if key == "Right":
                crosshair.move(10,0)
            elif key == "Left":
                crosshair.move(-10,0)
            elif key == "Up":
                crosshair.move(0,10)
            elif key == "Down":
                crosshair.move(0,-10)   
            elif key == "space":
                print("Shot taken!")
                crosshair.undraw()
                break
            remaining_time = int(timeout - (time.time() - start_time))
            timerCountdown.setText(f"{remaining_time}")
    if mode == "mouse":
        if click:
            wind = [wind_speed,directionsText[wind_direction]]
            pointCalculation(click,difficulty,wind)
        else:
            print("Program was not clicked in time")
    if mode == "arrows":
        if key == "space":
            currentPOS = crosshair.getAnchor()
            wind = [wind_speed,directionsText[wind_direction]]
            pointCalculation(currentPOS,difficulty,wind)
            return currentPOS
        else:
            print("Spacebar was not hit in time")
            crosshair.undraw()
    directions[wind_direction].undraw(), windText.undraw()

def main(): # main method
    win.redraw()
    data = reloadSettings()
    try:
        win.setBackground(data[0].replace('\n', ""))
        mode = data[1]
    except:
        data = ["pink\n","mouse\n"]
        with open(os.path.join(os.path.dirname(__file__), 'settings.mike'), "w") as file:
            file.writelines(data)
    openingText.draw(win)
    startButton.draw(win)
    startText.draw(win)
    settingsButton.draw(win)
    settingsText.draw(win)
    buttonClicked = ""
    currentPOS = center
    
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
    # checks button that was clicked and sends user to correct gamemode
    if buttonClicked == "Start":
        clear()
        gamemode = choiceScreen() 
        if gamemode == "HELP":
            htpScreen()
        elif gamemode == "FS":
            countToStart()
            for i in range(1,rounds+1):
                freeShootRound()
                arrows[i].undraw() 
            print(f"Your final score is: {score}\nClick to Quit.")
            clear()
        elif gamemode == "TP":
            countToStart()
            for i in range(1,rounds+1):
                currentPOS = targetPracticeRound("E",mode,currentPOS)
                arrows[i].undraw()
            print(f"Your final score is: {score}\nClick to Quit.")
            clear()
        elif gamemode == "FFA":
            countToStart()

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