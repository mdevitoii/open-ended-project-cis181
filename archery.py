# Michael DeVito
# archery.py
# An archery program designed for Theresa <3
# Version 1.2

from time import *
from math import sqrt
from os import path
from random import randint
from graphics import *
import gc

############### GLOBAL VARIABLES (GET RID OF ASAP) ###############
target = Image(Point(250,250), (os.path.join(os.path.dirname(__file__),"images/target.png")))
##################################################################

def settingsScreen(w):  
    # initalize local variables
    settingsPath = os.path.join(os.path.dirname(__file__), 'settings.mike') 
    defaultColorText, modeText = Text(Point(175,275),"Background Color:"), Text(Point(175,250),"Controls: (Mouse or Arrows)")
    defaultColorEntry, modeEntry = Entry(Point(350,275),10),Entry(Point(350,250),10)
    backButton = Rectangle(Point(150,75),Point(350,125))
    backButton.setFill("gray")
    backText = Text(Point(250,100),"Save and Exit")
    backText.setFill("Black")
    htpButton = Rectangle(Point(150,150),Point(350,200))
    htpButton.setFill("Light green")
    htpText = Text(Point(250,175), "How to Play")
    title = Text(Point(250,400),"Settings Screen")
    title.setSize(30)
    settingsObjects = [backButton,backText,htpButton,htpText,defaultColorText,defaultColorEntry,modeText,modeEntry,title]

    with open(settingsPath, 'r') as file:
        data = file.readlines()
        if defaultColorEntry.getText() == "":
            data[0] = "pink\n"
        elif modeEntry.getText() == "":
            data[1] = "mouse\n"
        defaultColorEntry.setText(data[0].replace('\n', ""))
        modeEntry.setText(data[1].replace('\n', ""))
    
    w.setBackground("light gray")
    for o in settingsObjects:
        o.draw(w)
    while True:
        try:
            mouse = w.checkMouse()
            if mouse:
                x = int(mouse.getX())
                y = int(mouse.getY())
                if (x >= 150) & (x <= 350):
                    if (y>=75) & (y<=125):
                        buttonClicked = "GoBack"
                        break
                    if (y>=150) & (y<=200):
                        buttonClicked = "HTP"
                        break
        except GraphicsError:
            w.close()
            with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
                f.write("True")
            break
    if buttonClicked == "GoBack":
        clear(w)
        if defaultColorEntry.getText() == "":
            data[0] = "pink\n"
        elif modeEntry.getText() == "":
            data[1] = "arrows\n"
        
        if modeEntry.getText().lower() in ['arrows','mouse']:
            data[1] = modeEntry.getText().lower()
        else:
            Text(Point(250,250),f'The mode {modeEntry.getText()} is invalid. Please try again.').draw(w)
            Text(Point(250,200),'Valid Modes: Arrows, Mouse').draw(w)
            button = Rectangle(Point(150,75),Point(350,125))
            button.setFill("gray"), button.draw(w)
            Text(Point(250,100),'Click here to exit.').draw(w)
            w.getMouse()
            clear(w)
        
        if defaultColorEntry.getText().lower() in ['pink','orange','red','yellow','green','blue','purple','lime','light green','light blue']:
            data[0] = defaultColorEntry.getText().lower() + '\n'
        else:
            Text(Point(250,250),f'The color {defaultColorEntry.getText()} is invalid. Please try again.').draw(w)
            Text(Point(250,200),'Valid colors include:\nRed, Orange, Yellow, Green, Blue,\n Purple, Pink, Lime, Light Green, Light Blue').draw(w)
            button = Rectangle(Point(150,75),Point(350,125))
            button.setFill("gray"), button.draw(w)
            Text(Point(250,100),'Click here to exit.').draw(w)
            w.getMouse()
            clear(w)
        

        with open(settingsPath, "w") as file:
            file.writelines(data)
    if buttonClicked == "HTP":
        clear(w)
        htpScreen(w)

