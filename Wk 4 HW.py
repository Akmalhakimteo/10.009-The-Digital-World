# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 00:27:37 2019

@author: akmal
"""
def f_to_c(f):
    c=(f-32)*(5/9)
    return c

def f_to_c_approx(f):
    c_approx=(f-30)/2
    return c_approx
    

def get_conversion_table_a():
    f=0
    while f<100:
        
        c=f_to_c(f)
        c_approx=f_to_c_approx(f)
        return( f,round(c,1),round(c_approx,1) )
        f+=10
       
        

print(get_conversion_table_a())
#%%
def max_list(inlist):
    newlist=[]
    print(len(inlist))
    for i in range(len(inlist)):
        for j in range(len(i)):
            maximum=inlist[i][j]            
  
        









inlist =[[3 ,4 ,5 ,2] ,[1 ,7] ,[8 ,0 , -1] ,[2]]
print(max_list(inlist))
#%%

def multiplication_table(n):
    list=[]
    if n<1:
        return None
    elif n==1:
        return 1
    else:
        listinlist=[]
        i=1
        while i<n:
            for x in range(n+1):
                listinlist.append(x)
            i+=1
    print(listinlist)
        
        
multiplication_table(8)
#%%
import copy
x=[1,2,3]
y1=[x,0]
y2=copy.deepcopy(y1)
y2[0][0]=0
y2[1]=1
print(y1[0][0]) # (a)
print(y1[1]) # (b)
print(y2[0][0]) # (c)
print(y2[1]) # (d)
#%%













































