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
paddle1_pos = HEIGHT / 2
paddle1_vel = 0
paddle2_pos = HEIGHT / 2
paddle2_vel = 0
ball_pos = [int(WIDTH / 2), int(HEIGHT / 2)]
ball_vel = [1, 1]
score1 = 0
score2 = 0
acc = 3

# helper function that spawns a ball by updating the 
# ball's position vector and velocity vector
# if right is True, the ball's velocity is upper right, else upper left
def ball_init(right):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos = [int(WIDTH / 2), int(HEIGHT / 2)]
    if right:
        ball_vel = [random.randrange(120, 240) / 60, - random.randrange(60, 180) / 60]
    else:
        ball_vel = [- random.randrange(120, 240) / 60, - random.randrange(60, 180) / 60]


# define event handlers

def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are floats
    global score1, score2  # these are ints
    global ball_pos, ball_vel
    paddle1_pos = HEIGHT / 2
    paddle1_vel = 0
    paddle2_pos = HEIGHT / 2
    paddle2_vel = 0
    ball_init(True)
    score1 = 0
    score2 = 0

def draw(c):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel
    
    # update paddle's vertical position, keep paddle on the screen
    if (paddle1_pos + paddle1_vel) < HALF_PAD_HEIGHT:
        paddle1_pos = HALF_PAD_HEIGHT
    elif (paddle1_pos + paddle1_vel) > HEIGHT - HALF_PAD_HEIGHT:
        paddle1_pos = HEIGHT - HALF_PAD_HEIGHT
    else:
        paddle1_pos += paddle1_vel
    
    if (paddle2_pos + paddle2_vel) < HALF_PAD_HEIGHT:
        paddle2_pos = HALF_PAD_HEIGHT
    elif (paddle2_pos + paddle2_vel) > HEIGHT - HALF_PAD_HEIGHT:
        paddle2_pos = HEIGHT - HALF_PAD_HEIGHT
    else:
        paddle2_pos += paddle2_vel
        
    # draw mid line and gutters
    c.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    c.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    c.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    
    # draw paddles
    c.draw_line([0, paddle1_pos - HALF_PAD_HEIGHT], [0, paddle1_pos + HALF_PAD_HEIGHT], PAD_WIDTH + 6, "White")
    c.draw_line([WIDTH, paddle2_pos - HALF_PAD_HEIGHT], [WIDTH, paddle2_pos + HALF_PAD_HEIGHT], PAD_WIDTH + 6, "White")
    
    # update ball
    #check top and bottom wall collisions
    if ball_pos[1] >= (HEIGHT - BALL_RADIUS):
        ball_vel[1] = - ball_vel[1]
    elif ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
        
    #check left and right gutters
    if ball_pos[0] >= (WIDTH - PAD_WIDTH - BALL_RADIUS):
        if ball_pos[1] <= paddle2_pos + HALF_PAD_HEIGHT and ball_pos[1] >= paddle2_pos - HALF_PAD_HEIGHT:
            ball_vel[0] = - (1.1 * ball_vel[0])
            ball_vel[1] = 1.1 * ball_vel[1]
        else:
            ball_init(False)
            score1 += 1
    elif ball_pos[0] <= (PAD_WIDTH + BALL_RADIUS):
        if ball_pos[1] <= paddle1_pos + HALF_PAD_HEIGHT and ball_pos[1] >= paddle1_pos - HALF_PAD_HEIGHT:
            ball_vel[0] = - (1.1 * ball_vel[0])
            ball_vel[1] = 1.1 * ball_vel[1]
        else:
            ball_init(True)
            score2 += 1
     
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
            
    # draw ball and scores
    c.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "White")
    c.draw_text(str(score1), [WIDTH / 2 - 100, 100], 72, "White", "sans-serif")
    c.draw_text(str(score2), [WIDTH / 2 + 50, 100], 72, "White", "sans-serif")
        
def keydown(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = -1 * acc
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel = -1 * acc
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = acc
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = acc
   
def keyup(key):
    global paddle1_vel, paddle2_vel
    if key == simplegui.KEY_MAP['up']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['w']:
        paddle1_vel = 0
    elif key == simplegui.KEY_MAP['down']:
        paddle2_vel = 0
    elif key == simplegui.KEY_MAP['s']:
        paddle1_vel = 0


# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", new_game, 100)


# start frame
frame.start()
new_game()
ball_init(True)
