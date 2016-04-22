# Mini-project #6 - Blackjack
import simplegui
import random

# load card sprite - 949x392 - source: jfitz.com
CARD_SIZE = (73, 98)
CARD_CENTER = (36.5, 49)
card_images = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/cards.jfitz.png")

CARD_BACK_SIZE = (71, 96)
CARD_BACK_CENTER = (35.5, 48)
card_back = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/card_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards = []	# create Hand object
        #self.hand_value = 0

    def __str__(self):
        hand_string = ""
        for element in self.cards:
            hand_string += str(element) + " "
        return "Hand contains " + hand_string # return a string representation of a hand

    def add_card(self, card):
        self.cards.append(card)	# add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        hand_value = 0
        hand_ranks = []
        for element in self.cards:
            hand_value += VALUES[element.get_rank()]
            hand_ranks.append(element.get_rank())
        
        if 'A' not in hand_ranks:
            return hand_value
        else:
            if hand_value + 10 <= 21:
                return hand_value + 10
            else:
                return hand_value
   
    def draw(self, canvas, pos):
        offset = 100
        n = 0
        for element in self.cards:
            element.draw(canvas, [pos[0] + n * offset, pos[1]])
            n += 1
            # draw a hand on the canvas, use the draw method for cards
 
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards = []
        for suit in SUITS:
            for rank in RANKS:
                next_card = Card(suit, rank)
                self.cards.append(next_card)
                # create a Deck object

    def shuffle(self):
        # add cards back to deck and shuffle
        random.shuffle(self.cards)	# use random.shuffle() to shuffle the deck

    def deal_card(self):
        return self.cards.pop()	# deal a card object from the deck
    
    def __str__(self):
        deck_string = ""
        for element in self.cards:
            deck_string += str(element) + " "
        return deck_string	# return a string representing the deck
    
deck = Deck()
player_hand = Hand()
dealer_hand = Hand()

#define event handlers for buttons
def deal():
    global outcome, in_play, deck, player_hand, dealer_hand, score
    if in_play:
        score -= 1
    # your code goes here
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    deck.shuffle()
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    player_hand.add_card(deck.deal_card())
    dealer_hand.add_card(deck.deal_card())
    in_play = True
    outcome = "Hit or Stand?"

def hit():
    global in_play, score, outcome
    if in_play:
        player_hand.add_card(deck.deal_card())
        outcome = "Hit or Stand?"
    else:
        return
    if player_hand.get_value() > 21:
        outcome = "Player has busted! Dealer wins! New Deal?"
        score -= 1
        in_play = False
       
def stand():
    global in_play, score, outcome
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more
    if in_play:
        while dealer_hand.get_value() < 17:
            dealer_hand.add_card(deck.deal_card())
    else:
        return
    
    # assign a message to outcome, update in_play and score
    if dealer_hand.get_value() > 21:
        outcome = "Dealer has busted! Player wins! New Deal?"
        score += 1
        in_play = False
    elif player_hand.get_value() <= dealer_hand.get_value():
        outcome = "Dealer wins! New Deal?"
        score -= 1
        in_play = False
    else:
        outcome = "Player wins! New Deal?"
        score += 1
        in_play = False
    
# draw handler    
def draw(canvas):
    player_hand.draw(canvas, [50, 400])
    dealer_hand.draw(canvas, [50, 100])
    
    if in_play:
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [50 + CARD_BACK_SIZE[0] / 2,100 + CARD_BACK_SIZE[1] / 2], CARD_BACK_SIZE)
    canvas.draw_text(outcome, [50, 300], 24, "White", "sans-serif")
    canvas.draw_text("Score: " + str(score), [375, 75], 24, "White", "sans-serif")



# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)

# deal an initial hand

# get things rolling
frame.start()
outcome = "Select Deal to start!"


# remember to review the gradic rubric