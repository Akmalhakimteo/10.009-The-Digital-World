# -*- coding: utf-8 -*-
"""
Created on Tue Feb 19 15:33:16 2019

@author: akmal
"""

x=[1,2,3]
x[0]=0
y=x
y[0]=1
print(x[0])
#%%
my_tuple = (1, 2, 3, 4, 5)
print(type(my_tuple[0]))
my_tuple[3] = 20
#%%
a = set('totoro')
print(a) 
a.add('p')
print(a) 
#%%
my_string = 'wander'
my_string.replace('a','o')
my_string=my_string.replace('a','o')
print(my_string)
#%% 
'''
important stuff for exam
FOR LOOP
'''
rate=0.0119
for yen in range(100,1000,100):
    out="{0} yen is {1:5.2f} sgd".format(yen,yen*rate)
    print(out)

#%%
x=123456.123456
out="hello {0:2.4f}".format(x)
print(out)


#%% Dictionariesssssssssssssssssssssssssss - DATABASES!
import requests, json
url = 'https://xkcd.com/info.0.json' 
output = requests.get(url).text  #download the JSON data
j = json.loads(output) #convert JSON to python dictionary
print(j)
print(type(j))
print(len(j))
print('num')
print('comic' in j)
#list=[]
#for i in ()
print(j.keys())
print(j.values())

#%% looking through a dictionary

animals= {'cat':'meow',
          'dog':'woof'}

for a,b in animals.items():
    print(a,b)
for c in animals.items():
    print(c)





















