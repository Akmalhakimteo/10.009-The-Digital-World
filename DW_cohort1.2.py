# -*- coding: utf-8 -*-
"""
Created on Thu Jan 31 12:38:11 2019

@author: akmal
"""

a=int(input('value of a\n'))
n=int(input('value of n\n'))
r=input('value of r\n')
r1,r2=r.split("/")
r1=int(r1)
r2=int(r2)
fraction=r1/r2
sum=a*((1-fraction**n)/(1-fraction))
print(sum)
#%%


class Coordinate:
    x=3.2
    y=-1.5
    
p1=Coordinate()
p2=Coordinate()
p2.x=0.3
p2.y=1.0

print(type(p1))
print(type(p2))
print(type(Coordinate))
print(p1.x,p1.y)
print(p2.x,p2.y)

#%%


print(type("This is the first Week!"))
print("This is the first Week!")
print(type(24))
print(24)
print(type(2.4))
print(2.4)
print(type("24"))
print("24")
#print(type(‘2.4‘))
print(type("""2.4"""))
#print(type(‘‘‘2.4‘‘‘))
print(10300)
print(10,300)
print(10.300)
print(type(10.300))

#%%
x=float("0.9")
x=x+1
print(x)

#%%
x=str(23)
y=1+2*x
print(y)
#%%
x = 3
print (x , end = ' ')
x = x + 2
print ( x )
#%%
import random
prob=random.randrange(1,101)
print(prob)
#%%
def square(x):
    '''raise x to the second power'''
    return x * x

import test
print('testing square function')

test.testEqual(square(10), 100)

#%%


























