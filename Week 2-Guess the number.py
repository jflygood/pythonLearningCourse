# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console

import simplegui
import random

# helper function to start and restart the game
secret_num = 0
remain_guess_times = 7
msg = "New game. Range is from 0 to 100"
end_number = 100
initial_remain_guess_times = 7
def new_game():
    # initialize global variables used in your code here
    global secret_num
    global remain_guess_times
    secret_num = random.randrange(0,end_number)
    #print secret_num
    # remove this when you add your code
    print " "
    print msg
    print "Number of remaining guesses is " + str(remain_guess_times) 

# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global remain_guess_times
    global msg
    global end_number
    global initial_remain_guess_times
    msg = "New game. Range is from 0 to 100"
    remain_guess_times = 7
    end_number = 100
    initial_remain_guess_times = 7
    # remove this when you add your code  
    new_game()
    

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global remain_guess_times
    global msg
    global end_number
    global initial_remain_guess_times
    msg = "New game. Range is from 0 to 1000"
    remain_guess_times = 10
    end_number = 1000
    initial_remain_guess_times = 10
    new_game()
    
    
def input_guess(guess):
    # main game logic goes here	
    global remain_guess_times
    if remain_guess_times > 0:
        remain_guess_times -= 1 
    global initial_remain_guess_times
    result = "Correct"
    print "                                  "
    if (not guess.isdigit()):
        print "Your input is "+ str(guess)+". Please input integer number!"
        remain_guess_times += 1
        result = "Wront input!!!"
    elif (remain_guess_times>=0):
        print "Guess was " + str(guess)
        if(int(guess)>int(secret_num)):
            result = "Lower"
        elif(int(guess)<int(secret_num)):
            result = "Higher"
        elif(int(guess)==int(secret_num)):
            result = "Correct" 
        else:
            result = "Wront logic"      
    print 'Number of remaining guesses is ' + str(remain_guess_times)
    print result
    if remain_guess_times==0 and result != "Correct":
        print "Sorry! Game Over!!! You have no chance!!!"
        print "secret number is: " + str(secret_num)
        remain_guess_times = initial_remain_guess_times
        new_game()
    elif result == "Correct":
        remain_guess_times = initial_remain_guess_times
        new_game()
# create frame
frame  = simplegui.create_frame("Guess number", 200,200)
frame.add_button("Range is [0,100)",range100,200)
frame.add_button("Range is [0,1000)",range1000,200)
frame.add_input("Enter the guess number",input_guess,100)

# register event handlers for control elements and start frame


# call new_game 
new_game()
frame.start()
             


# always remember to check your completed program against the grading rubric
