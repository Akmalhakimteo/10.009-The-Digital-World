# -*- coding: utf-8 -*-
"""
Created on Mon Feb 25 13:08:28 2019

@author: akmal
"""

def functionName(arg1, arg2, arg3 = 3):
 ##Your code here
.....
.....
.....
return expression
#%%

keys={'a','b','c'}
vowels=dict.fromkeys(keys)
print(vowels)

keys={'a','b','c'} 
value=[1,2,3]         #changing all a, b, c values

vowels=dict.fromkeys(keys,value)
print(vowels)
#%%

#1 function should only do 1 function
#%% WAYS TO IMPORT STUFF, **all must be in the same
                                    #folder
import myfunctions #OR 
from myfunctions import getfactorial
from myfunctions import * #imports everything
import myfunctions as mf #rename module
#import * dont need to write math.WHATEVER
print(myfunctions.getfactorial(10))
#%%
import random

print(random.randrange(1,6))
#%%
import random

craps=set([2,3,12])
naturals=set([7,11])

def roll_two_dices():
    dicenumber=random.randrange(1,7)
    dicenumber2=random.randrange(1,7)
    return dicenumber,dicenumber2

def print_lose():
    print("You lose")

def print_win():
    print("You win")

def print_point(p):
    print("Your points are ",p)

def is_craps(n):
    if n in craps:
        return True
    else:
        return False

def is_naturals(n):
    if n in naturals:
        return True
    else:
        return False


# ATTENTION!
# You shouldn't need to edit the function below

def play_craps():
    point=-1
    while True:
        n1,n2=roll_two_dices()
        sumn=n1+n2
        print ('You rolled %d + %d = %d'%(n1,n2,sumn))   #initial points obtained here
        if point==-1:              #At the initialisation of point == -1 (see line 29)
            if is_craps(sumn):  #if the sum is in the set of craps
                print_lose()     #then it is an immediate loss
                return 0
            elif is_naturals(sumn):   #if the sum is in the set of naturals
                print_win()     #then it is an immediate  win
                return 1
            point=sumn
            print_point(point)
        else:
            if sumn==7:
                print_lose()
                return 0
            elif sumn==point:
                print_win()
                return 1   #goal of the game is to keep rolling dice until the sum == points obtained
   
play_craps()
#%%
def leap_year(year):    #part a
    if year%4!=0:
        return False
    elif year%4!=100:
        return True
    elif year%400!=0:
        return False
    else:
        return True
    
#if (year is not divisible by 4) then (it is a common year)
#else if (year is not divisible by 100) then (it is a leap year)
#else if (year is not divisible by 400) then (it is a common year)
#else (it is a leap year)
        
def R(y,x): #part b
    return y%x
        
def day_of_week_jan1(year): #sunday 0, monday 1, tues 2, wed 3, thurs 4, fri 5, sat 6 
    d=R(1+(5*R(year-1,4)) + 4*R(year-1,100) + 6*R(year-1,400),7)
    return d


# d = R(1 + 5R(A − 1, 4) + 4R(A − 1, 100) + 6R(A − 1, 400), 7)

#part c
def num_days_in_month(month_num, leap_year):   #must fix True and False of leap year
    knuckle_months=[1,3,5,7,9,11]
    non_knuckle_months=[4,6,8,10,12]
    if month_num in knuckle_months:
        return 31
    elif month_num in non_knuckle_months:
        return 30
    elif month_num==2:
        if leap_year==True:
            return 29
        else:
            return 28

 #%%   #part d
def construct_cal_month(month_num, first_day_of_month, num_days_in_month):
    months_list=["January", "February", "March", "April", 
                  "May", "June", "July", "August",
                  "September", "October", "November", "December"
                 ]
    result=[]
    result.append(months_list[month_num-1])
    weekheader='  S  M  T  W  T  F  S'
    result.append(weekheader)
    week1=''
    space="   "
    week1=week1+first_day_of_month*space
    for i in range(7-first_day_of_month):
        week1=week1+"  "+str(i+1)
    result.append(week1)
    
    days_left=num_days_in_month-(7-first_day_of_month)
    
    week_n_start=7-(first_day_of_month)+1
    while days_left>=7:
        week_n=''
        for i in range(7):
            week_n=week_n + '{:3d}'.format(week_n_start+i)
        result.append(week_n)
        week_n_start+=7
        days_left-=7
    week_last=''
    for i in range(days_left):
        week_last+=(' '+str(week_n_start+i))
    result.append(week_last)
    return result
    
