# -*- coding: utf-8 -*-
"""
Created on Mon Feb  4 12:21:00 2019

@author: akmal
"""

for name in ["Joe", "Amy", "Brad", "Angelina", "Zuki", "Thandi", "Paris"]:
    print("Hi", name, "Please come to my party on Saturday!")
    #%%
import turtle            # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()

for i in [0, 1, 2, 3]:      # repeat four times
    alex.forward(50)
    alex.left(90)

wn.exitonclick()
 
#%%
import turtle            # set up alex
wn = turtle.Screen()
alex = turtle.Turtle()

for aColor in ["yellow", "red", "purple", "blue"]:
   alex.color(aColor)
   alex.forward(50)
   alex.left(90)

wn.exitonclick()

#%%
#for i in range(4):
    # Executes the body with i = 0, then 1, then 2, then 3
for x in range(10):
    print(x)
    # sets x to each of ... [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

#%%
import turtle
wn = turtle.Screen()
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
tess.color("blue")
tess.shape("turtle")

print(list(range(5, 60, 2)))
tess.up()                     # this is new
for size in range(5, 60, 2):    # start with size = 5 and grow by 2
    tess.stamp()                # leave an impression on the canvas
    tess.forward(size)          # move tess along
    tess.right(24)              # and turn her

wn.exitonclick()    
    
#%%
print(1/3 +1/3 +1/3+1/3+1/3+1/3+1/3==2)
print(((1/3)*6)==2)
#%%
def describe_bmi(bmi):
    if(bmi>=27.5):
        output='high risk'
    elif(bmi<27.5 and bmi>=23):
        output='moderate  risk'
    elif(bmi<23 and bmi>=18.5):
        output='low risk'
    else:
        output='nutritional deficiency'
        
        return output
    
    
def describe_bmi(bmi):
    if (bmi<18.5):
        output='nutritional deficiency'
    elif (bmi<23):
        output='low risk'
    elif (bmi<27.5):
        output='moderate risk'
    else:
        output='high risk'
        
        return output
#    height=(int(input("insert heigh in cm")))
#    weight=(int(input("insert weight in KG")))
#    bmi=weight/(height)
#%%
def letter_grade(mark):
    if(mark<=100 and mark>=0):
        if (mark>=90):
            return="A"
        elif (mark>=80):
            return="B"
        elif(mark>=70):
            return="C"
        elif(mark>=60):
            return "D"
        elif(mark<60):
            return "E"
        else:
            return none
#%%
class Coordinate:
    x=0
    y=0
    

def is_in_square(square1, side1, square2, side2):
    a1 = Coordinate()
    b1= Coordinate()
    c1= Coordinate()
    
    a1.x = square1.x - side1/2
    a1.y = square1.y - side1/2
    
    b1.x = square1.x + side1/2
    b1.y = square1.y - side1/2
    
    c1.x = square1.x + side1/2
    c1.y = square1.y + side1/2
    
    a2 = Coordinate()
    b2 = Coordinate()
    c2 = Coordinate()
    
    a2.x = square2.x - side2/2
    a2.y = square2.y - side2/2
    
    b2.x = square2.x + side2/2
    b2.y = square2.y - side2/2
    
    c2.x = square2.x + side2/2
    c2.y = square2.x + side2/2
    
    if(a1.x>b2.x):
        return "false"
    if(a2.x>b1.x):
        return "false"
    if(b1.y>c2.y):
        return "false"
    if (b2.y > c1.y):
        return "false"
    else:
        return "true"
    
    
    
    
    






















