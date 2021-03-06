# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 14:27:18 2019

@author: akmal
"""
import random

craps=set([2,3,12])
naturals=set([7,11])

def roll_two_dices():
    dicenumber=random.randrange(1,7)
    return dicenumber

def print_lose():
    print("sorry, you lost the game")

def print_win():
    print("WOOHOOO, you're a WINNER!!!")

def print_point(p):
    print("your points are ",p)

def is_craps(n):
    if n in craps:
        return True
    else:
        return False

def is_naturals(n):
    if n in naturals:
        return True
    else:
        return False


# ATTENTION!
# You shouldn't need to edit the function below

def play_craps():
    point=-1
    while True:
        n1,n2=roll_two_dices()
        sumn=n1+n2
        print ('You rolled %d + %d = %d'%(n1,n2,sumn))   #initial points obtained here
        if point==-1:              #At the initialisation of point == -1 (see line 29)
            if is_craps(sumn):  #if the sum is in the set of craps
                print_lose()     #then it is an immediate loss
                return 0
            elif is_naturals(sumn):   #if the sum is in the set of naturals
                print_win()     #then it is an immediate  win
                return 1
            point=sumn
            print_point(point)
        else:
            if sumn==7:
                print_lose()
                return 0
            elif sumn==point:
                print_win()
                return 1   #goal of the game is to keep rolling dice until the sum == points obtained
   
play_craps()
