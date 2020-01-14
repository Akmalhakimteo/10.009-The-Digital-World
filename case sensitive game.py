# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 13:20:49 2019

@author: akmal
"""
print("are there CAPS in your word?")
user_ans=input("type in your input here please\n")
list_caps=[]
for char in user_ans:
    if char.isupper()==True:
        list_caps.append(char)
print("{},{}".format(char.islower(),list_caps))
#print({},{}.format(user_input.islower(),list_caps)
#    

#
#if user_ans.islower()==True:
#    print("all is in lowercase")
#else:
#    print("At least one letter is not in lowercase")
#    
