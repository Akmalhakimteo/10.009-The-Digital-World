# -*- coding: utf-8 -*-
"""
Created on Tue Feb 12 15:32:11 2019

@author: akmal
"""
#n=int(input("insert value of n"))
#while n>1:
#    if n%2==0:
#        n=n/2
#        print(n)
#    else:
#        n=n-1
#        print(n)
#
##%%
#i=1
#while i<5:
#    print("hello")
#    i+=1
#%%

def minmax_in_list(ls):
    index=0
    if len(ls)==0:
        return None,None
    maximum=ls[0]
    minimum=ls[0]
    while index<len(ls):
        
        if (ls[index])>maximum:
            maximum=ls[index]
        if (ls[index])<minimum:
            minimum=ls[index]
       
        
        
        index=index+1
    
    
        
    return minimum, maximum
    
        

    
    
    
print(minmax_in_list([]))

#%%
num=str(12321)
maxnumber=len(num)
print(maxnumber)
#def is_palindrome(num):
    
#%%
def is_palindrome(num):
    my_list=str(num)
    index=0
    last_index= len(my_list) -1
    while index<len(my_list):
        front = index
        back = last_index - front
        
        if (my_list[front] != my_list[back]):
            return False
        
        
        
        index = index + 1
    return True

is_palindrome(12321)

#%%

pokemon = ['pikachu','snorlax','psyduck']
for i in range(len(pokemon)):
    print("welcome",pokemon[i])
    #%%
x_list=list(range(-3,10))
print(x_list)

y_list=[]

for i in range (len(x_list)):
    y_list.append(2*x_list[i]+1)
#    print(i,x_list[i],y_list)
print(x_list)
print(y_list)

import matplotlib.pyplot as plt

plt.plot(x_list,y_list,'bo')
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("y=2x+1")
plt.show()

#%%

import matplotlib.pyplot as plt
import math

x_list=list(range(-5,6))
y_list=[]
for x in x_list:
    y=1/(1+math.exp(-1*x))
    y_list.append(y)
    
plt.plot(x_list,y_list,'bo-')
plt.xlabel("x values")
plt.ylabel("y values")
plt.title("Logistic function")
plt.show()

#%%
def temp_convert(choice, temp):
    
    