construct_cal_month(4,1,30)

#%%
def leap_year(year):    #part a
    if year%4!=0:
        return False
    elif year%4!=100:
        return True
    elif year%400!=0:
        return False
    else:
        return True
    
def R(y,x): #part b
    return y%x
        
def day_of_week_jan1(year): #sunday 0, monday 1, tues 2, wed 3, thurs 4, fri 5, sat 6 
    d=R(1+(5*R(year-1,4)) + 4*R(year-1,100) + 6*R(year-1,400),7)
    return d

#part c
def num_days_in_month(month_num, leap_year):   #must fix True and False of leap year
    knuckle_months=[1,3,5,7,9,11]
    non_knuckle_months=[4,6,8,10,12]
    if month_num in knuckle_months:
        return 31
    elif month_num in non_knuckle_months:
        return 30
    elif month_num==2:
        if leap_year==True:
            return 29
        else:
            return 28
        
def construct_cal_month(month_num, first_day_of_month, num_days_in_month):
    months_list=["January", "February", "March", "April", 
                  "May", "June", "July", "August",
                  "September", "October", "November", "December"
                 ]
    result=[]
    result.append(months_list[month_num-1])
    weekheader='  S  M  T  W  T  F  S'
    result.append(weekheader)
    week1=''
    space="   "
    week1=week1+first_day_of_month*space
    for i in range(7-first_day_of_month):
        week1=week1+"  "+str(i+1)
    result.append(week1)
    
    days_left=num_days_in_month-(7-first_day_of_month)
    
    week_n_start=7-(first_day_of_month)+1
    while days_left>=7:
        week_n=''
        for i in range(7):
            week_n=week_n + '{:3d}'.format(week_n_start+i)
        result.append(week_n)
        week_n_start+=7
        days_left-=7
    week_last=''
    for i in range(days_left):
        week_last+=(' '+str(week_n_start+i))
    result.append(week_last)
    return result
    
#construct_cal_month(4,1,30)
        
def construct_cal_year(year):
    
    whole_year_calendar=[]
    
    if leap_year(year)==True:
        number_days_in_jan= num_days_in_month(1,True)
        number_days_in_feb= num_days_in_month(2,True)
        number_days_in_mar= num_days_in_month(3,True)
        number_days_in_apr= num_days_in_month(4,True)
        number_days_in_may= num_days_in_month(5,True)
        number_days_in_jun= num_days_in_month(6,True)
        number_days_in_july=num_days_in_month(7,True)
        number_days_in_aug= num_days_in_month(8,True)
        number_days_in_sep=num_days_in_month(9,True)
        number_days_in_oct= num_days_in_month(10,True)
        number_days_in_nov= num_days_in_month(11,True)
        number_days_in_dec= num_days_in_month(12,True)
        
        first_day_jan=day_of_week_jan1(year)
        first_day_feb=(first_day_jan+number_days_in_jan)%7
        first_day_mar=(first_day_feb+number_days_in_feb)%7
        first_day_apr=(first_day_mar+number_days_in_mar)%7
        first_day_may=(first_day_apr+number_days_in_apr)%7
        first_day_jun=(first_day_may+number_days_in_may)%7
        first_day_july=(first_day_jun+number_days_in_jun)%7
        first_day_aug=(first_day_july+number_days_in_july)%7
        first_day_sep=(first_day_aug+number_days_in_aug)%7
        first_day_oct=(first_day_sep+number_days_in_sep)%7
        first_day_nov=(first_day_oct+number_days_in_oct)%7
        first_day_dec=(first_day_nov+number_days_in_nov)%7
        
        january=construct_cal_month(1,first_day_jan,number_days_in_jan)
        february=construct_cal_month(2,first_day_feb,number_days_in_feb)
        march=construct_cal_month(3,first_day_mar,number_days_in_mar)
        april=construct_cal_month(4,first_day_apr,number_days_in_apr)
        may=construct_cal_month(5,first_day_may,number_days_in_may)
        june=construct_cal_month(6,first_day_jun,number_days_in_jun)
        july=construct_cal_month(7,first_day_july,number_days_in_july)
        august=construct_cal_month(8,first_day_aug,number_days_in_aug)
        september=construct_cal_month(9,first_day_sep,number_days_in_sep)
        october=construct_cal_month(10,first_day_oct,number_days_in_oct)
        november=construct_cal_month(11,first_day_nov,number_days_in_nov)
        december=construct_cal_month(12,first_day_dec,number_days_in_dec)
        
        whole_year_calendar.append(january)
        whole_year_calendar.append(february)
        whole_year_calendar.append(march)
        whole_year_calendar.append(april)
        whole_year_calendar.append(may)
        whole_year_calendar.append(june)
        whole_year_calendar.append(july)
        whole_year_calendar.append(august)
        whole_year_calendar.append(september)
        whole_year_calendar.append(october)
        whole_year_calendar.append(november)
        whole_year_calendar.append(december)
        
    return whole_year_calendar


