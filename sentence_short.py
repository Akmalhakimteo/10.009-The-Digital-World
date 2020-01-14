# -*- coding: utf-8 -*-
"""
Created on Thu Jan 17 14:58:01 2019

@author: akmal
"""
sentence=input("type anything here, I can tell you the shortest word\n")
list=sentence.split()
lowest_length=0

for word in list:
    number_letters=len(word)
#    print(number_letters)
    if lowest_length==0 or number_letters<lowest_length:
        lowest_length=number_letters
print(lowest_length)





#for word in sentence:
#    number_letters=len(word)
#    if number_letters==None or number_letters<len(list):
#        list.append(word)
        


#
#print(list)
#
#SOLUTIONS
#s=input("enter a list of words: ")
#s=s.split() # splits the string into a list of individual words
#l=min(s,key=len) #finds the shortest string in the list
#print(len(l)) #returns shortest word length
#
#
#generate list of prime number starting from 2
#cr8 scissors paper stone game
#cr8 blackjack game