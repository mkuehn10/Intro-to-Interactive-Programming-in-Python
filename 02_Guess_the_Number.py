# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random

# initialize global variables used in your code
number = random.randrange(0, 100)
guesses = 0
current_range = 100
max_guesses = 7

# define helper functions
def init():
    global max_guesses, guesses
    guesses = 0
    print "New game. ",
    if current_range == 100:
        print "Range is from 0 - 100."
        max_guesses = 7
    else:
        print "Range is from 0 - 1000."
        max_guesses = 10
    remaining_guesses()

def remaining_guesses():
    global max_guesses, guesses
    print "Number of remaining guesses is", max_guesses - guesses
    print ""

# define event handlers for control panel
def range100():
    # button that changes range to range [0,100) and restarts
    global number, current_range
    number = random.randrange(0, 100)
    current_range = 100
    init()

def range1000():
    # button that changes range to range [0,1000) and restarts
    global number, current_range
    number = random.randrange(0, 1000)
    current_range = 1000
    init()
    
def get_input(guess):
    # main game logic goes here
    guess = float(guess)
    print "Guess was",guess
    global guesses, number
    guesses += 1
    remaining_guesses()
    if guesses >= max_guesses and not(number == guess):
        print "You ran out of guesses. The number was",number
        print ""
        if current_range == 100:
            range100()
        else:
            range1000()
    elif number > guess:
        print "Higher!"
        print ""
    elif number < guess:
        print "Lower!"
        print ""
    elif number == guess:
        print "Correct!"
        print ""
        if current_range == 100:
            range100()
        else:
            range1000()
    
# create frame
frame = simplegui.create_frame("Guess The Number", 300, 300)

# register event handlers for control elements
frame.add_button("Range: 0 - 100", range100)
frame.add_button("Range: 0 - 1000", range1000)
frame.add_input("Guess: ", get_input, 100)

# start frame
frame.start()
init()

# always remember to check your completed program against the grading rubric
