import turtle

wn = turtle.Screen()
wn.title("Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# paddle1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350, 0)

# paddle2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 2
ball.dy = 2
# paddles movement 
def paddle_1_up():
	y = paddle_1.ycor()
	y += 20
	paddle_1.sety(y)

def paddle_1_down():
	y = paddle_1.ycor()
	y -= 20
	paddle_1.sety(y)

def paddle_2_up():
	y = paddle_2.ycor()
	y += 20
	paddle_2.sety(y)

def paddle_2_down():
	y = paddle_2.ycor()
	y -= 20
	paddle_2.sety(y)

wn.listen()
wn.onkeypress(paddle_1_up, "w")
wn.onkeypress(paddle_1_down, "s")
wn.onkeypress(paddle_2_up, "Up")
wn.onkeypress(paddle_2_down, "Down")

while True:
	wn.update()
	
	
	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)