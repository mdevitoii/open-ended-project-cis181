# Michael DeVito
# archery.py
# An archery program designed for Theresa <3
# v1.0

from time import *
from math import sqrt
from os import path
from random import randint
from graphics import *
from gc import collect

def settingsScreen(w): # exception handling
    try:
        # initalize all local variables
        settingsPath = os.path.join(os.path.dirname(__file__), 'settings.mike') 
        defaultColorText, modeText = Text(Point(175,275),"Background Color:"), Text(Point(175,250),"Controls: (Mouse or Arrows)")
        defaultColorEntry, modeEntry = Entry(Point(350,275),10),Entry(Point(350,250),10)
        backButton = Rectangle(Point(150,75),Point(350,125))
        backButton.setFill("gray")
        backText = Text(Point(250,100),"Save and Exit")
        backText.setFill("Black")
        htpButton = Rectangle(Point(150,150),Point(350,200))
        htpButton.setFill("Light yellow")
        htpText = Text(Point(250,175), "How to Play")
        title = Text(Point(250,400),"Settings Screen")
        title.setSize(30)
        settingsObjects = [backButton,backText,htpButton,htpText,defaultColorText,defaultColorEntry,modeText,modeEntry,title]

        # open settings.mike and check if settings are there. if not, then put in default settings
        with open(settingsPath, 'r') as file: 
            data = file.readlines()
            if defaultColorEntry.getText() == "":
                data[0] = "pink\n"
            elif modeEntry.getText() == "":
                data[1] = "mouse\n"
            defaultColorEntry.setText(data[0].replace('\n', ""))
            modeEntry.setText(data[1].replace('\n', ""))
        
        # gets the screen ready and draws all objects on settings screen
        w.setBackground("light blue")
        for o in settingsObjects:
            o.draw(w)
        
        # main screen loop
        on = True
        while on:
            try: 
                mouse = w.checkMouse() # checks if a user clicked
                if mouse: # if user did click
                    x = int(mouse.getX()) # x coord of click
                    y = int(mouse.getY()) # y coord of click 
                    if (x >= 150) & (x <= 350): # check if click is within X region of buttons
                        if (y>=75) & (y<=125): # check if click was for "Go Back" button
                            buttonClicked = "GoBack"
                            on = False
                        if (y>=150) & (y<=200): # check if click was for "How-to-play" button
                            buttonClicked = "HTP"
                            on = False
            except: # if screen is closed prematurely, close screen properly and note that there was a crash
                w.close()
                with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
                    f.write("True") # notes in debug.mike that there was a crash
                on = False
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
    except:
        w.close()
        with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
            f.write("True")

def htpScreen(w): # exception handling
    try:
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
        f"Thank you for playing, and have fun!")
        instructions, backButton= Text(Point(250,300),howToPlay), Rectangle(Point(150,75),Point(350,125))
        backButton.setFill("gray"), instructions.setSize(10), w.setBackground("light yellow"), backText.setText("Go Back")
        instructions.draw(w), backButton.draw(w), backText.draw(w)
        run = True
        while run:
            mouse = w.checkMouse()
            if mouse != None: 
                x = int(mouse.getX())
                y = int(mouse.getY())
                if (x >= 150) & (x <= 350):
                    if (y>=75) & (y<=125):
                        buttonClicked = "GoBackSettings"
                        run = False
        if buttonClicked == "GoBackSettings":
            clear(w)
            backText.setText("Save and Exit")
            settingsScreen(w)
    except:
        w.close()
        with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
            f.write("True")

def choiceScreen(w): # exception handling
    try:
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
        on = True
        while gamemode == "" and on:
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
                on = False
        clear(w)
        return gamemode
    except:
        w.close()
        with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
            f.write("True")

def reloadSettings(): # exception handling
    try:
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
    except:
        data = ['pink\n','mouse\n']
        with open(settingsPath, "w") as file:
            file.writelines(data)
        return data

def clear(w): # clears the window, exception handling
    try:
        for item in w.items[:]:
            item.undraw()
    except:
        pass