def htpScreen(w): 
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
    backButton.setFill("gray"), instructions.setSize(10), w.setBackground("light yellow"), backText.setText("Go Back")
    instructions.draw(w), backButton.draw(w), backText.draw(w)
    while True:
        try:
            mouse = w.checkMouse()
            if mouse != None: 
                x = int(mouse.getX())
                y = int(mouse.getY())
                if (x >= 150) & (x <= 350):
                    if (y>=75) & (y<=125):
                        buttonClicked = "GoBackSettings"
                        break
        except GraphicsError:
            w.close()
            with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
                f.write("True")
            break
    if buttonClicked == "GoBackSettings":
        clear(w)
        backText.setText("Save and Exit")
        settingsScreen(w)

def choiceScreen(w): 
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
    w.setBackground("light green")
    for o in objects:
        o.draw(w)
    while gamemode == "":
        try:
            mouse = w.checkMouse()
            if mouse:
                x = int(mouse.getX())
                y = int(mouse.getY())
                if (y >= 130) & (y <= 180):
                    if (x>=35) & (x<=155):
                        gamemode = 1
                    if (x>=190) & (x<=310):
                        gamemode = 2
                    if (x>=345) & (x<=465):
                        gamemode = 3
                if (y>=25) & (y<=75):
                    if(x>=150) & (x<=350):
                        gamemode = 4
        except GraphicsError:
            w.close()
            with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
                f.write("True")
            break
    clear(w)
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

def clear(w): # clears the window
    try:
        for item in w.items[:]:
            item.undraw()
    except:
        pass

def countToStart(gamemode,mode,difficulty,arrows,w): # function for countdown before start
    try:
        target = Image(Point(250,250), (os.path.join(os.path.dirname(__file__),"images/target.png")))
        gamemodeText,modetext = Text(Point(250,200),f'Current Gamemode: {gamemode}'),Text(Point(250,100),f'Controls: {mode}')
        gamemodeText.setSize(20),modetext.setSize(20)
        gamemodeText.draw(w),modetext.draw(w)
        startCountdownText = Text(Point(250,300), "Begin in ... 5")
        startCountdownText.setSize(30)
        startCountdownText.setFill("Black")
        timerSquare = Rectangle(Point(450,450), Point(500,500))
        timerSquare.setFill("Brown")
        timerCountdown = Text(Point(470.5, 470.5), "0")
        timerCountdown.setFill("White")
        timerCountdown.setSize(25)
        if difficulty != None:
            difficultytext = Text(Point(250,150),f'Current Difficulty: {difficulty}')
            difficultytext.setSize(20), difficultytext.draw(w)
        startCountdownText.draw(w)
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
        clear(w)
        timerSquare.draw(w)
        timerCountdown.draw(w)
        if gamemode != "Free-For-All":
            target.draw(w)
            for i in arrows:
                arrows[i].draw(w)
        startCountdownText.setText("Begin in ... 5")
    except GraphicsError:
        w.close()
        with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
            f.write("True")
    gc.collect()
    return timerCountdown

def pointCalculation(click,difficulty,wind,score,w):
    x,y = round(click.x,0), round(click.y,0)
    if difficulty != None:
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
    point = Circle(spotClicked,2)
    point.setFill("black"), point.setOutline("white"), point.draw(w)
    targetCenter = target.getAnchor()
    targetX = targetCenter.getX()
    targetY = targetCenter.getY()
    distance = sqrt((x - targetX)**2 + (y - targetY)**2)
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
    elif 0.0 <= distance_ratio <= 0.1:
        print("You hit Bullseye! +10 points")
        score += 10
    else:
        print("You missed!")
    return score

def freeShootRound(mode,currentPOS,score,timerCountdown,w): # 1 round of game, Free shoot gamemode
    timeout = 5
    timerCountdown.setText(timeout) # sets timer text to timeout time 
    # sleep(0.5)
    start_time = time.time()
    difficulty, wind = None, None
    if currentPOS is None:
        currentPOS = Point(250,250)
    if mode == "arrows":
        crosshair = Image(currentPOS,(os.path.join(os.path.dirname(__file__),"images/crosshair.png")))
        crosshair.draw(w)
    elif mode == "mouse":
        click = None

    while time.time() - start_time < timeout:
        if mode == "mouse": # ISSUE LIES SOMEWHERE IN HERE
            click = w.checkMouse()
            remaining_time = int(timeout - (time.time() - start_time))
            timerCountdown.setText(f"{remaining_time}")
            if click:
                break
        elif mode == "arrows":
            key = w.checkKey()
            # sleep(0.1)
            remaining_time = int(timeout - (time.time() - start_time))
            timerCountdown.setText(f"{remaining_time}")
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
    
    if mode == "mouse":
        if click:
            score = pointCalculation(click,difficulty,wind,score,w)
        else:
            print("Program was not clicked in time")
    
    if mode == "arrows":
        if key == "space":
            currentPOS = crosshair.getAnchor()
            score = pointCalculation(currentPOS,difficulty,wind,score,w)
            
        else:
            print("Spacebar was not hit in time")
            crosshair.undraw()
    
    passData = {
            "centerPOS": currentPOS,
            "score": score
            }
    return passData

