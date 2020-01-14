# -*- coding: utf-8 -*-
"""
Created on Sun Mar  3 13:17:04 2019

@author: akmal
"""

def find_average(lst):
    empty_list=[]
    overall_count=0
    overall_total=0


    for i in range(len(lst)):
        if len(lst[i])==0:
            empty_list.append(0)
            pass
        else:
            total=sum(lst[i])
            overall_total+=total
        
            count=len(lst[i])
            overall_count+=count
        
            indiv_ave=total/count
            empty_list.append(indiv_ave)
        
    overall_average=overall_total/overall_count
    
            
    return empty_list,overall_average
        
    
            

aa=[[13.13,1.1,1.1], [], [1,1,0.67]]  

#aa=[ [3,4] , [0], [-1,2,8] ]
print(find_average(aa))

#%% instructor ans
empty=[]
print(len(empty))
#%%
import copy
def transpose_matrix(matrix):
    b = copy.deepcopy(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            b[j][i]=matrix[i][j]
            
    return b


print(transpose_matrix([[-11,0,3], [4,0,6]]))

#%%
def transpose_matrix(a):               #[[-11,0,3], [4,0,6]])
    column_new=len(a)                 #2
    row_new=len(a[0])                 #3
    new_matrix=[]
    for i in range(row_new):
        in_matrix=[]
        for j in range(column_new):
            in_matrix.append(a[j][i])
        new_matrix.append(in_matrix)
    return new_matrix
                          
                          
print(transpose_matrix([[-11,0,3], [4,0,6]]))                         
                          
                          
                          
                          
                          
                          
    
    
