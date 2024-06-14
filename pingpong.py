import turtle

screen = turtle.Screen()
screen.title("PING PONG")
screen.bgcolor("Blue")
screen.setup(width=800,height=600)

paddle_1 = turtle.Turtle()
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5,stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350,0)

paddle_2 = turtle.Turtle()
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5,stretch_len=1)
paddle_2.penup()
paddle_2.goto(350,0)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0,0)
ball.dx = 5
ball.dy = -5

score_1 = 0
score_2 = 0
score_text = turtle.Turtle()
score_text.color("white")
score_text.hideturtle()
score_text.penup()
score_text.write("PLAYER 1 : 0  PLAYER 2 : 0",align="center",font=("courier",24,"normal"))



def checkColl():
    if(paddle_1.xcor() + 20 >= ball.xcor() >= paddle_1.xcor()-20 and paddle_1.ycor() + 60 >= ball.ycor() >= paddle_1.ycor()-60):
        ball.dx = ball.dx * -1
        ball.dy = ball.dy * -1

        x = ball.xcor()
        x = x + 10
        ball.setx(x)

    if(paddle_2.xcor() + 20 >= ball.xcor() >= paddle_2.xcor()-20 and paddle_2.ycor() + 60 >= ball.ycor() >= paddle_2.ycor()-60):
        ball.dx = ball.dx * -1
        ball.dy = ball.dy * -1

        x = ball.xcor()
        x = x - 10
        ball.setx(x)

def move_ball():
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    x = ball.xcor()
    y = ball.ycor()

    if y > 290:
        ball.sety(290)
        ball.dy = ball.dy * -1

    if y < -290:
        ball.sety(-290)
        ball.dy = ball.dy * -1

    if x > 390:
        ball.setx(390)
        ball.dx = ball.dx * -1

    if x < -390:
        ball.setx(-390)
        ball.dx = ball.dx * -1

def paddle_1_up():
    y = paddle_1.ycor()
    y = y + 10
    paddle_1.sety(y)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if y>240:
        paddle_1.sety(240)

def paddle_1_right():
    x = paddle_1.xcor()
    x = x + 10
    paddle_1.setx(x)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if x>0:
        paddle_1.setx(0)

def paddle_1_left():
    x = paddle_1.xcor()
    x = x - 10
    paddle_1.setx(x)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if x<-340:
        paddle_1.setx(-350)

def paddle_1_down():
    y = paddle_1.ycor()
    y = y - 10
    paddle_1.sety(y)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if y<-240:
        paddle_1.sety(-240)

def paddle_2_right():
    x = paddle_2.xcor()
    x = x + 10
    paddle_2.setx(x)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if x>340:
        paddle_2.setx(350)

def paddle_2_left():
    x = paddle_2.xcor()
    x = x - 10
    paddle_2.setx(x)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if x<0:
        paddle_2.setx(0)

def paddle_2_up():
    y = paddle_2.ycor()
    y = y + 10
    paddle_2.sety(y)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if y>240:
        paddle_2.sety(240)

def paddle_2_down():
    y = paddle_2.ycor()
    y = y - 10
    paddle_2.sety(y)
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if y<-240:
        paddle_2.sety(-240)

screen.listen()
screen.onkeypress(paddle_1_right,"d")
screen.onkeypress(paddle_1_left,"a")
screen.onkeypress(paddle_2_left,"Left")
screen.onkeypress(paddle_2_right,"Right")
screen.onkeypress(paddle_1_down,"s")
screen.onkeypress(paddle_2_down,"Down")
screen.onkeypress(paddle_1_up,"w")
screen.onkeypress(paddle_2_up,"Up")

while(1):
    screen.update()
    move_ball()
    checkColl()
    if ball.xcor()>=350:
        score_1 = score_1 + 1
        score_text.clear()
        score_text.write("PLAYER 1 : {}  PLAYER 2 : {}".format(score_1,score_2),align="center",font=("courier",24,"normal"))
        ball.goto(0,0)
        ball.dx = ball.dx * -1

    if ball.xcor()<= -350:
        score_2 = score_2 + 1
        score_text.clear()
        score_text.write("PLAYER 1 : {}  PLAYER 2 : {}".format(score_1,score_2),align="center",font=("courier",24,"normal"))
        ball.goto(0,0)
        ball.dx = ball.dx * -1