def countToStart(gamemode,mode,difficulty,arrows,w): # function for countdown before start, exception handling
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
        quiver = Rectangle(Point(0,350),Point(50,500))
        quiver.setFill("white"), quiver.setOutline("black")
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
        terminal = Rectangle(Point(50,450),Point(450,500))
        terminal.setFill("tan"), terminal.setOutline("black"), terminal.draw(w)
        if gamemode != "Free-For-All":
            target = Image(Point(250,250), (os.path.join(os.path.dirname(__file__),"images/target.png")))
            quiver.draw(w)
            target.draw(w)
            for i in arrows:
                arrows[i].draw(w)
        elif gamemode == "Free-For-All":
            r = Rectangle(Point(0,450),Point(50,500))
            r.setFill("white"), r.setOutline("black"), r.draw(w)
            i = Image(Point(25,475),(os.path.join(os.path.dirname(__file__),"images/infinity.png")))
            i.draw(w)
        startCountdownText.setText("Begin in ... 5")
        return timerCountdown
    except:
        w.close()
        with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
            f.write("True")

def pointCalculation(click,difficulty,wind,score,w): # exception handling
    try:
        x,y = round(click.x,0), round(click.y,0)
        if difficulty != None:
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
        target = Image(Point(250,250), (os.path.join(os.path.dirname(__file__),"images/target.png")))
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
            score += 1
        elif 0.8 < distance_ratio <= 0.9:
            score += 2
        elif 0.7 < distance_ratio <= 0.8:
            score += 3
        elif 0.6 < distance_ratio <= 0.7:
            score += 4
        elif 0.5 < distance_ratio <= 0.6:
            score += 5
        elif 0.4 < distance_ratio <= 0.5:
            score += 6
        elif 0.3 < distance_ratio <= 0.4:
            score += 7
        elif 0.2 < distance_ratio <= 0.3:
            score += 8
        elif 0.1 < distance_ratio <= 0.2:
            score += 9
        elif 0.0 <= distance_ratio <= 0.1:
            score += 10
        return score
    except:
        w.close()
        with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
            f.write("True")

def freeShootRound(mode,currentPOS,score,timerCountdown,terminalText,w): # 1 round of game, Free shoot gamemode, exception handling
    try:
        timeout = 5
        timerCountdown.setText(timeout) # sets timer text to timeout time 
        sleep(0.5)
        start_time = time.time()
        difficulty, wind = None, None
        if currentPOS is None:
            currentPOS = Point(250,250)
        if mode == "arrows":
            crosshair = Image(currentPOS,(os.path.join(os.path.dirname(__file__),"images/crosshair.png")))
            crosshair.draw(w)
        elif mode == "mouse":
            click = None
        
        on = True
        while time.time() - start_time < timeout and on:
            if mode == "mouse": 
                click = w.checkMouse()
                remaining_time = int(timeout - (time.time() - start_time))
                timerCountdown.setText(f"{remaining_time}")
                if click:
                    on = False
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
                    crosshair.undraw()
                    on = False
        
        if mode == "mouse":
            if click:
                score = pointCalculation(click,difficulty,wind,score,w)
                terminalText.setText(f'Shot Taken! Score: {score}')
            else:
                terminalText.setText(f"Shot Missed! Score: {score}")
        
        if mode == "arrows":
            if key == "space":
                currentPOS = crosshair.getAnchor()
                score = pointCalculation(currentPOS,difficulty,wind,score,w)  
                terminalText.setText(f'Shot Taken! Score: {score}')
            else:
                terminalText.setText(f"Shot Missed! Score: {score}")
                crosshair.undraw()
        
        passData = {
                "centerPOS": currentPOS,
                "score": score
                }
        return passData
    except:
        w.close()
        with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
            f.write("True")

