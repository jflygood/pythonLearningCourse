# implementation of card game - Memory

import simplegui
import random

Width = 50
Height = 100
# helper function to initialize globals
def new_game():
    global exposed_list,state, turns,expose_index_list,number_dic
    state = 0
    turns  = 0
    expose_index_list=[]
    number_dic = {}
    number_list = range(8)
    second_list = range(8)
    number_list.extend(second_list)
    random.shuffle(number_list)
    i = 0
    for n in number_list:
        number_dic[i] = n
        i += 1
     
    exposed_list = []
    for j in range(16):
        exposed_list.append(False)   
    label.set_text("Turns = " + str(turns))
     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state,expose_index_list,turns    
    click_index = pos[0]/50
    if click_index in expose_index_list:
        return
    else:
        expose_index_list.append(click_index)
    if state==2 and (number_dic[expose_index_list[-2]]!=number_dic[expose_index_list[-3]]):
        expose_index_list.pop(-2)
        expose_index_list.pop(-2) 
    if state == 0:
        state = 1
    elif state == 1:
        state = 2
        turns +=1
        label.set_text("Turns = " + str(turns))
    else:
        state = 1
    print 'exposed_list--',exposed_list
    print 'state=',state
    print 'expose_index_list=',expose_index_list
# cards are logically 50x100 pixels in size    
def draw(canvas):
    i = 0
    for key,value in number_dic.items():
        #print exposed_list[key]
        if key in expose_index_list:
            canvas.draw_text(str(value), [Width*i+10,Height/2], 50, "White")
            canvas.draw_line([Width*(i+1),0], [Width*(i+1),Height], 1, "White")
        else:
            canvas.draw_polygon([[Width*i,0],[Width*(i+1),0],[Width*(i+1),Height],[50*i,Height]], 1, "Black","Green")
        i +=1


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", Width*16, Height)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()



# Always remember to review the grading rubric