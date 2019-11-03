# template for "Stopwatch: The Game"

# define global variables
import simplegui
total_time = 0
timer_display = "0:00:0"
win_times_display = "0/0"
position_timer = [200,200]
position_win = [300,50]
interval = 1 # 0.1 second
win_times = 0
total_try_times = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global timer_display
    minute = t/(600)
    second = (t-minute*600)/10
    tenth_second = t-minute*600-second*10
    if second<10:
        str_second = "0"+str(second)
    else:
        str_second = str(second)
    timer_display = str(minute) + ":" + str(str_second) + "." + str(tenth_second)
    
    
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_watch():
    timer.start()

def stop_watch():
    timer.stop()
    global total_times
    global total_try_times
    global win_times
    global win_times_display
    if total_time ==0:
        return
    if total_time%50 == 0:
        win_times += 1
    total_try_times += 1
    win_times_display = str(win_times) + "/" + str(total_try_times)
    

def reset():
    timer.stop()
    global timer_display 
    global win_times_display 
    global win_times 
    global total_try_times 
    global total_time 
    timer_display = "0:00:0"
    win_times_display= "0/0"
    win_times= 0
    total_try_times = 0
    total_time = 0

# define event handler for timer with 0.1 sec interval
def tick():
    global interval
    global total_time
    total_time += interval
    format(total_time)
    

# define draw handler
def draw(canvas):
    canvas.draw_text(timer_display, position_timer, 36, "Red")
    canvas.draw_text(win_times_display, position_win, 36, "Red")
    
# create frame
frame = simplegui.create_frame("Stop watch", 400,400)


# register event handlers
frame.add_button("Start",start_watch, 100)
frame.add_button("Stop",stop_watch,100)
frame.add_button("Reset",reset,100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(interval*100,tick)


# start frame
frame.start()

# Please remember to review the grading rubric
