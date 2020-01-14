# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 13:57:50 2019

@author: akmal
"""
sum_series=int(input("enter a number here\n"))
totalSum=0
#implement loop
for i in range(1,sum_series*3,3):
    totalSum+=1/i
print(round(totalSum,2))
#4
#1,12 - 1,4,7,10

#
#sum=1+1/4+1/7+1/10+1/13
#print(round(sum,2))
