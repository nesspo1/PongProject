from tkinter.messagebox import ERROR
import turtle
#import pygame
import time
import tkinter as tk
wn = turtle.Screen()
wn.setup(800,600)
root = wn._root
root.resizable(width=False,height=False)

ballimg = "C:/Users/dakot/source/repos/PongClone/Pong/Images/piggy.gif"
backround = "C:/Users/dakot/source/repos/PongClone/Pong/Images/backround.gif"
wn.addshape(ballimg)
wn.addshape(backround)
wn.bgpic(backround)
global left_score 
left_score = 0
global right_score 
right_score = 0
text = turtle.Turtle()
text.pu()
text.hideturtle()
text.goto(0,200)
text.write("                W and S keys move the left side.\n      Up arrow and Down arrow move the right side.\nPress Z to hide this text, Escape key to quit the game",align="center",font=("Arial",15,"normal"))
start = False
score_text = turtle.Turtle()
score_text.pu()
score_text.hideturtle()
score_text.color("Purple")
score_text.goto(0, 150)
def write_score():
    score_text.clear()
    score_text.write("Player 1 score:"+str(left_score)+"            Player 2 score:"+str(right_score),align="center",font=("MS Sans Serif 1",18,"normal"))
write_score()
min_speed = 5
def wait(cond):
  while cond != True:
    time.sleep(0.1)
con = False
def hidetext():
  text.clear()
  #con = True
  score_text.goto(0, 250)
  write_score()


wn.listen()
wn.onkey(hidetext,"z")
#wait(con)

#score_text = turtle.Turtle()

global ball
ball = turtle.Turtle(shape=ballimg)
#ball.shape("circle")
#ball.color("Blue")
ball.speed(0)
ball.pu()
ball.goto(0,0)
ball.dx = 5
ball.dy = 0
#Assign a variable to the ball object: ball.dx = 5 & ball.dx =  -5
global left_pad
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.pu()
left_pad.goto(-400,0)
left_pad.shape("square")
left_pad.shapesize(6,2)
global right_pad
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.pu()
right_pad.goto(393,0)
right_pad.shape("square")
right_pad.shapesize(6,2)
top_border = 250
bottom_border=-250
#bgoverride = turtle.Turtle(shape=backround)
#bgoverride.ht()
#bgoverride.pu()
enable = True
def restart():
    ball.goto(0,0)
    right_pad.goto(395,0)
    left_pad.goto(-400,0)
    #bgoverride.ht()
    score_text.clear()
    score_text.goto(0,250)
    write_score()
    ball.st()
    left_pad.st()
    right_pad.st()
    enable = True
    ball.dx = 5
def endgame():
    enable = False
    ball.dx = 0
    ball.dy = 0
    ball.ht()
    left_pad.ht()
    right_pad.ht()
    print("ended")
    #bgoverride.st()
    #bgoverride.pu()

    if left_score >= 10:
        #score_text.write("Player 1 Wins!\nPress F to play again, Escape to close",align="center",font=("MS Sans Serif 1",18,"italic"))
        score_text.clear()
        score_text.write("Player 1 score:"+str(left_score)+"            Player 2 score:"+str(right_score),align="center",font=("MS Sans Serif 1",18,"normal"))
        player = 1
        for i in range(int(score_text.ycor()/5)):
            if score_text.ycor() != 0:
                score_text.write("Player 1 score:"+str(left_score)+"            Player 2 score:"+str(right_score),align="center",font=("MS Sans Serif 1",18,"normal"))
                score_text.sety(score_text.ycor() - 5)
                time.sleep(0.05)
                #score_text.undo()
            else: 
                None
                
    elif right_score >= 10:
        player = 2
        score_text.clear()
        score_text.write("Player 1 score:"+str(left_score)+"            Player 2 score:"+str(right_score),align="center",font=("MS Sans Serif 1",18,"normal"))

        for i in range(int(score_text.ycor()/5)):
            if score_text.ycor() != 0:
                score_text.write("Player 1 score:"+str(left_score)+"            Player 2 score:"+str(right_score),align="center",font=("MS Sans Serif 1",18,"normal"))
                score_text.sety(score_text.ycor() - 5)
                time.sleep(0.05)
                #score_text.undo()
            else:
                None
    score_text.goto(0,0)
    score_text.clear()
    score_text.write(f"                Player {player} Wins!\nPress F to play again, Escape to close",align="center",font=("MS Sans Serif 1",18,"italic"))
            
    wn.onkey(restart,"f")
        #score_text.write("Player 1 Wins!",align="center",font=("MS Sans Serif 1",18,"normal"))

def byebye():
    wn.bye()

def up():
  if left_pad.ycor() == 250:
    t=1
  else:
    left_pad.goto(left_pad.position()[0],left_pad.position()[1]+25)
def down():
  if left_pad.ycor() == -250:
    t=2
  else:
    left_pad.goto(left_pad.position()[0],left_pad.position()[1]-25)

def up_right():
  if right_pad.ycor() == 250:
    t=1
  else:
    right_pad.goto(right_pad.position()[0],right_pad.position()[1]+25)
def down_right():
  if right_pad.ycor() == -250:
    t=2
  else:
    right_pad.goto(right_pad.position()[0],right_pad.position()[1]-25)
wn.onkey(byebye,"Escape")
wn.onkey(up,"w")
wn.onkey(down,"s")
wn.onkey(up_right,"Up")
wn.onkey(down_right,"Down")
global game_running
game_running = True

while enable == True:
   try:
      if not game_running:
           break
      #wn.update()
      ball.setx(ball.xcor()+ball.dx)
      ball.sety(ball.ycor()+ball.dy)
      #d = ball.xcor() - right_pad.xcor()
      if abs(ball.xcor()-right_pad.xcor()) <= 26 and abs(ball.ycor()-right_pad.ycor()) <= 50:
        ball.dx=-5 - abs(ball.dy/2)
        ball.dy = ((ball.ycor()-right_pad.ycor()))/10

      if abs(ball.xcor()-left_pad.xcor()) <= 26 and abs(ball.ycor()-left_pad.ycor()) <= 50:
        ball.dx=5 + ball.dy/2
        ball.dy = (ball.ycor()-left_pad.ycor())/10
        #print(ball.ycor(),left_pad.ycor(),(ball.ycor()-left_pad.ycor()/2))
      if ball.ycor() >= 245: # make top and bottom border bounce it.
        ball.dy=-5
      elif ball.ycor() <=-245:
        ball.dy=5
      if ball.xcor() >= 420:
        #time.sleep(0.3)
        ball.dx = -ball.dx
        ball.dy = 0
        ball.goto(0,0)
        left_score +=1

        #print("Player 1 scored!\n","Player 1 Score:",left_score)
        write_score()
      elif ball.xcor()<=-420:
        ball.dx = -ball.dx
        ball.dy = 0
        ball.goto(0,0)
        right_score +=1
        #print("Player 2 scored!\n","Player 2 Score:",right_score)
        write_score()
      if left_score >= 10 or right_score >= 10:
          endgame()
          right_score = 0
          left_score = 0    
   except turtle.Terminator:
       break
   except Exception as e:
       print(f"An unexpected error occurred: {e}")
       break
wn.mainloop()
