import turtle
import random
s=turtle.getscreen()
t=turtle.Turtle()
c=turtle.Turtle()

#player1
t.shape("turtle")
t.penup()
t.goto(-400,200)
t.color("red","blue")
t.shapesize(3,3,3)
t.speed(6)
t.penup()
t.goto(300,200)
t.pendown()
t.circle(50)
t.penup()
t.goto(-400,200)
t.pendown()

#player2
c.shape("turtle")
c.penup()
c.goto(-400,-200)
c.color("green","pink")
c.shapesize(3,3,3)
c.speed(6)
c.penup()
c.goto(300,-200)
c.pendown()
c.circle(50)
c.penup()
c.goto(-400,-200)
c.pendown()

#dice
d=[1,2,3,4,5,6]
#game
for i in range(40) :
    if t.pos() >= (300,200) :
        print("player 1 win")
        break
    elif c.pos() >= (300,-200) :
        print("player 2 win")
        break
    else :
        input("player 1 to play (press enter)")
        die1=random.choice(d)
        print("die number",die1,"!")
        t.fd(die1*20)
        input("player 2 to play (press enter)")
        die2=random.choice(d)
        print("die number",die2,"!")
        c.fd(die2*20)
input("tq")