def targetPracticeRound(difficulty,mode,currentPOS,score,timerCountdown,terminalText,w): # 1 round of game, Target Practice gamemode, exception handling
    try:
        # local variables
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

        if difficulty == "Easy": 
            wind_speed = randint(0,3)
        elif difficulty == "Medium":
            wind_speed = randint(1,5)
        elif difficulty == "Hard": 
            wind_speed = randint(3,6)
        elif difficulty == "Extreme": 
            wind_speed = randint(0,10)
        

        wind_direction = randint(0,7) # 0 = North, 7 = NW
        if randint(1,4) == 1: # 20% chance of being cut in half
            if wind_speed != 0:
                wind_speed /= 2
        
        windText.setText(f'Wind:\n{wind_speed} {directionsText[wind_direction]}')
        windbox.draw(w), directions[wind_direction].draw(w), windText.draw(w)
        timerCountdown.setText(timeout) # sets timer text to timeout time 
        sleep(0.5)
        start_time = time.time()
        on = True
        while time.time() - start_time < timeout and on:
            if mode == "mouse":
                click = w.checkMouse()
                remaining_time = int(timeout - (time.time() - start_time))
                timerCountdown.setText(f"{remaining_time}")
                sleep(0.1)
                if click:
                    on = False
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
                    crosshair.undraw()
                    on = False
        if mode == "mouse":
            if click:
                wind = [wind_speed,directionsText[wind_direction]]
                print(wind) # troubleshooting
                score = pointCalculation(click,difficulty,wind,score,w)
                terminalText.setText(f'Shot Taken! Score: {score}')
            else:
                terminalText.setText(f'Shot Missed! Score: {score}')
            passData = {
                "centerPOS": Point(250,250),
                "score": score
                }
        if mode == "arrows":
            if key == "space":
                currentPOS = crosshair.getAnchor()
                wind = [wind_speed,directionsText[wind_direction]]
                score = pointCalculation(currentPOS,difficulty,wind,score,w)
                terminalText.setText(f'Shot Taken! Score: {score}')
                passData = {
                "centerPOS": currentPOS,
                "score": score
                }
            else:
                passData = {
                "centerPOS": Point(250,250),
                "score": score
                }
                terminalText.setText(f'Shot Missed! Score: {score}')
                crosshair.undraw()
        directions[wind_direction].undraw(), windText.undraw()
        return passData
    except:
        w.close()
        with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
            f.write("True")

def ffaRound(mode,timerCountdown,terminalText,w): # 1 round of game, Free For All gamemode, exception handling
    try:
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
            d = (randint(25,475),randint(25,415))
            if d[0] >= 475 and d[1] >= 405:
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

        start_time = time.time()
        while time.time() - start_time < timeout:
            if mode == "mouse":
                click = w.checkMouse()
                remaining_time = int(timeout - (time.time() - start_time))
                timerCountdown.setText(f"{remaining_time}")
                sleep(0.1)
                if click:
                    for c in active_coordinates: # checks to see if a target was clicked
                        targetX,targetY = c[0],c[1]
                        clickX,clickY = click.getX(),click.getY()
                        distance = sqrt((clickX - targetX)**2 + (clickY - targetY)**2)
                        radius = 25
                        distance_ratio = distance/radius
                        if distance_ratio <= 1.0:
                            score += 1
                            terminalText.setText(f'Shot Taken! Score: {score}')
                            for _ in range(0,(randint(1,3))): # checks how many new targets should be drawn. can be 1-3
                                try:                                
                                    targets[nextTarget].draw(w)
                                    active_coordinates.append(coordinates[nextTarget])
                                    nextTarget += 1
                                except IndexError:
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
                    for c in active_coordinates: # checks to see if a target was clicked
                        targetX,targetY = c[0],c[1]
                        crosshairCoordinates = crosshair.getAnchor()
                        clickX,clickY = crosshairCoordinates.getX(),crosshairCoordinates.getY()
                        distance = sqrt((clickX - targetX)**2 + (clickY - targetY)**2)
                        radius = 25
                        distance_ratio = distance/radius
                        if distance_ratio <= 1.0:
                            score += 1
                            terminalText.setText(f'Shot Taken! Score: {score}')
                            for _ in range(0,(randint(1,3))): # checks how many new targets should be drawn. can be 1-3
                                try:                                
                                    targets[nextTarget].draw(w)
                                    active_coordinates.append(coordinates[nextTarget])
                                    nextTarget += 1
                                except IndexError:
                                    pass
                            coords = (targetX,targetY)
                            i = coordinates.index(coords)
                            targets[i].undraw()
                            active_coordinates.pop(active_coordinates.index(c))
                            coordinates.pop(i),targets.pop(i)
                            crosshair.undraw(), crosshair.draw(w)
        return score
    except:
        w.close()
        with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
            f.write("True")
    
