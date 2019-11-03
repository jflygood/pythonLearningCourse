# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions
"""
Scissors cuts paper, 
paper covers rock. 
Rock crushes lizard, 
lizard poisons Spock. 
Spock smashes scissors,
scissors decapitates lizard. 
Lizard eats paper, 
paper disproves Spock,
Spock vaporizes rock, 
and as always has been, rock crushes scissors.
"""
import random

def name_to_number(name):
    # delete the following pass statement and fill in your code below

    # convert name to number using if/elif/else
    # don't forget to return the result!
    if name == "rock":
        a=0
    elif name == "spock":
        a=1
    elif name == "paper":
        a=2
    elif name == "lizard":
        a=3
    elif name == "scissors":
        a=4
    else:
        a=-1
        print "Name is incorrect. Name should be one of:rock,spock,paper,lizard,scissors"
    return a


def number_to_name(number):
    # delete the following pass statement and fill in your code below
    
    # convert number to a name using if/elif/else
    # don't forget to return the result!
    if number == 0:
        name = "rock"
    elif number == 1:
        name = "spock"
    elif number == 2:
        name = "paper"
    elif number == 3:
        name = "lizard"
    elif number == 4:
        name = "scissors"
    else:
        name = "invalid number"
    return name

def compare_rule(a_num,b_num):
    if a_num==b_num:
        result = 0
    elif a_num==4 and b_num==2:
        result = 1
    elif a_num==2 and b_num==0:
        result = 1
    elif a_num==0 and b_num==3:
        result = 1
    elif a_num==3 and b_num==1:
        result = 1
    elif a_num==1 and b_num==4:
        result = 1
    elif a_num==4 and b_num==3:
        result = 1
    elif a_num==3 and b_num==2:
        result = 1
    elif a_num==2 and b_num==1:
        result = 1
    elif a_num==1 and b_num==0:
        result = 1
    else:
        result = 2
    return result
"""
if (a-b)%5 ==3 or == 4 lose
if (a-b)%5 ==1 or ==2 win
if==0 draw
"""
def compare_rule1(a_num,b_num):
    if (a_num-b_num)%5==0:
        result = 0
    elif  (a_num-b_num)%5==1 or (a_num-b_num)%5==2:
        result = 1
    elif (a_num-b_num)%5==3 or (a_num-b_num)%5==4:
        result = 2
    else:
        result = -1
    return result
        
   # (a_num-b_num)%5==2 or (a_num-b_num)%5==4:
        
def rpsls(player_choice): 
    # delete the following pass statement and fill in your code below
   
    # print a blank line to separate consecutive games
    # print out the message for the player's choice
    # convert the player's choice to player_number using the function name_to_number()
    # compute random guess for comp_number using random.randrange()

    # convert comp_number to comp_choice using the function number_to_name()
    
    # print out the message for computer's choice
    # compute difference of comp_number and player_number modulo five

    # use if/elif/else to determine winner, print winner message
    print "                                                            "    
    print "Player chooses " + player_choice
    player_number = name_to_number(player_choice)
    if player_number==-1:
       return
    comp_number = random.randrange(0,5)
    comp_choice = number_to_name(comp_number)
    print "Computer chooses " + comp_choice
    
    result=compare_rule(player_number,comp_number)
    if result==0:
        print "Computer and Player draw!!!"
    elif result==1:
        print "Player wins!"
    elif result==2:
        print "Computer wins!"
    else:
        print "Invalid Game!"
    print "-----------------------------------------"    
    result=compare_rule1(player_number,comp_number)
    if result==0:
        print "Computer and Player draw!!!"
    elif result==1:
        print "Player wins!"
    elif result==2:
        print "Computer wins!"
    else:
        print "Invalid Game!"
    



    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

# always remember to check your completed program against the grading rubric


