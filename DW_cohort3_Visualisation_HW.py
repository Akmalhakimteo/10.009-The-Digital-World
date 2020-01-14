# -*- coding: utf-8 -*-
"""
Created on Sun Feb 17 21:10:53 2019

@author: akmal
"""
#%%
import matplotlib.pyplot as plt #import FIRST!!!

x_list = list(range(-1,6,1))  #generate X- values

y_list = []                  #generating Y values
for x in x_list:    
    y = x*x - 4*x + 3    
    y_list.append(y) 
    
plt.plot(x_list,y_list,marker="o")     #plotting x values, corresponding y values, marker type

plt.xlabel("x-values")                #labelling
plt.ylabel("y-values")

plt.title("y = x^2 -4x + 3")         #Labelling plot title

plt.show()                           #displaying title

#%%
import matplotlib.pyplot as plt
daily_total_rainfall=[0.2,7.8,0.4,3.4,0.4,3.8,12,5.4,1.6,0,0.8,12.4,2.4,2,4.6,0.8,18.4,7.4,20.6,4,13.2,2,4,0,4.8,14.4,9.6,0,5.6,7.6]
#middle_rainfall=
#plt.boxplot(daily_total_rainfall)
plt.hist(daily_total_rainfall,bins=[0,2,4,6,8,10,12,14,16,18,20,22])
plt.show()

#%%
print("Points system")
print("Akmal","\t","Filzah")
print("-----","\t","-------")
print("10001","\t","24")

#%%
import image
img = image.Image("luther.jpg")

print(img.getWidth())
print(img.getHeight())

p = img.getPixel(30, 100)                  #column followed by row
print(p.getRed(), p.getGreen(), p.getBlue())

#%%
import cImage as image
img = image.Image("myfile.gif")

#%%
#inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
#
#for akey in inventory.keys():     # the order in which we get the keys is not defined
#   print("Got key", akey, "which maps to value", inventory[akey])
#
#ks = list(inventory.keys())
#print(ks)
#inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
#
#print(list(inventory.values()))
#print(list(inventory.items()))
#
#for (v,k) in inventory.items():
#    print("Got", v, "that maps to", k)
#
#for v in inventory:
#    print("Got", v, "that maps to", inventory[v])

inventory = {'apples': 430, 'bananas': 312, 'oranges': 525, 'pears': 217}
print('apples' in inventory)
print('cherries' in inventory)

#%%
matrix = {(0, 3): 1, (2, 1): 2, (4, 3): 3}
print(matrix)
#%%
for number in [5, 4, 3, 2, 1, 0]:

    print("I have", number, "cookies.  I'm going to eat one.")
    #%%
mydict = {"cat": 12, "dog": 6, "elephant": 23, "bear": 20}
print("elephant" in mydict)

#%%

for i in range(4):
    for j in range(3):
        my_sum = i + j
     print(my_sum)











