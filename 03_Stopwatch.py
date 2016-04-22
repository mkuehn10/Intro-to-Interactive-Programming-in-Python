# template for "Stopwatch: The Game"
import simplegui

# define global variables
counter = 0
success = 0
attempts = 0

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    minutes_str = str(t // 600)
    seconds = (t % 600) // 10
    if seconds < 10:
        seconds_str = '0' + str(seconds)
    else:
        seconds_str = str(seconds)
    tenths_str = str((t % 600) % 10)
    return minutes_str + ":" + seconds_str + "." + tenths_str
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()

def stop_handler():
    # do nothing if timer is already stopped
    if not timer.is_running():
        return
    # stop the timer, check for success
    timer.stop()
    global counter, success, attempts
    if (counter % 10) == 0:
        success += 1
        attempts += 1
    else:
        attempts += 1

def reset_handler():
    timer.stop()
    global counter, success, attempts
    counter, success, attempts = 0, 0, 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global counter
    counter += 1
    
def draw_handler(canvas):
    global counter, success, attempts
    canvas.draw_text(format(counter), ((300 - f.get_canvas_textwidth(format(counter), 72, "sans-serif")) / 2, (300 / 2) + (72 / 3.75)), 72, "Red", "sans-serif")
    canvas.draw_text(str(success) + "/" + str(attempts), (300 - f.get_canvas_textwidth(str(success) + "/" + str(attempts),24, "sans-serif"), 24 - (24 / 3.75)), 24, "Red", "sans-serif")

# create frame
f = simplegui.create_frame("Stopwatch", 300, 300)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
f.add_button("Start", start_handler, 100)
f.add_button("Stop", stop_handler, 100)
f.add_button("Reset", reset_handler, 100)
f.set_draw_handler(draw_handler)

# start timer and frame
f.start()