def targetPracticeRound(difficulty,mode,currentPOS,score,timerCountdown,w): # 1 round of game, Target Practice gamemode
    # local variables
    try:
        wind_speed, wind_direction = 0,0
        timeout = 5
        windbox = Rectangle(Point(450,350),Point(500,450))
        windbox.setFill("light blue")
        windText = Text(Point(475,425),"Wind:")
        directionsText = ["N","NE","E","SE","S","SW","W","NW"]
        if currentPOS == None:
            currentPOS = Point(250,250)
        crosshair = Image(currentPOS,(os.path.join(os.path.dirname(__file__),"images/crosshair.png")))
        if mode == "arrows":
            crosshair.draw(w)
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
        windbox.draw(w), directions[wind_direction].draw(w), windText.draw(w)
        timerCountdown.setText(timeout) # sets timer text to timeout time 
        sleep(0.5)
        start_time = time.time()
        while time.time() - start_time < timeout:
            if mode == "mouse":
                click = w.checkMouse()
                remaining_time = int(timeout - (time.time() - start_time))
                timerCountdown.setText(f"{remaining_time}")
                sleep(0.1)
                if click:
                    break
            elif mode == "arrows":
                key = w.checkKey()
                sleep(0.1)
                remaining_time = int(timeout - (time.time() - start_time))
                timerCountdown.setText(f"{remaining_time}")
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
        if mode == "mouse":
            if click:
                wind = [wind_speed,directionsText[wind_direction]]
                score = pointCalculation(click,difficulty,wind,score,w)
            else:
                print("Program was not clicked in time")
            passData = {
                "centerPOS": Point(250,250),
                "score": score
                }
            return passData
        if mode == "arrows":
            if key == "space":
                currentPOS = crosshair.getAnchor()
                wind = [wind_speed,directionsText[wind_direction]]
                score = pointCalculation(currentPOS,difficulty,wind,score,w)
                passData = {
                "centerPOS": currentPOS,
                "score": score
                }
                return passData
            else:
                print("Spacebar was not hit in time")
                crosshair.undraw()
        directions[wind_direction].undraw(), windText.undraw()
    except GraphicsError:
        w.close()
        with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
            f.write("True")
        passData = {"centerPOS": Point(250,250),"score": 0} 

