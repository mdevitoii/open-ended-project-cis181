# Michael DeVito II
# settings.py
# Settings screen for Archery game
# Also might store future settings (ex: # of rounds, wind enable/disable, etc.)

from graphics import *

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
