# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 10:53:44 2019

@author: akmal
"""

def fahrenheit_to_celsius(temp):
    t_celcius=(temp-32)*(5/9)
    return t_celcius

print(fahrenheit_to_celcius(-40))

#%%%
temp=0
def celsius_to_fahrenheit(temp):
    t_fahrenheit=temp*(9/5)+32
    return t_fahrenheit
print(celsius_to_fahrenheit(temp))
#%%
import math

radius=5
length=6
def area_vol_cylinder(radius,length):
    area=radius*radius*math.pi
    volume=area*length
    area=round(area,2)
    volume=round(volume,2)
    return area,volume
    print(area,volume)
    

print(area_vol_cylinder(1,2))
#%%
temp=float(input("Outside temperature in Fahrenheit:"))
speed=float(input("Wind speed in miles per hour:"))
def wind_chill_temp(temp,speed):
    temp_wc=35.74 + 0.6215*temp - 35.75*speed**0.16 + 0.4275*temp*speed**0.16
    temp_wc=round(temp_wc,5)
    return(temp_wc)

print("wind chill index:",wind_chill_temp(temp,speed))
#%%
minutes=int(input("insert number of minutes"))
def minutes_to_years_days(minutes):
    days=minutes/1440
    years=days//365
    days_remaining=days%365
    years=int(years)
    days_remaining=int(days_remaining)
    return years,days_remaining

print("{} minutes is approximately {} years and {} days".format(minutes,minutes_to_years_days(1000000000)[0],minutes_to_years_days(1000000000)[1]))

#%%
#amt=1000
#rate=4.25
#years=1
def investment_val(amt, rate, years):
    rate=rate
    months=years*12
    future_investment=amt*(1+rate/1200)**months
    future_investment=round(future_investment,2)
    return future_investment
print(investment_val(1000,4.25,1))

#%%
#n1=1
#n2=2
def is_larger(n1,n2):
    if n1>n2:
        return True
    else:
        return False
is_larger(2,-1)

#%%
def check_value(n1,n2,n3,x):
    if x>n1 and x>n2 and x<n3:
        return True
    else:
        return False
    
print("Test case 3:check_value(1,4,8,7)")
print("ans=True")
ans=check_value(1,4,8,7)





