def scoreScreen(passData,w): # exception handling
    try:
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
    except:
        w.close()
        with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
            f.write("True")

def crashScreen(w): # exception handling
    try:
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
    except:
        w.close()
        with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
            f.write("True")

def difficultyScreen(w): # exception handling
    try:
        easyButton,mediumButton,hardButton,extremeButton = Rectangle(Point(20,150),Point(120,200)),Rectangle(Point(140,150),Point(240,200)),Rectangle(Point(260,150),Point(360,200)),Rectangle(Point(380,150),Point(480,200))
        easyButton.setFill("lime"),mediumButton.setFill("yellow"),hardButton.setFill("orange"),extremeButton.setFill("red")
        easyText,mediumText,hardText,extremeText = Text(Point(70,175),"Easy"),Text(Point(190,175),"Medium"),Text(Point(310,175),"Hard"),Text(Point(430,175),"Extreme")
        difficulty = "Easy"
        waiting = True
        bigTitle = Text(Point(250,450),"Please Select Your Difficulty:")
        bigTitle.setFace("arial"), bigTitle.setSize(20)
        
        allObjects = [easyButton,mediumButton,hardButton,extremeButton,bigTitle,easyText,mediumText,hardText,extremeText]
        for o in allObjects:
            o.draw(w)
        
        while waiting:
            try: 
                mouse = w.checkMouse() # checks if a user clicked
                if mouse: # if user did click
                    x = int(mouse.getX()) # x coord of click
                    y = int(mouse.getY()) # y coord of click 
                    if (y >= 150) & (y <= 200): # check if click is within Y region of buttons
                        if (x>=20) & (x<=120): # check if click was for "Easy" button
                            difficulty = "Easy"
                            waiting = False
                        elif (x>=140) & (x<=240): # check if click was for "Medium" button
                            difficulty = "Medium"
                            waiting = False
                        elif (x>=260) & (x<=360): # check if click was for "Hard" button
                            difficulty = "Hard"
                            waiting = False
                        elif (x>=380) & (x<=480): # check if click was for "Extreme" button
                            difficulty = "Extreme"
                            waiting = False
            except: # if screen is closed prematurely, close screen properly and note that there was a crash
                w.close()
                with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
                    f.write("True") # notes in debug.mike that there was a crash
                waiting = False
        
        clear(w)
        return difficulty
    except:
        w.close()
        with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
            f.write("True")

