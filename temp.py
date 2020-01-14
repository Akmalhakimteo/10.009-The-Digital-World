# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

"""
print("hi")
"""

# from pythymiodw import *
import random as rd
from pythymiodw import *
robot=ThymioSimPG(scale=5)
for i in range(1,6):
 robot.wheels(300,600)
 robot.sleep(5)
 robot.quit()
 
#num1=int(input("Insert another number here\n"))
#if num1%2>0:
# robot.wheels(300,600)
# robot.sleep(5)
#else:
# robot.wheels(600,300)
# robot.sleep(5)
#num2=int(input("Insert another number here\n"))
#if num2%2>0:
# robot.wheels(300,600)
# robot.sleep(5)
#else:
# robot.wheels(600,300)
# robot.sleep(5)
#robot.quit()

