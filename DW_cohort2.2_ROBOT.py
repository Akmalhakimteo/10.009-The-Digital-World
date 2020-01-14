# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 14:11:21 2019

@author: akmal
"""

from pythyiodw import *

def print_temp(t_celcius):
    t_fahr=t_celcius*(9/5)+32
    print("The temperature is {:5.3f}) fahrenheit. It is {:5.3f} degrees celcius".format(t_fahr,t_celcius))
    pass

def forward(speed,duration):
    robot.wheels(speed,speed)
    robot.sleep(duration)
    pass

robot=ThymioReal()

temp=robot.temperature

robot.quit()

