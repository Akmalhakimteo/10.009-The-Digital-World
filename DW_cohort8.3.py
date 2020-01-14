# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 13:04:47 2019

@author: akmal
"""

# 10 spaces, 2 decimal places - {0}:10.2f
class Line:
    
    def __init__(self,C0,C1):
        self.C0=C0
        self.C1=C1
    
    def __call__(self,x):
        return self.C0 + self.C1 + x
    
    def table(self,L,R,n):
        step=(R-L)/(n-1)
        x=[]
        for i in range(n):
            x.append(step*i+L)
        table=''
        for x_value in x:
            y=self(x_value)
            table+="{0:10.2f}{1:10.2f}\n".format(x_value,y)
        return table
            
line_1 = Line(1,5)
print(line_1.table(1,5,4))
''' different types of inheritence
1) Simple inheritence  - fire under spell
2) Chained inheritence - supernove under fire under spell
3) Multiple inheritence - armour,vest and shield

1)inheritence > simple,chained multiple
2) super().methodname(args)
3) is-a & has-a
    
    
You can check the method
resolution order by printing
className.__mro__

print(wizard.__mro__)