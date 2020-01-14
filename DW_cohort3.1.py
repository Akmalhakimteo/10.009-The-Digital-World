# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 13:42:05 2019

@author: akmal
"""

#%%
a=1
r=2/3
n=1
sum=1
while n<10:
    sum+=a*r**n
    n+=1
    print(sum)
#%%

def summ(a,n,r):
    
    if r==1:
        return none
    else:
        i=0
        total=0
        while i<=n:
            term=a*r**i
            print(term)
            total=total+term
            i=i+1
        return total
summ(1,10,2/3)

#%%
d=list(range(10))

e=list(range(2,11))
f=list(range(1,7,2)) #(start, end, increment)
print(d)
print(e)
print(f)
#%%
g=[0]*10
print(g)

p=['pika']
c=['chu']
q=p*10 + c
#r=10*p +2 

print(q)
#%%
c=[]
c.append(20)
c.append(10)
c.append(30)
print(c)
c.sort()
print(c)
#%%
a=[]
a.append(None)
i=0
for i in range(20):
    print(i)
    a.append(None)
print(a)

#Answer
#b=[None]*20
#print(b)
#
#%%
def list_sum(ls):
    index=0
    total=0
    while index < len(ls):
        total = total + ls[index]
        print(index,total)
        index=index+1
    return total

#%%
b=[2,3,4,5,1]
b.sort()
print(b)
#%%
a=1
r=2/3
n=1
while n<10:
    sum+=r**n
    n+=1
    print(n)
    print(sum)





