def main(): # main method, uses win, exception handling
    try:
        playing = True
        w = GraphWin("Archery Game", 500, 500)  
        w.setCoords(0,0,500,500)
        try: # checks if debug.mike is true
            debugPath = os.path.join(os.path.dirname(__file__), 'debug.mike') 
            with open(debugPath, 'r') as file:
                crash = file.readlines()
            if crash == ['True']: # if debug.mike is true, initiate crash screen
                crashScreen(w)
                settingsScreen(w) 
                with open(debugPath, 'w') as file:
                    file.writelines('False') # set debug.mike to false
        except:
            pass # if debug.mike doesn't exist, oh well!

        while playing: # while user has not quit the game
            # initialize everything
            data = reloadSettings()
            arrows = dict()
            rounds = 5
            openingText, startButton, startText, settingsButton, settingsText, quitButton, quitText = Text(Point(250,450), "Theresa's Archery Game!"), Rectangle(Point(150,100),Point(350,150)), Text(Point(250, 125), "Click to Start"),Rectangle(Point(150,25),Point(350,75)),Text(Point(250,50),"Settings/How-To-Play"),Rectangle(Point(450,50),Point(501,-1)),Text(Point(475,25),"Quit")
            openingText.setSize(30),startButton.setFill("light green"),startText.setFill("Black"),settingsButton.setFill("gray"),settingsText.setFill("Black"),quitButton.setFill("red")
            photo = Image(Point(250,300),os.path.join(os.path.dirname(__file__), 'images/M+T.png'))
            for i in range(1,rounds+1):
                arrows[i] = Image(Point(25,500-(i * 25)), (os.path.join(os.path.dirname(__file__),"images/arrow.png")))
            try:
                w.setBackground(data[0].replace('\n', ""))
                mode = data[1]
            except:
                data = ["pink\n","arrows\n"]
                with open(os.path.join(os.path.dirname(__file__), 'settings.mike'), "w") as file:
                    file.writelines(data)
            try: # tries to draw objects. if it fails, window must not be open!
                openingText.draw(w), startButton.draw(w), startText.draw(w),settingsButton.draw(w), settingsText.draw(w), quitButton.draw(w), quitText.draw(w),photo.draw(w)
            except:
                playing = False
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
                            if (y >= 100) & (y <= 150):
                                buttonClicked = 1 # start
                            elif (y>=25) & (y<=75):
                                buttonClicked = 2 # settings
                        elif (x >=450):
                            if (y <= 50):
                                buttonClicked = 3 # quit
                                playing = False
                                
                    
                except GraphicsError:
                    w.close()
                    buttonClicked = -1 
                    passData = {
                        "centerPOS": center,
                        "score": 0
                    } 
                    with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
                        f.write("True")
            try: # checks button that was clicked and sends user to correct gamemode
                if buttonClicked == 1: # start
                    clear(w)
                    gamemode = choiceScreen(w) 
                    if gamemode == 4:
                        htpScreen(w)
                    elif gamemode == 1:
                        timerCountdown = countToStart("Free Shoot", mode.capitalize(),None,arrows,w)
                        terminalText = Text(Point(250,475),"Take A Shot! Score: 0")
                        terminalText.draw(w)
                        for i in range(1,rounds+1):
                            try:
                                passData = freeShootRound(mode,passData['centerPOS'],passData['score'],timerCountdown,terminalText,w)
                                arrows[i].undraw() 
                            except TypeError:
                                playing = False
                    elif gamemode == 2:
                        difficulty = difficultyScreen(w)
                        timerCountdown = countToStart("Target Practice",mode.capitalize(),difficulty,arrows,w)
                        terminalText = Text(Point(250,475),"Take A Shot! Score: 0")
                        terminalText.draw(w)
                        for i in range(1,rounds+1):
                            try:
                                passData = targetPracticeRound(difficulty,mode,passData['centerPOS'],passData["score"],timerCountdown,terminalText,w)
                                arrows[i].undraw()
                            except TypeError:
                                playing = False
                    elif gamemode == 3:
                        timerCountdown = countToStart("Free-For-All",mode.capitalize(),None,arrows,w)
                        terminalText = Text(Point(250,475),"Take A Shot! Score: 0")
                        terminalText.draw(w)
                        score = ffaRound(mode,timerCountdown,terminalText,w)
                        passData = {
                            "centerPOS": center,
                            "score": int(score)
                        } 
                    
                    sleep(0.5)
                    if gamemode != 4 and playing == True:
                        scoreScreen(passData,w)
                    clear(w)

                elif buttonClicked == 2: # settings
                    clear(w)
                    settingsScreen(w)
                elif buttonClicked == 3: # quit
                    w.close()
                    playing = False
            except GraphicsError:
                w.close()
                buttonClicked = -1 
                passData = {
                    "centerPOS": center,
                    "score": 0
                } 
                with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
                    f.write("True")
            collect()
    except:
        w.close()
        with open(os.path.join(os.path.dirname(__file__), 'debug.mike'), "w") as f:
            f.write("True")
    
# run the program!
if __name__ == "__main__":
    main()