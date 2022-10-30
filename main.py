import turtle

# window
wn = turtle.Screen()
# the title of the window will be 'pong_game'
wn.title("fala's pong_game")
# a classic 'pong' color way
wn.bgcolor("black")
# resizing window to a playable size
wn.setup(width = 800, height = 600)
# stops updates to window/game
wn.tracer(0) # (cl.1)

# score
score_a = 0
score_b = 0

# left paddle
l_paddle = turtle.Turtle()
# speed of animation; max possible speed; otherwise-->slow
l_paddle.speed(0)
# NOTE: (will change)
l_paddle.shape('square')
# classic 'pong' paddle color
l_paddle.color('white')
# to resize the 'square' to a classic paddle shape
l_paddle.shapesize(stretch_wid = 5, stretch_len = 1)
# line to goto() will not be drawn.
l_paddle.penup()
# l_paddle is shown on the left of the screen
l_paddle.goto(-350, 0)



# right paddle
r_paddle = turtle.Turtle()
# speed of animation; max possible speed; otherwise-->slow
r_paddle.speed(0)
# NOTE: (will change)
r_paddle.shape('square')
# classic 'pong' paddle color
r_paddle.color('white')
# to resize the 'square' to a classic paddle shape
r_paddle.shapesize(stretch_wid = 5, stretch_len = 1)
# line to goto() will not be drawn.
r_paddle.penup()
# r_paddle is shown on the right of the screen
r_paddle.goto(350, 0)

# ball
ball = turtle.Turtle()
# speed of animation; max possible speed; otherwise-->slow
ball.speed(0)
# a circle is made
ball.shape('circle')
# classic 'pong' ball color
ball.color('white')
# line to goto() will not be drawn.
ball.penup()
# ball is shown in the middle of the screen
ball.goto(0, 0)
# 'x' and 'y' movements (by x pixels)
ball.dx = 2
ball.dy = -2

#pen (the score count)
pen = turtle.Turtle()
# animation speed; NOTE:(not really animation though)
pen.speed(0)
# classic 'pong'color way
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player A: 0 Player B: 0', align = 'center', font = ('Courier', 24, 'normal'))


# l_paddle movement up/down
# function
def l_paddle_up():
    y = l_paddle.ycor() # '.ycor()' returns 'y' coordinate
    y += 20 # (y = y+20) # as 'y' increases, l_paddle moves up
    l_paddle.sety(y)

def l_paddle_down():
    y = l_paddle.ycor() # '.ycor()' returns 'y' coordinate
    y -= 20 # (y = y-20) # as 'y' decreases, l_paddle moves down
    l_paddle.sety(y)

def r_paddle_up():
    y = r_paddle.ycor()  # '.ycor()' returns 'y' coordinate
    y += 20  # (y = y+20) # as 'y' increases, r_paddle moves up
    r_paddle.sety(y)

def r_paddle_down():
    y = r_paddle.ycor()  # '.ycor()' returns 'y' coordinate
    y -= 20  # (y = y-20) # as 'y' decreases, r_paddle moves down
    r_paddle.sety(y)

# calling the function 'l_paddle_up()'
# keyboard binding
wn.listen() # 'listens' for keyboard input
wn.onkeypress(l_paddle_up, 'w') # l_paddle moves up when 'w' is pressed; NOTICE: will not work with 'W', not inputted in 'keyboard_binding'
wn.onkeypress(l_paddle_down, 's') # l_paddle moves down when 's' is pressed; NOTICE: will not work with 'S', not inputted in 'keyboard_binding'
wn.onkeypress(r_paddle_up, 'Up') # the 'Up', NOTICE: capital U in 'Up' is the Up arrow key
wn.onkeypress(r_paddle_down, 'Down') # the 'Down', NOTICE: capital D in 'Down' is the Down arrow key


# main game loop
while True:
    wn.update() # refer to (cl.1) # everytime the loop runs, screen updates
    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290: # difference in terms of ball height and screen height
        ball.sety(290)
        # reverses direction
        ball.dy *= -1

    if ball.ycor() < -290: # difference in terms of ball height and screen height
        ball.sety(-290)
        # reverses direction
        ball.dy *= -1

    if ball.xcor() > 390: # if ball passes the paddle form the right; ball is off screen
        ball.goto(0, 0)
        ball.dx *= -1
        # score for player 1
        score_a += 1
        # so the scores don't overlap (clears screen; too fast)
        pen.clear()
        pen.write('Player A: {} Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))

    if ball.xcor() < -390: # if ball passes the paddle form the left; ball is off screen
        ball.goto(0, 0)
        # reverses direction
        ball.dx *= -1
        # score for player 2
        score_b += 1
        # so the scores don't overlap (clears screen; too fast)
        pen.clear()
        pen.write('Player A: {} Player B: {}'.format(score_a, score_b), align='center', font=('Courier', 24, 'normal'))

    # r_paddle collison with ball
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < r_paddle.ycor() + 40 and ball.ycor() > r_paddle.ycor() - 40):
        # reverses direction
        ball.setx(340)
        ball.dx *= -1

    # l_paddle collison with ball
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < l_paddle.ycor() + 40 and ball.ycor() > l_paddle.ycor() - 40):
        # reverses ball direction
        ball.setx(-340)
        ball.dx *= -1
