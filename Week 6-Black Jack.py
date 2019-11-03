# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome1 = ""
outcome2 = ""
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
    def draw_bak(self,canvas,pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0],CARD_CENTER[1])
        canvas.draw_image(card_back, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        # create Hand object
        self.handlist=[]

    def __str__(self):
        # return a string representation of a hand
        str="Hand contains "
        for item in self.handlist:
            str += item.get_suit() + item.get_rank()+" "
        return str
    def add_card(self, card):
        # add a card object to a hand
        self.handlist.append(card)

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        value=0
        hasAce= False
        for item in self.handlist:
            value +=VALUES[item.rank]
        for item in self.handlist:
            if "A"==item.rank:
                hasAce = True
                break
        if hasAce and value+10<21:
            value +=10
        return value
        
    def draw_card_image(self,canvas,pos):
        for idx in range(len(self.handlist)):
            if idx !=0 and idx<5:
                self.handlist[idx].draw(canvas,pos)
                pos[0]= pos[0] + CARD_SIZE[0] + 15
            
    def draw_card_back(self,canvas,pos):
        self.handlist[0].draw_bak(canvas,pos)
    
    def draw(self, canvas, pos):
        # draw a hand on the canvas, use the draw method for cards
        i=0
        for item in self.handlist:
            if i<5:
                item.draw(canvas,pos)
                pos[0]= pos[0] + CARD_SIZE[0] + 15
                i +=1
                
# define deck class 
class Deck:
    def __init__(self):
        # create a Deck object
        self.decklist=[]
        for suit in SUITS:
            for ranks in RANKS:
                card=Card(suit,ranks)
                self.decklist.append(card)
                
    def shuffle(self):
        # shuffle the deck 
        # use random.shuffle()
        random.shuffle(self.decklist)

    def deal_card(self):
        # deal a card object from the deck
        deal_card= self.decklist[-1]
        self.decklist.pop()
        return deal_card
    
    
    def __str__(self):
        # return a string representing the deck
        str="Deck contains "
        for item in self.decklist:
            str += item.get_suit() + item.get_rank()+" "
        return str	

#define event handlers for buttons
def deal():
    global outcome1,outcome2,score, in_play,test_deck,playerhand,dealerhand
    if in_play:
        outcome1 = "You lose!"
        outcome2 = "New deal?"
        score -=1
        in_play = False
        return
    # your code goes here
    test_deck=Deck()
    #print test_deck
    test_deck.shuffle()
    #print test_deck
    dealerhand=Hand()
    playerhand=Hand()
    dealerhand.add_card(test_deck.deal_card())
    playerhand.add_card(test_deck.deal_card())
    dealerhand.add_card(test_deck.deal_card())
    playerhand.add_card(test_deck.deal_card())
    #print test_deck
    outcome1 = ""
    outcome2 = "Hit or stand?"
    in_play = True

def hit():
    global outcome1,outcome2, in_play,test_deck,playerhand,dealerhand,score
    # replace with your code below
 
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
    if in_play:
        playerhand.add_card(test_deck.deal_card())
        if playerhand.get_value()>21:
            outcome1 = "You have busted and lose"
            outcome2 = "New Deal?"
            in_play = False
            score -= 1
        else:
            outcome2="Hit or stand?"
#    print "dealerhand=",dealerhand,"  Value=",dealerhand.get_value()
#    print "playerhand=",playerhand,"  Value=",playerhand.get_value()
#    print score
        
def stand():
    global outcome1,outcome2, in_play,test_deck,playerhand,dealerhand,score
    # replace with your code below
   
    # if hand is in play, repeatedly hit dealer until his hand has value 17 or more

    # assign a message to outcome, update in_play and score
    if in_play:
        if playerhand.get_value()>21:
            outcome = "You have busted!"
            in_play = False
            score -= 1
        else:
            while dealerhand.get_value()<17:
                dealerhand.add_card(test_deck.deal_card())
            if dealerhand.get_value()>21:
                outcome1 = "Dealer have busted!"
                outcome2 = "New deal?"
                score +=1
                in_play = False
            else:
                if playerhand.get_value()<=dealerhand.get_value():
                    outcome1 = "You lose! Dealer win"
                    outcome2 = "New deal?"
                    score -=1
                    in_play = False
                else:
                    outcome1 = "You Win!"
                    outcome2 = "New deal?"
                    score +=1
                    in_play = False
#    print "dealerhand=",dealerhand,"  Value=",dealerhand.get_value()
#    print "playerhand=",playerhand,"  Value=",playerhand.get_value()
#    print score
        
            

# draw handler    
def draw(canvas):
    # test to make sure that card.draw works, replace with your code below
    global outcome1,outcome2,score
    canvas.draw_text('Blackjack', (50, 80), 60, 'Blue','serif')
    canvas.draw_text("Score",(340,80),35,'Black','serif')
    canvas.draw_text(str(score),(430,80),35,'Black','serif')
    
    canvas.draw_text('Dealer',(40,150),35,'Black','serif')
    canvas.draw_text('Player',(40,350),35,'Black','serif')
    canvas.draw_text(outcome1,(240,150),35,'Black','serif')
    canvas.draw_text(outcome2,(240,350),35,'Black','serif')
    if in_play:
        dealerhand.draw_card_back(canvas,[40,180])
        dealerhand.draw_card_image(canvas,[40+CARD_SIZE[0] + 15,180])
    else:
        dealerhand.draw(canvas,[40,180])
    playerhand.draw(canvas,[40,380])
#    card = Card("C", "2")
#    card.draw(canvas, [300, 300])


# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric