# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 08:43:24 2019

@author: akmal
"""

class Line:
    
    def __init__(self,C0,C1):
        self.C0=C0
        self.C1=C1
    
    def __call__(self,x):
        return self.C0 + self.C1 * x 
    
    def table(self,L, R, n):
        if n==0: 
            return 'Error in printing table'
        else:
            step=(R-L)/(n-1)
            x=[]
            
            for i in range(n):
                x.append(step*i+L)
            table=''
            ystuff=[]
            for x_values in x:
                y=self(x_values)
                ystuff.append(y)
            return x,ystuff
#                table+="{0:10.2f}{1:10.2f}\n".format(x_values,y)
#                if x[0]==x[1]:
#                    return table   
#        return table
    
line=Line(1,2)
line(2)
print(line.table(1,5,4))