#%% 
def construct_cal_year(year):
    cal_year=[year]
    firstday=day_of_week_jan1(year)
    is_leap=leap_year(year)
    
    for i in list(range(1,13)):
        numdays=num_days_in_month(i, is_leap)
        month_n=construct_cal_month(i, firstday, numdays)
        if len(month_n[-1])==0:
            firstday=0
        elif len(month_n[-1])/3==7:
            firstday=0
        else:
            firstday=int(len(month_n[-1])/3)
        cal_year.append(month_n)
    return cal_year

def display_calendar(year):
    calendar=''
    cal_year=construct_cal_year(year)
    for i in cal_year:
        if type(i)==str:
            calendar+=(cal_year[i]+'\n')
        elif type(i)==list:
            for j in range(len(i)):
                if j==0:
                    calendar+=(i[j]+'\n')
                    calendar+='  S  M  T  W  T  F  S\n'
                elif i[0]=='December' and j==len(i)-1:
                    calendar+=(i[j])
                else:
                    calendar+=(i[j]+'\n')
            if i[0]=='December':
                pass
            else:
                calendar+='\n'
    return calendar
        
        
        
        
    
    
            
        




















        
    
        

    #%% skipppp
    
    first_day_of_month=3
    num_days_in_month=31
    result=[]
    
    week1=''
    space="   "
    week1=week1+first_day_of_month*space
    for i in range(7-first_day_of_month):
        week1=week1+"  "+str(i+1)
    result.append(week1)
    
    days_left=num_days_in_month-(7-first_day_of_month)
    
    week_n_start=7-(first_day_of_month)+1
    while days_left>=7:
        week_n=''
        for i in range(7):
            week_n=week_n + '{:3d}'.format(week_n_start+i)
        result.append(week_n)
        week_n_start+=7
        days_left-=7
    week_last=''
    for i in range(days_left):
        week_last+=(' '+str(week_n_start+i))
    result.append(week_last)
    
    
    #%%
    
    
    
    
    
    
    
    
    
    
    
    
    
#    
#    week=[]
#    counter=first_day_of_month
#    
#    for i in range(counter):
#        week.append("   ")
#        
#    for i in range(1,num_days_in_month+1):
#        week.append("%3d" % i)
#        counter += 1
#        if counter == 7:
#            line="".join(week)
#            result.append(line)
#            week=[]
#            counter=0
#            
#    if week:
#        line="".join(week)
#        result.append(line)
#    return result
        
print(construct_cal_month(1,2,31))
    





#%%










def construct_cal_year(year):
    pass

def display_calendar(year):
    pass












