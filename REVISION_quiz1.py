# -*- coding: utf-8 -*-
"""
Created on Thu Feb 21 20:41:52 2019

@author: akmal
"""
rand_list=[0,1,2,3,4,5]
for i in range(len(rand_list)):
    print(rand_list[i])
#%%

def fahrenheit_to_celsius(temp):
    temp_celcius=((temp-32)*5)/9
    return temp_celcius
#%%
def celsius_to_fahrenheit(temp):
    temp_fahr=temp*(9/5)+32
    return temp_fahr
#%%
import math
def area_vol_cylinder(radius,length):
    area=math.pi*radius**2
    vol=area*length
    return round(area,2),round(vol,2)

#%%
    

def wind_chill_temp(temp,speed):
    temp_wc=35.74 + 0.6215*temp - 35.75*speed**0.16 + 0.4275*temp*speed**0.16
    print('wind chill index:',temp_wc)
temp=float(input('Outside temperature in Fahrenheit:'))
speed=float(input('Wind speed in miles per hour: ))
wind_chill_temp(temp,speed)
#%%

def minutes_to_years_days(minutes):
    hours=minutes/60
    days=hours/24
    years=days//365
    days_left=days%365
    days_left=int(days_left)
    print("{} minutes is approximately {} years and {} days".format(minutes,years,days_left))

minutes_to_years_days(int(input('Enter the number of minutes:')))
#%%
def investment_val(amt, rate, years):
   monthly_rate=((rate/100)/12)
   months=years*12
   total=amt*(1+monthly_rate)**months
   return round(total,2)
#%%
def is_larger(n1,n2):
    if n1>n2:
        return True
    else:
        return False

is_larger(-23,-23.9)
#%%
def check_value(n1,n2,n3,x):
    if x>n1 and x>n2 and x<n3:
        return True
    else:
        return False
    #%%

dy/dx=3
    #%%
def primes_upto(n):
    """ Return a list of all prime numbers less than n. """
    result = []
    for i in range(2, n):
        if is_prime(i):
            result.append(i)
    return result
primes_upto(100)
    
#%%
def my_reverse(ls):
    newlist=[]
    for i in range(len(ls)-1,len(ls)-len(ls)-1,-1):
        newlist.append(ls[i])
    return newlist
        



ls=[1,2,3,4,5,6]

my_reverse(ls)

#%%
def my_reverse(ls):
    new_list=[]

    index=len(ls)-1
    while index<len(ls):
#        if index>=0:
#            #print(index)
#            term=ls[index]
#            print(term)
#            new_list.append(term)
#            print(new_list)
#        index=index-1
#    return new_list
        print(index)
        

ls=[1,2,3,4,5,6]
#my_reverse(ls)
print(len(ls))

#%%
def my_reverse(ls):
    newlist=[]
    x=len(ls)
    x=x-1
    while x>=0:
        newlist.append(ls[x])
        x-=1
    return newlist
    
    
ls=[1,2,3,4,5,6]
my_reverse(ls)

#%%
def may_ignore(obj):

    if type(obj)==type(1):
        obj=obj+1
        return obj
    else:
        None
#    if type(obj)==type(1) and type(obj)==type(1j) and type(obj)==type(3.0) and type(obj)==type('hi'):

may_ignore(1)
#%%
import math


front=(2*math.sqrt(2)/9801)

def approx_pi(n):
    sum=1
    
    for i in range(n+1):
        4n=4*n
        for x in range(4n,0,-1):
            sum*=x
    sum1=1103+26390*n
    
#%%
import math



def approx_pi(n):
    frontfrac=(2*math.sqrt(2)/9801)  

      
    summation=0
    while n>0:

        sum=1
#        fourn=4*n
        for x in range(1,fourn+1,1):
            sum*=x        

        sum2=1103+26390*n

        sumforsecondfact=1
        for i in range(1,n+1,1):
            sumforsecondfact*=i
        sumforsecondfact=sumforsecondfact**4

        fourthpart=396**(4*n)

        total=(sum*sum2)/(sumforsecondfact*fourthpart)
        summation=summation+total
        n-=1
        
    finalsum=frontfrac*summation
    pi=finalsum**(-1)
    return pi

approx_pi(3)
            #%%
def approx_pi(n):
    import math
    k=0
    summ=0
    while k<(n+1):
        fact=1
        i=1
        while i<(k+1):
            fact=fact*i
            i+=1
        summ=4*fact*(1103+26390*k)/((fact**4)*(396**(4*k)))+1103
        k+=1
    RHS=2*math.sqrt(2)/9801*summ
    ans=RHS**(-1)
    return ans           
#%%
def approx_pi(n):
    import math
    k=0
    summ=0
    while k<(n+1):
        summ=summ+(math.factorial(4*k)*(1103+26390*k)/((math.factorial(k)**4)*(396**(4*k))))
        k+=1
    RHS=2*math.sqrt(2)/9801*summ
    ans=RHS**(-1)
    return ans
#%%
def approx_pi(n):
    import math
    k=0
    sum=0
    while k<(n+1):
        sum= sum + (( math.factorial(4*k)* (1103+26390*k)) / ((math.factorial(k)**4) * (396**(4*k))) )
        

        
        k+=1
    invpi=sum*2*math.sqrt(2)/9801
    pi=invpi**(-1)
    return pi



approx_pi(3)
    #%%
def gcd(a,b):
    alist=[]
    blist=[]
    

    
    for i in range (1,a+1,1):
        if a%i==0:
            alist.append(i)
    print(alist)
    
    for x in range (1,b+1,1):
        if b%x==0:
            blist.append(x)
    print(blist)

    
    k=len(blist)-1
    for j in range(len(alist)-1,0,-1):
        for k in range(len(blist)-1,0,-1):
            if alist[j]==blist[k]:
                return alist[j]
            else:
                pass
            
        

        
    
    
    
gcd(18,9)

#%%
def simpsons_rule(f, n, a, b):
    
    if n<=0 or type(n)!=type(1):
        return None
    else:
        
        h=(b-a)/n
        
        first_term=f(a)
        
        sum_part2=0
        for j in range (1,(n/2)-1,1):
            x2j=a + j*h
            sum_part2=sumpart2+f(x2j)
        sum_part2=2*sum_part2
        
#        sum_part3=0
#        for k in range (1,n/2,1):
#            x2k=2*k-1
#            sum_part2=sumpart2+f(x2k)
#        sum_part3=4*sum_part2
        sum_part3=0
        for k in range (1,(n/2),1):
            thirdpart_subscript=2*k-1
            fn3= f( a + (thirdpart_subscript)*h )
            sum_part3 = sum_part3 + fn3
        sum_part3=sum_part3*4


        part4=f(b)

        finalsum=(h/3)(first_term + sum_part2 + sum_part3 + part4)        
            
def f(x):                                                                                                                                                                                                                                                                  
   return x**2                                                                                                                                                                                                                                                             


return round(simpsons_rule(f,1000,1,3), 2)             
            
        
    
    
    
    
    
    
    
    

        
        
            
         




















