#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 10:24:04 2019

@author: norman_lee
"""
#%% 

""" Week 4 Question 5 """  

phonebook =[
{ 'name': 'Andrew', 
 'mobile_phone' :9477865, 
 'office_phone' : 6612345, 
 'email': 'andrew@sutd.edu.sg'} ,
 { 'name': 'Bobby' , 
  'mobile_phone' :8123498 , 
  'office_phone' :6654321 , 
  'email': 'bobby@sutd.edu.sg'} ] 

def get_details(name, key, phonebook):
    for dd in phonebook:
        if(dd['name']==name):
            print('found {}'.format(name))
            return dd[key]
    pass

print(get_details('Andrew','mobile_phone',phonebook))

#%% 
"""Week 4 Question 6""" 

def get_base_counts(dna):
    validchar='ATCG'
    dd={'A':0,'T':0,'C':0,'G':0}
    for char in dna:
        if(char in validchar):
            dd[char]+=1
        else:
            return 'The input DNA string is invalid'
            
    return dd
        
    
    


get_base_counts('GATTACA')

#%%






















