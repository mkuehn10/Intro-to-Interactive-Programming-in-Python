# GUI-based version of RPSLS

###################################################
# Student should add code where relevant to the following.

import simplegui
import random

#global variables
player_wins = 0
computer_wins = 0
ties = 0

#helper functions
def init():
    global player_wins, computer_wins, ties
    player_wins = 0
    computer_wins = 0
    ties = 0
    print "New game started!"
    print_game_status()

def print_game_status():
    print "Player: " + str(player_wins) + " Computer: " + str(computer_wins) + " Ties: " + str(ties) + "\n"
    
def number_to_name(number):
    # fill in your code below 
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        return 'rock'
    elif number == 1:
        return 'Spock'
    elif number == 2:
        return 'paper'
    elif number == 3:
        return 'lizard'
    elif number == 4:
        return 'scissors'
    else:
        return None
    
def name_to_number(name):
    # fill in your code below
    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == 'rock':
        return 0
    elif name == 'Spock':
        return 1
    elif name == 'paper':
        return 2
    elif name == 'lizard':
        return 3
    elif name== 'scissors':
        return 4
    else:
        return None

def rpsls(name): 
    # fill in your code below
    # convert name to player_number using name_to_number
    player_number = name_to_number(name)
    player_string = "Player chooses " + number_to_name(player_number)
    
    # compute random guess for comp_number using random.randrange()
    comp_number = random.randrange(0,5)
    
    # compute difference of player_number and comp_number modulo five
    difference = (player_number - comp_number) % 5
    
    # use if/elif/else to determine winner
    if difference == 1 or difference  == 2:
        result_string = "Player wins!"
        global player_wins
        player_wins += 1
    elif difference == 3 or difference == 4:
        result_string =  "Computer wins!"
        global computer_wins
        computer_wins += 1
    else:
        result_string = "Player and computer tie!"
        global ties
        ties += 1
        
    # convert comp_number to name using number_to_name
    comp_string =  "Computer chooses " + number_to_name(comp_number)
    
    # print results
    print player_string
    print comp_string
    print result_string + "\n"
    print_game_status()
    
#event handlers
def rock_handler():
    rpsls("rock")

def paper_handler():
    rpsls("paper")

def scissors_handler():
    rpsls("scissors")
    
def lizard_handler():
    rpsls("lizard")
    
def spock_handler():
    rpsls("Spock")
    
def reset_handler():
    init()
    
# Create frame and assign callbacks to event handlers
frame = simplegui.create_frame("GUI-based RPSLS", 300, 300)
frame.add_button("Rock",rock_handler,100)
frame.add_button("Paper",paper_handler,100)
frame.add_button("Scissors",scissors_handler,100)
frame.add_button("Lizard",lizard_handler,100)
frame.add_button("Spock",spock_handler,100)
frame.add_button("Reset Game",reset_handler,100)

# Start the frame animation
frame.start()
init()

