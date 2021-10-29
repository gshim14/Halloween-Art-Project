# Gina and Jane
#import statement
import turtle as trtl
import random as rand
#configurations
spotColor = "black"
spotShape = "square"
spotSize = 20
#initialize turtle
spot = trtl.Turtle()
spot.shape(spotShape)
spot.turtlesize(spotSize)
spot.fillcolor(spotColor)
spot.speed(0)
spot.penup()
#functions
def change_position():
  new_xpos = rand.randint(-180,180)
  new_ypos = rand.randint(-140,140)
  spot.penup()
  spot.goto(new_xpos,new_ypos)
  spot.pendown()
#box disappears when clicked on 
def spot_clicked(x,y):
  size = rand.randint(1, 10)
  spot.hideturtle()
spot.onclick(spot_clicked)
wn = trtl.Screen()
wn.mainloop()