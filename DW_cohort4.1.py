# -*- coding: utf-8 -*-
"""
Created on Mon Feb 18 12:59:47 2019

@author: akmal
"""
result=[]
for i in range (1,5,1):
    a=1
    r=2/3
    c=a*r**i
    result.append(c)
print(result)

#%%

def compound_value_months(amt, rate, months):    #quite useful
    result=0
    monthly_ir=rate/12
    for i in range(months):
        result=(amt+result)*(1+monthly_ir)
    result=round(result,2)
    return result

ans=compound_value_months(100,0.05,6)
print(ans)

#%%
aa=[ [3,4] , [5,6,7], [-1,2,8] ]
def find_average(lst):
    emplist=[]
    overall_total=0
    overall_count=0
    for i in range(len(lst)):
        
        total=sum(lst[i])
        overall_total += total
        count=len(lst[i])
        overall_count+=count
        average = total/count
        emplist.append(average)
        
        
    overall_ave=overall_total/overall_count
    return emplist,overall_ave
    
    
        
        
    
#        
aa=[ [3,4] , [5,6,7], [-1,2,8] ]
ans = find_average(aa)
print(len(aa))
print(ans)

#%%
import copy
a = [1,2,3]
b = [10, a]
c = copy.deepcopy(b) 		#using the copy library 
print(c[1] is a) 			#True/False?

#%%
pokemon = ['pikachu', 'snorlax', 'psyduck']
ghibli = ['totoro', 'chihiro', 'ponyo' ]
doraemon = ['anywhere-door', 'bamboo-copter' ]
fav = [pokemon, ghibli] 
chara = fav[:]
chara[0][1] = 'eevee' 
chara[1] = doraemon 
print(pokemon)
#%%
import copy
def transpose_matrix(a):
    b = copy.deepcopy(a)
   
    if len(a)==len(a[0]):    
        for i in range(len(a)):
            for j in range(len(a)):
                b[j][i]=a[i][j]
            
    else:
        row_length=len(a[0])
        
        for i in range(len(a)):
            for j in range(row_length):
                b[j][i]=a[i][j]
            
    return b


a= [[-11,0,3],[4,0,6]]
ans=transpose_matrix(a)
print(ans)
#%%

# Code:
import math
import scipy.constants as c

def deg_to_rad(deg):
    new_rad=(deg/360)*2*math.pi
    return new_rad
  
def rad_to_deg(rad):
    new_deg=(rad/(2*math.pi))*360
    return new_degree

#%%
import numpy as np 
import math
def spherical_to_cartesian(r,theta,phi):
    x=round(r*math.sin(theta)*math.cos(phi),5)
    y=round(r*math.sin(theta)*math.sin(phi),5)
    z=round(r*math.cos(theta),5)
    return x,y,z
	

def cartesian_to_spherical(x, y, z):
    r=round(math.sqrt(z**2+y**2+x**2),5)
    phi=round(math.atan2(y,x),5)
    theta=round(math.atan2(math.sqrt((x**2+y**2)/z)),5)
    return r,phi,theta