def ffaRound(mode,timerCountdown,w): # 1 round of game, Free For All gamemode
    # initialize variables
    targets = []
    coordinates = []
    active_coordinates = []
    timeout = 30
    score = 0
    currentPOS = Point(250,250)
    nextTarget = 0
    for _ in range(0,500):
        # randomize 500 tuples of coordinates and put them in a list
        d = (randint(25,475),randint(25,475))
        if d[0] >= 425 and d[1] >= 425:
            d = (d[0]-25,d[1]-25)
        coordinates.append(d)
        # 500 targets for screen, initialize them and put them all in a list
        t = Image(Point(d[0],d[1]), (os.path.join(os.path.dirname(__file__),"images/target_small.png")))
        targets.append(t)
    for t in range(0,30):
        # draw first 30 targets, leave last 470 as extras
        targets[t].draw(w)
        active_coordinates.append(coordinates[t]) # put first 30 coordinates into an active list
        nextTarget += 1
    if currentPOS == None:
        currentPOS = Point(250,250)
    crosshair = Image(currentPOS,(os.path.join(os.path.dirname(__file__),"images/crosshair.png")))
    if mode == "arrows":
        crosshair.draw(w)
    elif mode == "mouse":
        click = None
    
    print(f'ACTIVE COORDINATES: {active_coordinates}')


    start_time = time.time()
    while time.time() - start_time < timeout:
        if mode == "mouse":
            click = w.checkMouse()
            remaining_time = int(timeout - (time.time() - start_time))
            timerCountdown.setText(f"{remaining_time}")
            sleep(0.1)
            if click:
                print("Shot taken!") # troubleshooting
                for c in active_coordinates: # checks to see if a target was clicked
                    targetX,targetY = c[0],c[1]
                    clickX,clickY = click.getX(),click.getY()
                    distance = sqrt((clickX - targetX)**2 + (clickY - targetY)**2)
                    radius = 25
                    distance_ratio = distance/radius
                    if distance_ratio <= 1.0:
                        score += 1
                        print(f"A target was clicked at ({targetX,targetY}). +1 POINT\n\n")
                        for _ in range(0,(randint(1,3))): # checks how many new targets should be drawn. can be 1-3
                            try:                                
                                targets[nextTarget].draw(w)
                                active_coordinates.append(coordinates[nextTarget])
                                nextTarget += 1
                            except IndexError:
                                print("No more targets") # troubleshooting
                                pass
                        coords = (targetX,targetY)
                        i = coordinates.index(coords)
                        targets[i].undraw()
                        active_coordinates.pop(active_coordinates.index(c))
                        coordinates.pop(i),targets.pop(i)
        elif mode == "arrows":
            key = w.checkKey()
            remaining_time = int(timeout - (time.time() - start_time))
            timerCountdown.setText(f"{remaining_time}")
            if key == "Right":
                crosshair.move(10,0)
            elif key == "Left":
                crosshair.move(-10,0)
            elif key == "Up":
                crosshair.move(0,10)
            elif key == "Down":
                crosshair.move(0,-10)   
            elif key == "space":
                print("Shot taken!") # troubleshooting
                Point(crosshair.getAnchor().getX(),crosshair.getAnchor().getY()).draw(w)
                if randint(1,2) == 2:
                    try:
                        print("Drawing new target!") # troubleshooting
                        targets[nextTarget].draw(w)
                        if mode == "arrows":
                            crosshair.undraw(), crosshair.draw(w)
                        nextTarget += 1
                    except IndexError:
                        print("No more targets") # troubleshooting
                        pass
    return score
    
def scoreScreen(passData,w):
    scorebox = Rectangle(Point(125,125),Point(375,175))
    scorebox.setFill("yellow"),scorebox.draw(w)
    scoretext = Text(Point(250,150),f'Your Final Score is: {passData["score"]}')
    scoretext.setSize(15),scoretext.draw(w)
    returnbutton = Rectangle(Point(200,25),Point(300,75))
    returnbutton.setFill("lime"), returnbutton.draw(w)
    returntext = Text(Point(250,50),f'Return to Menu')
    returntext.setSize(10), returntext.draw(w)
    buttonClicked = 0
    while buttonClicked == 0:
        try:
            mouse = w.checkMouse()
            if mouse:
                x = int(mouse.getX())
                y = int(mouse.getY())
                if (x >= 200) & (x <= 300):
                    if (y >= 25) & (y <= 75):
                        buttonClicked = 1 # go back to menu
        except GraphicsError:
            w.close()
            with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
                f.write("True")
            buttonClicked = -1 # win closed prematurely

def crashScreen(w):
    w.setBackground("Lime")
    instructions = Text(Point(250,250), "This is a crash screen. \nThe last time the game was run, it was closed unexpecetedly. \nYou can ignore this screen, this is just to make sure the game runs properly. \nThanks for playing!") 
    instructions.setSize(10)
    backButton = Rectangle(Point(150,75),Point(350,125))
    backButton.setFill("gray")
    backText = Text(Point(250,100),"Exit")
    backText.setFill("Black")
    crashObjects = [instructions,backButton,backText]
    for o in crashObjects:
        o.draw(w)
    clicked = False
    while clicked == False:
        try:
            mouse = w.checkMouse()
            if mouse:
                x = int(mouse.getX())
                y = int(mouse.getY())
                if (x >= 150) & (x <= 350):
                    if (y>=75) & (y<=125):
                        buttonClicked = "GoBack"
                        clear(w)
                        clicked = True
        except GraphicsError:
            w.close()
            with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
                f.write("True")
            clicked = True

