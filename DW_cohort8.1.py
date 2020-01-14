# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 13:09:07 2019

@author: akmal
"""

class Celcius:
    temperature=0
    
    def __init__(self,t=0):
        self.temperature = t
        
    def to_fahrenheit(self):
        return (self.temperature*1.8) + 32

c=Celcius()
print(c.to_fahrenheit)
print(c.to_fahrenheit(2)) ## whats the argument
#print(C3.temperature())

#%%
class Celcius:
    temperature=0
    
    def __init__(self,t=0):
        self.temperature=t
        
    def to_fahrenheit(self):
        return (self.temperature*1.8)+32
    
    def to_string(self):
        return "temp is {0} degreescelc.".format(self.temperature)
    
    def __str__(self):
        return "temp is {0} degreescelc.".format(self.temperature)
    
c_2=Celcius(100)
print(c_2.to_string())
#%% cohort problem 1 
class Coordinate:
    
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y
        
    def magnitude(self):
        return (self.x**2+self.y**2)**(1/2)
        
    def translate(self,dx,dy):
        self.x=self.x+dx
        self.y=self.y+dy
        return self.x,self.y
        
    def translated_magnitude(self,dx,dy):
        self.translate(dx,dy)
        return self.magnitude()
    
    def __eq__(self,other):
        if self==other:
            return True
        else:
            return False
    
p=Coordinate()
print(p.x,p.y)
print(p.translate(1,1))
        

























