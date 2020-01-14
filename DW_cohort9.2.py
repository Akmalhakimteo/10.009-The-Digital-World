# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 15:39:08 2019

@author: akmal
"""

class simpleAccount(sm.SM):
            
    def __init__(self,money):
        self.balance=money
        if money>=100:
            self.startstate=1
        else:
            self.startstate=0
    
    def get_next_values(self,state,inp):
        new_balance=self.balance + inp
        if (new_balance>=100):
            self.balance=new_balance
            return 1,new_balance
        
        elif (inp<0 and state==0):
            self.balance=new_balance-5
            return 0, new_balance
        
        elif (inp<0 and state==1):
            self.balance=new_balance
            if self.balance>=100:
                return 1,new_balance
            else:
                return 0,new_balance
            
        elif (inp>0 and state==0):
            self.balance=new_balance
            if self.balance>=100:
                return 1,new_balance
            else:
                return 0,new_balance
            
        elif (inp>0 and state==1):
            self.balance = new_balance
            return 1,new_balance
            #%%
            
    