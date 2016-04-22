# implementation of card game - Memory

import simplegui
import random

# global variables
cards = []
exposed = []
state = 1
card_1 = 0
card_2 = 0
card_1_index = 0
card_2_index = 0
turns = 0

# helper function to initialize globals
def init():
    global cards, exposed, state, turns
    state, turns = 0, 0
    cards = [i for i in range(8)] + [i for i in range(8)]
    random.shuffle(cards)
    exposed = [False for i in range(16)]
     
# define event handlers
def mouseclick(pos):
    global state, exposed, cards, turns, card_1, card_2, card_1_index, card_2_index
    index = pos[0] // 50
    #if already exposed do nothing
    if exposed[index] == True:
        return
    #if state 0 then get the first card and expose it
    if state == 0:
        exposed[index] = True
        card_1 = cards[index]
        card_1_index = int(index)
        state = 1
    #if state 1 get the second card and expose it
    elif state == 1:
        exposed[index] = True
        card_2 = cards[index]
        card_2_index = int(index)
        state = 2
        turns += 1
    #flip the cards back over if they do not match
    #get the next card that is selected
    elif state == 2:    
        if not(card_1 == card_2):
            exposed[card_1_index], exposed[card_2_index] = False, False
        state = 1
        exposed[index] = True
        card_1 = cards[index]
        card_1_index = int(index)
        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global cards
    space = 0
    position = 0
    for num in cards:
        if exposed[position]:
             canvas.draw_text(str(num), [space+11, (50 - 50 / 3.75)+25], 50, "White")
        else:
            canvas.draw_polygon([(space, 0), (space + 50, 0), (space + 50, 100), (space, 100)], 2, "White", "Green")
        space += 50
        position += 1
    l.set_text("Moves = " + str(turns))

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Restart", init)
l=frame.add_label("Moves = 0")

# initialize global variables
init()

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
frame.start()


# Always remember to review the grading rubric