# -*- coding: utf-8 -*-
"""
Created on Fri Feb  1 14:34:39 2019

@author: akmal
"""
import math
#def calculate_hypo(a,b):
#    hypo=math.sqrt(a*a + b*b)
#    return hypo
#side1=int(input("side1\n"))
#side2=int(input("side2\n"))
#result=calculate_hypo(side1,side2)
#print("the hypotenuse side is {}".format(result))
#%%
def calculate_sum(a,r,n):
    sum=a*((1-r**n)/(1-r))
    return sum
a=1
n=10
r=2/3
result=calculate_sum(a,r,n)
print(result)
#%%
def say_something():
    print("lol")
#%%
def position_velocity(v0, t):
    g=9.81
    y=v0*t-0.5*g*t**2
    dy=v0-g*t
    y=round(y,2)
    dy=round(dy,2)
    return y,dy
print(position_velocity(5.0,10.0))
print(position_velocity(5.0,0.0))
print(position_velocity(0.0,5.0))
#%%
def bmi(weight, height):
    height=height/100
    result=weight/(height**2)
    return round(result,1)
print(bmi(60,120))
#%%
my_weight=float(input("what is your weight in KG\n"))
my_height=float(input("what is your height in CM\n"))
my_height=my_height/100
my_bmi=my_weight/(my_height**2)
print("BMI",my_bmi)
%%
from math import sqrt

class Coordinate:
    x=0.0
    y=0.0
#    
#p1=Coordinate ()
#p1.x=1.5
#p1.y=-3.4
#p2=Coordinate ()
#p2.x=4.6
#p2.y=5
#p3=Coordinate ()
#p3.x=9.5
#p3.y=-3.4

def area_of_triangle(p1,p2,p3):
    side1=(p1.x-p3.x)**2 + (p1.y - p3.y)**2
    side1=sqrt(side1)
    
    side2=(p1.x-p2.x)**2 + (p1.y - p2.y)**2
    side2=sqrt(side2)    
    
    side3=(p2.x-p3.x)**2 + (p2.y - p3.y)**2
    side3=sqrt(side3) 
    
    s=(side1+side2+side3)/2
    area=sqrt(s*(s-side1)*(s-side2)*(s-side3))
    area=round(area,2)
    return area

p1=Coordinate()
p2=Coordinate()
p3=Coordinate()
p1.x=float(input("first x value"))
p1.y=float(input("first y value"))
p2.x=float(input("second x value"))
p2.y=float(input("second y value"))
p3.x=float(input("3rd x value"))
p3.y=float(input("3rd y value"))


print("area of triangle is",area_of_triangle(p1,p2,p3),"cm3")

#%%
def position_velocity(v0, t):
    g=9.81
    x=v0*t-(1/2)*g*t**2
    a=v0-g*t
    return round(x,2),round(a,2)
#%%
def bmi(weight, height):
    height=height/100
    x=weight/(height**2)
    return round(x,1)
#%%
from math import sqrt

class Coordinate:
    x=0.0
    y=0.0
    
def area_tri(p1,p2,p3):
    s1=math.sqrt((p3.y-p1.y)**2+(p3.x-p1.x)**2)
    s2=math.sqrt((p2.y-p1.y)**2+(p2.x-p1.x)**2)
    s3=math.sqrt((p3.y-p2.y)**2+(p3.x-p2.x)**2)
    s=(s1+s2+s3)/2
    area=math.sqrt(s*(s-s1)*(s-s2)*(s-s3))    
    return round(area,2)
    
    
    
    
    
    
p1=Coordinate()
p2=Coordinate()
p3=Coordinate()

#%%

#         

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    