def main(): # main method, uses win
    playing = True
    w = GraphWin("Archery Game", 500, 500)  
    w.setCoords(0,0,500,500)
    # trying to fix crash error
    try:
        debugPath = os.path.join(os.path.dirname(__file__), 'debug.mike') 
        with open(debugPath, 'r') as file:
            crash = file.readlines()
        if crash == ['True']:
            crashScreen(w)
            settingsScreen(w) 
            with open(debugPath, 'w') as file:
                file.writelines('False')
    except:
        pass

    while playing:
        time.sleep(0.5)
        # initialize everything
        data = reloadSettings()
        arrows = dict()
        rounds = 5
        openingText, startButton, startText, settingsButton, settingsText, quitButton, quitText = Text(Point(250,450), "Theresa's Archery Game"), Rectangle(Point(150,150),Point(350,250)), Text(Point(250, 200), "Click to Start"),Rectangle(Point(150,75),Point(350,125)),Text(Point(250,100),"Settings/How-To-Play"),Rectangle(Point(450,50),Point(501,-1)),Text(Point(475,25),"Quit")
        openingText.setSize(30),startButton.setFill("light green"),startText.setFill("Black"),settingsButton.setFill("gray"),settingsText.setFill("Black"),quitButton.setFill("red")
        for i in range(1,rounds+1):
            arrows[i] = Image(Point(i * 20,480), (os.path.join(os.path.dirname(__file__),"images/arrow.png")))
        try:
            w.setBackground(data[0].replace('\n', ""))
            mode = data[1]
        except:
            data = ["pink\n","arrows\n"]
            with open(os.path.join(os.path.dirname(__file__), 'settings.mike'), "w") as file:
                file.writelines(data)
        try:
            openingText.draw(w), startButton.draw(w), startText.draw(w),settingsButton.draw(w), settingsText.draw(w), quitButton.draw(w), quitText.draw(w)
        except:
            playing = False
            break
        buttonClicked = 0
        center = Point(250,250)
        passData = {
            "centerPOS": center,
            "score": 0
        } # currentPOS and Score

        # checks what option the user chooses and sends them to desired option
        while buttonClicked == 0:
            try:
                mouse = w.checkMouse()
                if mouse:
                    x = int(mouse.getX())
                    y = int(mouse.getY())
                    if (x >= 150) & (x <= 350):
                        if (y >= 150) & (y <= 250):
                            buttonClicked = 1 # start
                        elif (y>=75) & (y<=125):
                            buttonClicked = 2 # settings
                    elif (x >=450):
                        if (y <= 50):
                            buttonClicked = 3 # quit
                            break
                
            except GraphicsError:
                w.close()
                buttonClicked = -1 
                passData = {
                    "centerPOS": center,
                    "score": 0
                } 
                with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
                    f.write("True")
        # checks button that was clicked and sends user to correct gamemode
        if buttonClicked == 1: # start
            clear(w)
            gamemode = choiceScreen(w) 
            if gamemode == 4:
                htpScreen(w)
            elif gamemode == 1:
                timerCountdown = countToStart("Free Shoot", mode.capitalize(),None,arrows,w)
                for i in range(1,rounds+1):
                    try:
                        passData = freeShootRound(mode,passData['centerPOS'],passData['score'],timerCountdown,w)
                        arrows[i].undraw() 
                    except TypeError:
                        playing = False
                        break
            elif gamemode == 2:
                timerCountdown = countToStart("Target Practice",mode.capitalize(),"Easy",arrows,w)
                for i in range(1,rounds+1):
                    try:
                        passData = targetPracticeRound("E",mode,passData['centerPOS'],passData["score"],timerCountdown,w)
                        arrows[i].undraw()
                    except TypeError:
                        playing = False
                        break
            elif gamemode == 3:
                timerCountdown = countToStart("Free-For-All",mode.capitalize(),None,arrows,w)
                score = ffaRound(mode,timerCountdown,w)
                passData = {
                    "centerPOS": center,
                    "score": int(score)
                } 
            
            sleep(0.5)
            if gamemode != 4 and playing == True:
                scoreScreen(passData,w)
            clear(w)
            gc.collect()

        elif buttonClicked == 2: # settings
            clear(w)
            settingsScreen(w)
            gc.collect()
        elif buttonClicked == 3: # quit
            w.close()
            playing = False
            gc.collect()
    
# run the program!
if __name__ == "__main__":
    main()
