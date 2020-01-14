# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 12:44:50 2019

@author: akmal
"""
class Polynomial:
    
    def __init__(self,coeff):
        self.coeff=coeff
        
    def __add__(self,p2):
        newcoeff=[]
        length_max=max(len(self.coeff),len(p2.coeff))
        for i in range(length_max):
            if i<len(self.coeff) and i<len(p2.coeff):
                newcoeff.append(self.coeff[i]+p2.coeff[i])
            elif i<len(self.coeff):
                newcoeff.append(self.coeff[i])
            else:
                newcoeff.append(p2.coeff[i])
        return Polynomial(newcoeff)
    
    def __sub__(self,p2):
        newcoeff=[]
        length_max=max(len(self.coeff),len(p2.coeff))
        for i in range(length_max):
            if i<len(self.coeff) and i<len(p2.coeff):
                newcoeff.append(self.coeff[i]-p2.coeff[i])
            elif i<len(self.coeff):
                newcoeff.append(self.coeff[i])
            else:
                newcoeff.append(-p2.coeff[i])
        return Polynomial(newcoeff)
    
    def __call__(self,x):
        retval=0
        for i in range(len(self.coeff)):
            retval+= self.coeff[i] * x ** i
        return retval
    
    def __mul__(self,p2):                                       ###
        length1=len(self.coeff)
        length2=len(p2.coeff)
        new_length=length1+length2-1
        new_list=[0]*new_length
        for i in range(length1):
            for j in range(length2):
                count=i+j
                new_list[count]=length1[i]+length2[j]
        return new_list
        

p = Polynomial([1, 2, 3])                                                                                                                                        
q = Polynomial([2, 3]) 
print(p*q)     

  #%%
class Polynomial:
    
    def __init__(self,coeff):
        self.coeff=coeff
        
    def __add__(self,p2):
        newcoeff=[]
        length_max=max(len(self.coeff),len(p2.coeff))
        for i in range(length_max):
            if i<len(self.coeff) and i<len(p2.coeff):
                newcoeff.append(self.coeff[i]+p2.coeff[i])
            elif i<len(self.coeff):
                newcoeff.append(self.coeff[i])
            else:
                newcoeff.append(p2.coeff[i])
        return Polynomial(newcoeff)

    def __sub__(self,p2):
        newcoeff=[]
        length_max=max(len(self.coeff),len(p2.coeff))
        for i in range(length_max):
            if i<len(self.coeff) and i<len(p2.coeff):
                newcoeff.append(self.coeff[i]-p2.coeff[i])
            elif i<len(self.coeff):
                newcoeff.append(self.coeff[i])
            else:
                newcoeff.append(-p2.coeff[i])
        return Polynomial(newcoeff)
    
    def __call__(self,x):
        retval=0
        for i in range(len(self.coeff)):
            retval+=self.coeff[i]*x**i
        return retval
    
    def __mul__(self,p2):
        lenfp=len(self.coeff)*len(p2.coeff)
        d={} 
        for i in range(lenfp):
            d[i]=0
        for i in range(len(self.coeff)):
            for j in range(len(p2.coeff)):
                coeff=self.coeff[i]*p2.coeff[j]
                d[i+j]+=coeff
        maxid=0
        for i in range(lenfp):             
            if d[i]!=0:
                maxid=i
        fl = []

        for i in range(maxid+1):            
            fl.append(d[i])

        return Polynomial(fl)
    def derivative(self):
        newPoly=Polynomial(self.coeff)
        newPoly.differentiate()
        return newPoly
    def differentiate(self):
        newcoeff = []
        for i in range(1,len(self.coeff)):
            newcoeff.append(i*self.coeff[i])
        self.coeff = newcoeff
        
 
p = Polynomial([1, 2, 3])                                                                                                                                        
q = Polynomial([2, 3]) 

print((p-q).coeff)

#%%
#HW QN 4

class Polynomial:
    
    def __init__(self,coeff):
        self.coeff=coeff
        
    def __add__(self,p2):
        newcoeff=[]
        length_max=max(len(self.coeff),len(p2.coeff))
        for i in range(length_max):
            if i<len(self.coeff) and i<len(p2.coeff):
                newcoeff.append(self.coeff[i]+p2.coeff[i])
            elif i<len(self.coeff) and i>len(p2.coeff):
                newcoeff.append(self.coeff[i])
            elif i>len(self.coeff) and i<len(p2.coeff):
                newcoeff.append(p2.coeff[i])
        return Polynomial(newcoeff)
    
    def __sub__(self,p2):
        newcoeff=[]
        length_max=max(len(self.coeff),len(p2.coeff))
        for i in range(length_max):
            if i<len(self.coeff) and i<len(p2.coeff):
                newcoeff.append(self.coeff[i]-p2.coeff[i])
            elif i<len(self.coeff) and i>len(p2.coeff):
                newcoeff.append(self.coeff[i])
            elif i>len(self.coeff) and i<len(p2.coeff):
                newcoeff.append(-p2.coeff[i])
        return Polynomial(newcoeff)
    
    def __call__(self,x):
        retval=0
        for i in range(len(self.coeff)):
            retval+= self.coeff[i] * x ** i
        return retval
    
    def __mul__(self,p2):     
        length1=len(self.coeff)
#         print(self.coeff)
#         print(p2.coeff)
        length2=len(p2.coeff)
        new_length=length1+length2-1
        new_list=[0]*new_length
        for i in range(length1):
            
            for j in range(length2):
                
                counter=i+j
                print(self.coeff[i],p2.coeff[j])
                new_list[counter]+=self.coeff[i]*p2.coeff[j]
                
        return new_list
    
    def differentiate(self):
        new_polynomial=[]
        for i in range(len(self.coeff)):
            x=self.coeff[i]*i
            new_polynomial.append(x)
        return new_polynomial
    
    def derivative(self):
        newPoly=Polynomial(self.coeff)
        newPoly.differentiate()
        return newPoly
        
#checker for mul
p = Polynomial([1, 2, 3])                                                                                                                                        
# q = Polynomial([2, 3])   
# r = p * q    
# print(r)         #should be [2, 7, 12, 9]
# print(p.differentiate())            #TAKE NOTE


p2 = Polynomial ([0, 1, 0, 0, -6, -1]) 
p5 =p2.derivative
print(type(p2))
print(type(p5))
#%%
from libdw import sm

class CM(sm.SM):
    def __init__(self):
        self.start_state=0
    
    def get_next_values(self,state,inp):
        if state==0 and inp==100:  #all cases of table
            return (0 ,(0,"coke",0 ))
        
        elif state==1 and inp==100:
            return (0,(0,'coke',50))
        
        elif state==1 and inp==50:
            return (0,(0,'coke',0))
        
        elif state==0 and inp==50:
            return (1,(50 , '--', 0))
        else:                     #this part handles illegal input
            if state==1:          
                balance=50
            else:
                balance=0
            return (state,(balance,'--',inp))    
        #%%
from libdw import sm


class SimpleAccount(sm.SM):
            
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
            return 0, self.balance
        
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
    
class Cipher:
    
    def __init__(self,key,inp):
        self.key=key
        self.inp=inp
        
    def stuffz(self,msg):
        if key=='e':
            new_str=''
            for i in msg:
                if int(ord(i)+self.key)>122:
                    new_str+=str(chr(ord(i)+self.key-26))
                else:
                    new_str+=str(chr(ord(i)+self.key))
    
        if key=='d':
            new_str=''
            for i in msg:
                if int(ord(i)-self.key)<97:
                    new_str+=str(chr(ord(i)-self.key+26))
                else:
                     new_str+=str(chr(ord(i)-self.key))
                     
                     

         #%%   
for i in range(97,97+26):
    print(chr(i))
#%%
chr(97)
        




