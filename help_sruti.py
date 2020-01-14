# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 23:16:20 2019

@author: akmal
"""
import random 
def throw_dice(n, num_experiments):
    
    counter=0
    for x in range(num_experiments+1):
        
        for i in range(n):
            number=random.randint(1,7)
            if number==6:
                counter=counter+1 
        
    prob= round(counter/num_experiments,4)
    return prob

print(throw_dice(1,100))
print(throw_dice(2,100))
