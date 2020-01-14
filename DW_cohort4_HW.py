# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 22:00:11 2019

@author: akmal
"""

def f_to_c(f):
    c=(f-32)*(5/9)
    return c

def f_to_c_approx(f):
    c_approx=(f-30)/2
    return c_approx
    

def get_conversion_table_a():
    big_list=[]
    for f in range(0,101,10):
        c=round(f_to_c(f),1)
        c_approx=round(f_to_c_approx(f),1)
        small_list=[f,c,c_approx]
        big_list.append(small_list)
    return big_list
        
        

print(get_conversion_table_a())
#%%
def f_to_c(f):
    c=(f-32)*(5/9)
    return c

def f_to_c_approx(f):
    c_approx=(f-30)/2
    return c_approx

def get_conversion_table_b():
    f_list=[]
    c_list=[]
    c_approx_list=[]
    for f in range(0,101,10):
        c=round(f_to_c(f),1)
        c_approx=round(f_to_c_approx(f),1)
        f_list.append(f)
        c_list.append(c)
        c_approx_list.append(c_approx)
    biglist=[f_list,c_list,c_approx_list]
    return biglist


print(get_conversion_table_b())
#%%
def max_list(inlist):
    
    output=[]
    
    for i in range(len(inlist)):
        
        max=[inlist[i][0]]
        for j in range(len(inlist[i])):
            if inlist[i][j]>max[0]:
                max[0]=inlist[i][j]
            else:
                pass
        output.append(max[0])
    return output


max_list([[1,2,3], [4,5]])             
#%%

def multiplication_table(n):
    if n<1:
        return None
    
    
    else:
        big_row=[]
        for i in range(1,n+1):
            row=[]
            for j in range(i,n*i+1,i):
                row.append(j)
            big_row.append(row)
            
        return big_row
    
print(multiplication_table(7))

#%%
#def max_list(inlist):
#    
#    output=[]
#    
#    for i in range(len(inlist)):
#        
#        max=[inlist[i][0]]
#        for j in range(len(inlist[i])):
#            if inlist[i][j]>max[0]:
#                max[0]=inlist[i][j]
#            else:
#                pass
#        output.append(max[0])
#    return output

def most_frequent(lst):
    
    d={}
    for i in lst:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    print(d)
    most_times=[]
    x=d[max(d,key=d.get)] # ??
    print(x)
    
    for key in d:
        if d[key]==x:
            most_times.append(key)
        else:
            pass
    return most_times
    
lst=[2,3,40,3,5,4,-3,3,3,2,0]
most_frequent(lst)
    
      #%%
      
keys={'a','b','c'}
vowels=dict.fromkeys(keys)
print(vowels)

keys={'a','b','c'} 
value=[1,2,3]         #changing all a, b, c values

vowels=dict.fromkeys(keys,value)
print(vowels)
#%%
def most_frequent(lst):
    dic_of_times = {}
    for item in lst: 
        if item in dic_of_times: 
            dic_of_times[item] += 1
        else: 
            dic_of_times[item] = 1
    most_times = []
    x = dic_of_times[max(dic_of_times, key = dic_of_times.get)]
    for key in dic_of_times.keys():
        if dic_of_times[key] == x: 
            most_times.append(key)
        else: 
            pass
    return most_times

lst=[2,3,40,3,5,4,-3,3,3,2,0]
most_frequent(lst)
            
            
    
            































