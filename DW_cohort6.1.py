# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:05:01 2019

@author: akmal
"""
#strings are immutable, only way is to reassign
#print(type("hello"))

#print("Sammy has {0:5.2f} red {1:10}!".format(5,"balloons"))

for i in range(1,10,2):
    print("{:6d}{:6d}{:6d}".format(i,i*i,i*i*i))
#%%
    
myfood="eggs,maggi,ayampenyet,nasilemak"
newfood=myfood.split(",") #becomes list
print(newfood)
#%%
grocery="milkchicken\rcool"
print(grocery)
#print(grocery.splitlines())
#%%
s='hello there friend'
print(s.strip())
#%%
slicer=slice(0,9,2)
sentence='abcdefghijklmnopqrstuvwxyz'
print(sentence[slicer])
#%%
def findASCIIvalue(arg_string):
    return sum(ord(c) for c in arg_string)

print(findASCIIvalue("abc"))
print(findASCIIvalue("cba"))
print("abc"=="bca")
'''== compares character by charater, NOT based 
on ASCII sum as proven above'''
#%%





























