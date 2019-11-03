# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH = 600
HEIGHT = 400       
BALL_RADIUS = 20
PAD_WIDTH = 8
PAD_HEIGHT = 80
HALF_PAD_WIDTH = PAD_WIDTH / 2
HALF_PAD_HEIGHT = PAD_HEIGHT / 2
LEFT = False
RIGHT = True
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [WIDTH / 2, HEIGHT / 2]
    if(direction=="Right"):
        ball_vel = [random.randrange(2, 4), random.randrange(1, 3)]
    elif(direction=="Left"):
        ball_vel = [-random.randrange(2, 4), random.randrange(1, 3)]
    #print ball_pos
    #print ball_vel
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel # these are numbers
    global score1, score2  # these are ints
    paddle1_pos=HEIGHT/2
    paddle2_pos=HEIGHT/2
    score1=0
    score2=0
    paddle1_vel=0
    paddle2_vel=0
    direction=random.randrange(2)
    if(direction==0):
        spawn_ball("Left")
    elif(direction==1):
        spawn_ball("Right")
    
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos
    global ball_vel,LEFT,RIGHT,score1,score2
 
        
    # draw mid line and gutters
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
        
    # update ball
    # determine whether paddle and ball collide 
    
    
    if(ball_pos[1]<=BALL_RADIUS or ball_pos[1]>=HEIGHT-BALL_RADIUS):
        ball_vel[1] = -ball_vel[1] 
    if(ball_pos[0]<=BALL_RADIUS+PAD_WIDTH):
        if paddle1_pos-40<=ball_pos[1]<=paddle1_pos+40:
            ball_vel[0]=1.1* ball_vel[0]
            #ball_vel[1]=1.1* ball_vel[1]
            ball_vel[0] = -ball_vel[0]
        else:
            RIGHT = True
            LEFT = False
            score2 +=1
            spawn_ball("Right")
    if(ball_pos[0]>=WIDTH -BALL_RADIUS-PAD_WIDTH):
        if paddle2_pos-40<=ball_pos[1]<=paddle2_pos+40:
            ball_vel[0]=1.1* ball_vel[0]
            #ball_vel[1]=1.1* ball_vel[1]
            ball_vel[0] = -ball_vel[0]
        else:
            LEFT=True
            RIGHT = False
            score1 +=1
            spawn_ball("Left")
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]   
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")     
    
    
    # update paddle's vertical position, keep paddle on the screen
    if((paddle1_pos+paddle1_vel>=HALF_PAD_HEIGHT) and (paddle1_pos +paddle1_vel<=HEIGHT-HALF_PAD_HEIGHT) ):
         paddle1_pos += paddle1_vel
    if((paddle2_pos + paddle2_vel>=HALF_PAD_HEIGHT)and(paddle2_pos + paddle2_vel<=HEIGHT-HALF_PAD_HEIGHT)):
        paddle2_pos += paddle2_vel
   
    # draw paddles
    canvas.draw_polygon([(0,paddle1_pos-HALF_PAD_HEIGHT), (PAD_WIDTH,paddle1_pos-HALF_PAD_HEIGHT),
                         (PAD_WIDTH, paddle1_pos+HALF_PAD_HEIGHT),(0,paddle1_pos+HALF_PAD_HEIGHT)], 1, 'White', 'White')
    canvas.draw_polygon([(WIDTH-PAD_WIDTH,paddle2_pos-HALF_PAD_HEIGHT), (WIDTH,paddle2_pos-HALF_PAD_HEIGHT),
                         (WIDTH, paddle2_pos+HALF_PAD_HEIGHT),(WIDTH-PAD_WIDTH,paddle2_pos+HALF_PAD_HEIGHT)], 1, 'White', 'White')     
    
    # draw scores
    canvas.draw_text(str(score1), (WIDTH/2-150,50), 45, "White")
    canvas.draw_text(str(score2), (WIDTH/2+150,50), 45, "White")
        
def keydown(key):
    global paddle1_vel, paddle2_vel,ball_vel
    current_key = chr(key)
    if(current_key in "wW"):
        paddle1_vel =-8
    elif(current_key in "sS"):
        paddle1_vel =8
    if key == simplegui.KEY_MAP["down"]:
        paddle2_vel = 8
    elif key == simplegui.KEY_MAP["up"]:
        paddle2_vel = -8  
    if (current_key in "vV"):
        ball_vel[0]=2*ball_vel[0]
    elif (current_key in "bB"):
        ball_vel[0]=ball_vel[0] /2
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    paddle1_vel=0
    paddle2_vel=0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.add_button("Restart",new_game, 100)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)

# start frame
new_game()
frame.start()
