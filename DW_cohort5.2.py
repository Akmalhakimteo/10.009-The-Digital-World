# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 15:42:35 2019

@author: akmal
"""                                             #RECURSION
# For or while loop - iterative
def printhello(n):
    if n==0:               #Terminating/stopping condition
        pass
    else:
        print("Hello")     #call yourself back
        printhello(n-1)    #different argument which makes it calll itself
        
printhello(30000000000)
#%%

myArray=[11,22,12,67,2,0,33,78,12,99,100,92,10,20,25]

def getSumRecursive(x):
    if len(x)<=1:
        return x[0]
    else:
        return getSumRecursive(x[0:int(len(x)/2)])+getSumRecursive(x[int(len(x))/2]:)

getSumRecursive(myArray)
#%% try try try
