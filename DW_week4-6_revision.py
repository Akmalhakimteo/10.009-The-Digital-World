# -*- coding: utf-8 -*-
"""
Created on Sat Mar 16 15:11:58 2019
week 4-6 revision!!! woohooo
@author: akmal
"""
'''week 4'''
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
my_list1=my_list[0:9:3]
print(my_list1)
#my_list2=my_list[10:0:-2]
#print(my_list2)
#my_list3=my_list[::-1]
#print(my_list3)
#%%
list_a=['koala']
list_b=list_a
list_a.append('cat')
print(list_a)
print(list_b)
len(list_a)==len(list_b)
#%%
print("hello",end=" ")
print("charlier")
#%%
a=[2,4,6,8]
a.remove(2)
a.pop(0)
print(a)
#%%
import copy
a = [1,2,3]
b = [10, a]
c = copy.deepcopy(b) 		#using the copy library 
print(c[1] is a) 		
#%%
my_string = 'wander'
my_string.replace('a','o')
print(my_string)
my_string = my_string.replace('a','o') 
print(my_string)
new_string = my_string.replace('a','o') 
print(new_string)
#%%
aa = ['Love Live!','AKB48', 'KanColle']
aa.sort() 
print(aa)
bb = aa.sort() #this gives None. Why?  
print(bb)
#%%
a = set('totoro')
print(a) 
a.add('p')
print(a) 
#%%
import requests, json
url = 'https://xkcd.com/info.0.json' 
output = requests.get(url).text  #download the JSON data
j = json.loads(output) #convert JSON to python dictionary
print(j)
#%%
countries={}
musical_terms=dict()


countries['singapore']=5
countries['malaysia']=3
#print(countries)

#print('singapore' in countries)
countries.keys()
#print(countries.keys())
print(countries.values())

countries.get('scandinavia')
#%%
my_dd={'a':5}
my_dd['b']=my_dd.get('c',9)
my_dd['k']=my_dd.get('a',2)
print(my_dd)
#%%
animals = {'cat': 'meow',
           'dog': 'woof',
           'rat': 'squeak'}

#what is a? key or value? 
for a in animals: 
    print(a)
#%%
animals = {'cat': 'meow',
           'dog': 'woof',
           'rat': 'squeak'}

#what is b? key or value? 
for a,b in animals.items():
    print(a,b)
    print(type(a))

#what data type is c?     
for c in animals.items():
    print(c)
    print(type(c))
#%%
    
def compound_value_months(amt, rate, months):
    result=0
    monthly_ir=rate/12
    for i in range(months):
        result=(amt+result)*(1+monthly_ir)
    result=round(result,2)
    return result

compound_value_months(100, 0.05, 6)
assert(compound_value_months(100, 0.05, 6)==608.81)
assert(compound_value_months(200, 0.03, 1)==200.5)
print('all correct')

#%%


def find_average(lst):        #CASE: ([[3,4], [5,6,7], [-1,2,8]])
    empty_list=[]
    overall_total=0
    overall_count=0
    
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
        
    




assert(find_average([[13.13,1.1,1.1], [], [1,1,0.67]])==([5.11, 0.0, 0.89], 3.0))
assert(find_average([[2,3,4], [2,6,7], [10,5,15]])==([3.0, 5.0, 10.0], 6.0))
print('all correct')

#%%
def transpose_matrix(a):           #[[-11,0,3], [4,0,6]])
    column_new=len(a)
    row_new=len(a[0])
    new_matrix=[]
    
    for i in range(row_new): #0,1,2
        in_matrix=[]
        
        for j in range(column_new):   #0,1
            in_matrix.append(a[j][i])
        
        new_matrix.append(in_matrix)
        
    return new_matrix

            
transpose_matrix([[-11,0,3], [4,0,6]])
#%%
phonebook =[
{ 'name': 'Andrew', 
 'mobile_phone' :9477865, 
 'office_phone' : 6612345, 
 'email': 'andrew@sutd.edu.sg'} ,
 { 'name': 'Bobby' , 
  'mobile_phone' :8123498 , 
  'office_phone' :6654321 , 
  'email': 'bobby@sutd.edu.sg'} ] 

def get_details(name, key, phonebook):
    for i in phonebook:
        if i['name']==name:
            print('found {}'.format(name))
            return i[key]
    pass

print(get_details('Andrew','mobile_phone',phonebook))
#%%
def get_base_counts(dna):
    validchar='ATCG'
    dict={'A':0,'T':0,'C':0,'G':0}
    
    for char in dna:
        if char in validchar:
            dict[char]+=1
        else:
            return 'The input DNA string is invalid'
        
    return dict


get_base_counts('GV')
#%%
def max_list(inlist):
    output=[]
    
    for i in range(len(inlist)):
        first_max=inlist[i][0]
        for j in range(len(inlist[i])):
            if inlist[i][j]>first_max:
                first_max=inlist[i][j]
            else:
                pass
        output.append(first_max)
    return output
        

max_list([[100], [1,7], [-8,-2,-1], [2]])    
#%%
def multiplication_table(n):
    if n<1:
        return None
    
    else:
        big_row=[]
        for i in range(1,n+1):
            small_row=[]
            for j in range(i,i*n+1,i):
                small_row.append(j)
            big_row.append(small_row)
    return big_row


multiplication_table(7)
#%%

def most_frequent(lst):
    d={}
    for i in lst:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
            
    print(d)
            
    most_number=[]
    x=d[max(d,key=d.get)]
    print(x)
    
    for key in d:
        if d[key]==x:
            most_number.append(key)
        else:
            pass
    return most_number
    
    
    
    

#most_frequent([2,3,40,4,5,4,-3,3,3,2,0])        
most_frequent([9,30,3,9,3,2,4]) 

#%%
def diff(p):
    dp={}
    keys=p.keys()
    print(dp)
    
    for i in keys:
        if i!=0:
            dp[i-1]=i*p[i]
    return dp



diff({1:-3, 3:2, 5:-1, 6:2})
#%%
a =(1)
b =(1 ,)
print(type(a))
print(type(b))



#%%
import math
print(a == 'abc')
print(b ==0+0j)
print(c ==(1 ,))
print(d == '')
print(e ==  None)
print(f == None)
#%%
t=(1,2,3)
print(t+t)
print(t*3)
print(t[1:-1])
#%%
import random
import matplotlib.pyplot as plt
import numpy

def pi_approx_monte_carlo(n):
    
    x = numpy.random.uniform(low=-1, high=1, size=[n,1])
    y=  numpy.random.uniform(low=-1, high=1, size=[n,1])
    
    inside_bool= x**2 + y**2 <1
    
    approx_pi = 4*numpy.sum(inside_bool)/n
    
    x_in=x[inside_bool]
    y_in=y[inside_bool]
    
    plt.figure(figsize=[5,5])
    plt.scatter(x,y,s=1)
    plt.scatter(x_in, y_in, color = 'r' , s=1)
    plt.show()
    return approx_pi
    
pi_approx_monte_carlo(1000)
#%%
'''Write a function matAdd(A, B) to compute the sum of two matrices A and B.

Specifically, given two mxn matrices A = [aij], B = [bij], matAdd(A, B) returns a new matrix C = A + B. 
That is, C = [cij] is a mxn matrix, cij = aij + bij.

You can assume A and B are always mxn.

Note that you need to return a new matrix C that does not have any aliasing with the input matrices A and B.
 The mxn matrices A, B and C are represented by Python nested lists.

Each matrix is a nested list that has m entries, each entry is a list that represents a row of the matrix.'''

def matAdd(A,B):
    if len(A)==len(B) and len(A[0])==len(B[0]):
        new_matrix=[]
        for i in range(len(A)):
            new_matrix.append([])
            for j in range(len(A[0])):
                C=A[i][j]+B[i][j]
                new_matrix[i].append(C)
    else:
        return 'Invalid'
            
    return new_matrix


matAdd([[1,2,3],[4,5,6]],[[1,1,1],[1,1,1]])
#%%
myarray=[1,1,1,1,1,1,1,1,1]

def getSumRecursive(x):
    if len(x)<=1:
        return x[0]
    else:
        return getSumRecursive(x[0:int(len(x)/2)]) + getSumRecursive(x[int(len(x)/2):])

getSumRecursive(myarray)
#%%

x =[1 ,2 ,3]
x [0]=0
y = x
y [0]=1
print(x,y)
#%%
x =[1 ,2 ,3]
def f ( l ) :
    l [0]='a'
f(x)
print(x)
#%%
x =[1 ,2 ,3]
y =[ x ]
a =[ y , x ]
y [0][0] = (1 ,2)
print(y)
#%%
x =[1 ,2 ,3]
y1 =[ x ,0]
y2 = y1 [:]
y2 [0][0]=0
y2 [1]=1
print(y1,':y1')
print(y2,':y2')
#print(y1[0][0],'a') # ( a )
print(y1[1],'b') # ( b )
#print(y2[0][0],'c') # ( c )
#print(y2[1],'d') # ( d )
#%%
import copy
x =[1 ,2 ,3]
y1 =[ x ,0]
y2 = copy . deepcopy ( y1 )
y2 [0][0]=0
y2 [1]=1
print(y1 [0][0],'a') # ( a )
print(y1 [1],'b') # ( b )
print(y2 [0][0],'c') # ( c )
print(y2 [1],'d') # ( d )


#%%
l =[1,2,3]
l[2:3]=[4]    # ( a )
print(l)
#%%

l =[1 ,2 ,3]
l[1:3]=[0] # ( b )
print(l)
#%%
l =[1 ,2 ,3]
l[1:1]=[1] # ( c )
print(l)
#%%
l =[1 ,2 ,3]
l[2:]=[] # ( d )
print(l)
#%%
def compound_value_months(amt, rate, months):
    monthly_ir=rate/12
    total=0
    for i in range(months):
        total=(amt+total)*(1+monthly_ir)
    return total

compound_value_months(100,0.03,7)
#%%
def find_average(lst):
    
    overall_total=0
    overall_count=0
    empty_list=[]
    
    for i in range(len(lst)):
        if len(lst[i])==0:
            empty_list.append(0)
        else:
            total=sum(lst[i])
#            print(total)
            overall_total+=total
            
            count=len(lst[i])
#            print(count)
            overall_count+=count
            
            local_average=total/count
            empty_list.append(local_average)
            
    overall_average=overall_total/overall_count
            
    return empty_list,overall_average
            
            
            
        


ans = find_average ([[2 ,3 ,4] ,[] ,[10 ,5 ,15]])
print ( ans )
#%%

def transpose_matrix(matrix):
    new_column=len(matrix)
    new_row=len(matrix[0])
    new_matrix=[]
    
    for i in range(new_row):
        new_column_matrix=[]
        for j in range(new_column):
            new_column_matrix.append(matrix[j][i])
        new_matrix.append(new_column_matrix)
    return new_matrix

transpose_matrix([[-11,0,3], [4,0,6]])  
transpose_matrix([[1,2,3], [4,5,6], [7,8,9]]) 
#%%
phonebook =[
{ 'name': 'Andrew', 
 'mobile_phone' :9477865, 
 'office_phone' : 6612345, 
 'email': 'andrew@sutd.edu.sg'} ,
 { 'name': 'Bobby' , 
  'mobile_phone' :8123498 , 
  'office_phone' :6654321 , 
  'email': 'bobby@sutd.edu.sg'} ] 

def get_details(name, key, phonebook):
    
    for dd in phonebook:
        if dd['name']==name:
            print('{} found'.format(name))
            return dd[key]
        
            

print ( get_details ( 'Andrew' , 'mobile_phone' , phonebook ))
#%%

def get_base_counts(dna):
    validchar='ACGT'
    dd={'A':0,'C':0,'G':0,'T':0}
    for i in dna:
        if i in validchar:
            dd[i]+=1
        else:
            pass
    return dd

get_base_counts('GATTACA')
#%%
def max_list(inlist):
    
    new_list=[]
    
    for i in range(len(inlist)):
        max=inlist[i][0]
        for j in range(len(inlist[i])):
            if inlist[i][j]>max:
                max=inlist[i][j]
            else: pass
        new_list.append(max)
    return new_list

inlist = [[100] ,[1 ,7] ,[ -8 , -2 , -1] ,[2]]
print ( max_list ( inlist ) )

#%%
def multiplication_table(n):
    
    if n<1:
        return None
    else:
        big_row=[]
        
        for i in range(1,n+1):
            row=[]
            for j in range(i,i*n+1,i):
                row.append(j)
            big_row.append(row)
    return big_row

multiplication_table(7)
#%%
def most_frequent(lst):
    d={}
    
    for i in lst:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1
    
    most_times=[]
    x=d[max(d,key=d.get)]
    
    for key in d:
        if d[key]==x:
            most_times.append(key)
        else:
            pass
    
    return most_times


most_frequent([2,3,40,3,5,4,4,4,4,-3,3,3,2,0])

#%%
def diff(p):
    dp={}
    keys=p.keys()
    print(keys)
    
    for i in keys:
        if i!=0:
            dp[i-1]=i*p[i]
    return dp
    
p ={0: -3 , 3:2 , 5: -1}
diff ( p )
#%%
craps=set([2,3,12])
print(craps)

#%%
def get_fact(n):
    if n==1:
        return 1
    return n*get_fact(n-1)

get_fact(5)
#%%

def extract_values(values):
    a.split(" ")
    a1=int(a[0])
    a2=int(a[1])
    
    return a1,a2

def calc_ratios(values):
    if values[1]==0:
        return None
    else:
        return values[1]/values[0]
    
    #%%
spacebar="hello there"
y=spacebar.split(" ")
print(y)
#%%
'''Tower of HANOI WOOOOOOOOOOOO'''
def move_disks(n, from_tower, to_tower, aux_tower, sol):
    if n==0:
        return None
    else:
        move_disks(n-1,from_tower,tp_tower,aux_tower,sol)
        
    #%%
def move_disks(n, from_tower, to_tower, aux_tower, sol):
     if n==1:
         sol.append('Move disk 1 from {} to {}'.format(from_tower,to_tower))
         return sol
     else:
         move_disks(n-1,from_tower,to_tower,aux_tower,sol)
         sol.append('Move disk {} from {} to {}'.format(n,from_tower,to_tower))
         return sol
             #%%
def reverse(string):
    a=''
    for i in range(len(string)):
        a=string[i] + a
    return a
reverse('akmal hakim teo')

#%%
def check_password(password):
    check_length=False
    check_2digits=False
    check_alphanumeric=False
    
    if len(password)>=8:
        check_length=True
    
    if password.isalnum():
        check_alphanumeric=True
    
    counter=0
    for i in  range(0,len(password)):
        if password[i].isdigit():
            counter+=1
    if counter>=2:
        check_2digits=True
    
    if check_length==True and check_2digits==True and check_alphanumeric==True:
        return True
    else: return False
    
check_password('bobbnk32n')
            
            #%%
string='ab23cdeg'
for i in string:
    print(i)
    
    #%%
    
    
def longest_common_prefix(string1, string2):
    common_stuff=''
    if len(string1)>len(string2):
        shorter_string=len(string2)
    else:
        shorter_string=len(string1)
    
    for i in range(shorter_string):
        if string1[i]==string2[i]:
            common_stuff=common_stuff+string1[i]
        else:
            break
    return common_stuff

longest_common_prefix('hefll','hellboy')
#%%
import numpy as np
open_file=open('xy.dat','r')

class Coordinate:
    x = 0
    y = 0

def get_maxmin_mag(f):
    
    lst=[]
    for line in f:
        
        points=line.split()
        coordinate_var=Coordinate()
        lst.append(coordinate_var)
        
    
    
        #%%
import math

class Coordinate:
    x = 0
    y = 0

def get_maxmin_mag(f):
    class Coordinate:
        x = 1
        y = 1
    themax = Coordinate()
    themin = Coordinate()
    maxx, maxy, minx, miny = None,None,None,None
    for line in f:
        x,y = line.split()
        x,y = float(x),float(y)
        magnitude = math.sqrt((x**2)+(y**2))
        if maxx == None:
            maxx,maxy,minx,miny = x,y,x,y
            print('max is ', maxx,maxy,'min is ', minx,miny)
        elif magnitude > math.sqrt(maxx**2 + maxy**2):
            maxx,maxy = x,y
        elif magnitude < math.sqrt(minx**2 + miny**2):
            minx,miny = x,y
    themax.x,themax.y,themin.x,themin.y = maxx,maxy,minx,miny
    return themax,themin
        
        #%%
        tuple1=(1,2)
#        print(type(tuple1))
#        string=str(tuple1)
#        string=string.split(',')
#        print(string)
        a=''
        for i in range(len(tuple1)):
            a = a + ' '  + str(tuple1[i])
        print(a)
        
        
    
        






















#%%
cococo='hello\tworld'
print(cococo)
cococo=cococo.split('\t')
print(cococo)

#$$
y='abcdefgh'
print(y[1])


#%%
lists='abc'
for i in range(len(lists)):
    print(i)
#%%
def get_base_counts2(dna):
    for i in dna:
        if i.isalpha:
            if i.isUpperCase:
                validchar='ATCG'
                d={'A':0,'T':0,'G':0,'C':0}
                
                for char in dna:
                    if char in validchar:
                        d[char]+=1
                    else:
                        pass
                    
                return d
            else: return 'The input DNA string is invalid.'
        else: return 'The input DNA string is invalid.'
    
get_base_counts('GATTACA')
#%%
import numpy as np

class Coordinate:
    x = 0
    y = 0

def get_maxmin_mag(f):
    
    lst=[]
    for line in f:
        points=line.strip()
        points=line.split('\t')
        coord_var=Coordinate()
        coord_var.x = float(points[0])
        coord_var.y = float(points[1])
        lst.append(coord_var)
      
    magnitude_several=[]
    for i in lst:
        magnitude = ( coord_var.x**2 + coord_var.y**2 ) ** (1/2)
        magnitude_several.append(magnitude)
    
    max=magnitude_several[0]
    max_placement=0
    
    min=magnitude_several[0]
    min_placement=0
    
    
    for j in range(len(magnitude_several)):
        if magnitude_several[j]>max:
            max=magnitude_several[j]
            max_placement=j
        elif magnitude_several[j]<min:
            min=magnitude_several[j]
            min_placement=j
        else:
            pass
    
    pmax=Coordinate()
    pmax.x=lst[max_placement].x
    pmax.y=lst[max_placement].y
    
    pmin=Coordinate()
    pmin.x=lst[min_placement].x
    pmin.y=lst[min_placement].y
    
    return pmax,pmin
#%%
def most_frequent(lst):
    
    d={}
    for i in lst:
        if i not in d:
            d[i]=1
        else:
            d[i]+=1

    most_times=[]
    x=d[max(d,key=d.get)] #ask prof/suhas
    print(x)
    
    for key in d:
        if d[key]==x:
            most_times.append(key)
        else:
            pass
    return most_times
            
        #%%
class Coordinate:
    x = 0
    y = 0

def get_maxmin_mag(f):
    
    lst=[]
    for line in f:
        points=line.strip()
        points=line.split('\t')
        coord_var=Coordinate()
        coord_var.x = float(points[0])
        coord_var.y = float(points[1])
        lst.append(coord_var)
      
    magnitude_several=[]
    for i in lst:
        magnitude = ( i.x**2 + i.y**2 ) ** (1/2)
        magnitude_several.append(magnitude)
    
   
    
    max=-999999
    max_placement=0
    min=9999999
    min_placement=0
    
    for j in range(len(magnitude_several)):
        if magnitude_several[j]>max:
            max=magnitude_several[j]
            max_placement=j
        elif magnitude_several[j]<min:
            min=magnitude_several[j]
            min_placement=j
    
    pmax=Coordinate()
    pmax.x=lst[max_placement].x
    pmax.y=lst[max_placement].y
    
    pmin=Coordinate()
    pmin.x=lst[min_placement].x
    pmin.y=lst[min_placement].y
    
    return pmax,pmin
#%%
hw 4: def get_fundamental_constants(f):
    dic={}
    string=f.readlines()
    print (string)
    #string=f.readline()
     #with 2 readline, for loop starts at line 3
        #print (line.split())

        p=line.strip().split() #strip first removes all empty spaces at start and end, split then convert str to list
        #p is now a list of char
        #use float since got decimal
        dic.update({p[0]:float(p[1])})
   
        
    return dic

#%%
def get_fundamental_constants(f):
    dd={}
    lines=f.readlines()
    for line in lines:
        line = line.strip()
        line = line.split()
        if len(line)==3:
            dd.update({line[0]:float(line[1])})
        else: pass
    return dd
        
        
#%%
a=[1,2,3,4,5,7,7,8]
print(a.index(7))
b='agcdefg'
print(b.index('g'))
    
#%%
str = "2009"
print (str.isnumeric())
#%%
# MID-TERM EXAM: QUESTION 3

import math

def area_square(s):
    return s*s

def vol_frustum(top_area, bottom_area, height):
    volume= (height/3) * ( top_area + bottom_area + math.sqrt(top_area*bottom_area) )
    volume=round(volume,3)
    return volume
def get_volume(s1, s2, height):
#    top_area=area_square(s1)
#    bottom_area=area_square(s2)
    vol_frustum(area_square(s1), area_square(s2), height)
    
print(get_volume(3.6,6.4,4.0)) 

#%%
x=5.34324
print(round(x,2))
    #%%
def det_2x2_matrix(mat):
    det=mat[0][0]*mat[1][1]-mat[0][1]*mat[1][0]
    return det

def det_3x3_matrix(mat):
    firstpart = mat[0][0] * ( mat[1][1]*mat[2][2] - mat[2][1]*mat[1][2] )
    secondpart= -mat[0][1] * ( mat[1][0] * mat[2][2] - mat[1][2] * mat[2][0] )
    thirdpart= mat[0][2] * ( mat[1][0]*mat[2][1] - mat[1][1]*mat[2][0] )
    det = firstpart + secondpart + thirdpart
    return det


def determinant(matrix):
    n=len(matrix)
    if n>3 and n<1:
        return None
    elif n=1:
        det=matrix[0]
    elif n=2:
        det=det_2x2_matrix(matrix)
    elif n=3:
        det=det_3x3_matrix(matrix)
    else: 
        pass

#%%

def matAdd(A, B):
    m = len(A)
    n= len(A[0])
    C=[]
    
    for i in range(m):
        mini_C=[]
        for j in range(n):
            newvalue=A[i][j]+B[i][j]
            mini_C.append(newvalue)
        C.append(mini_C)
    
    return C

matAdd ( [[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]])
#%%
def getMRT(f):
    mrt_dict={}
    lines = f.read().splitlines()
    for l in lines:
        words = l.split(",")
        mrt_dict[words[0]]=words[1:]
    return mrt_dict
#%%
my_list=[1,2,3,4,5]
my_list.remove(3)
print(my_list)
        #%%
for i in range(1,10,2): 

    print("{:6d} {:6d}{:6d}".format(i,i*i,i**3))
#%%
dd= {'a':0,'b':0,'c':0}
print(dd['a'])
#%%
Output:  {'=EastWestLine (EW)=': [], 'Pasir Ris': [' Tampines', ' Simei', ' Tana                                                                                      
 Lavender', ' Bugis', ' City Hall', ' Raffles Place', ' Tanjong Pagar', ' Outram                                                                                      
' Dover', ' Clementi', ' Jurong East', ' Chinese Garden', ' Lakeside', ' Boon La                                                                                      
uas Link'], '': [], '=EastWestLine (CG)=': [], 'Tanah Merah': [' Expo', ' Changi                                                                                      
 ' Choa Chu Kang', ' Yew Tee', ' Kranji', ' Marsiling', ' Woodlands', ' Admiralt                                                                                      
 ' Bishan', ' Braddell', ' Toa Payoh', ' Novena', ' Newton', ' Orchard', ' Somer                                                                                      
Pier']}                                                                                                                                                               
Expected:  {'EastWestLine (EW)': ['Pasir Ris', 'Tampines', 'Simei', 'Tanah Merah                                                                                      
ugis', 'City Hall', 'Raffles Place', 'Tanjong Pagar', 'Outram Park', 'Tiong Bahr                                                                                      
rong East', 'Chinese Garden', 'Lakeside', 'Boon Lay', 'Pioneer', 'Joo Koon', 'Gu                                                                                      
anah Merah', 'Expo', 'Changi Airport'], 'NorthSouthLine': ['Jurong East', 'Bukit                                                                                      
ds', 'Admiralty', 'Sembawang', 'Canberra', 'Yishun', 'Khatib', 'Yio Chu Kang', '                                                                                      
rset', 'Dhoby Ghaut', 'City Hall', 'Raffles Place', 'Marina Bay', 'Marina South                                                                                       
Pass:
    #%%
Output:  {'=EastWestLine (EW)=': [], 'Pasir Ris': [' Tampines', ' Simei', ' Tana                                                                                      
 Lavender', ' Bugis', ' City Hall', ' Raffles Place', ' Tanjong Pagar', ' Outram                                                                                      
' Dover', ' Clementi', ' Jurong East', ' Chinese Garden', ' Lakeside', ' Boon La                                                                                      
uas Link'], '': [], '=EastWestLine (CG)=': [], 'Tanah Merah': [' Expo', ' Changi                                                                                      
 ' Choa Chu Kang', ' Yew Tee', ' Kranji', ' Marsiling', ' Woodlands', ' Admiralt                                                                                      
 ' Bishan', ' Braddell', ' Toa Payoh', ' Novena', ' Newton', ' Orchard', ' Somer                                                                                      
Pier']}                                                                                                                                                               
Expected:  {'EastWestLine (EW)': ['Pasir Ris', 'Tampines', 'Simei', 'Tanah Merah                                                                                      
ugis', 'City Hall', 'Raffles Place', 'Tanjong Pagar', 'Outram Park', 'Tiong Bahr                                                                                      
rong East', 'Chinese Garden', 'Lakeside', 'Boon Lay', 'Pioneer', 'Joo Koon', 'Gu                                                                                      
anah Merah', 'Expo', 'Changi Airport'], 'NorthSouthLine': ['Jurong East', 'Bukit                                                                                      
ds', 'Admiralty', 'Sembawang', 'Canberra', 'Yishun', 'Khatib', 'Yio Chu Kang', '                                                                                      
rset', 'Dhoby Ghaut', 'City Hall', 'Raffles Place', 'Marina Bay', 'Marina South                                                                                       
Pass:  False                                                                                                                                                          
                                           #%%
=EastWestLine (EW)=
Pasir Ris, Tampines, Simei, Tanah Merah, Bedok, Kembangan, Eunos, Paya Lebar, Aljuned, Kallang, Lavender, Bugis, City Hall, Raffles Place, Tanjong Pagar, Outram Park, Tiong Bahru, Redhill, Queenstown, Commonwealth, Buona Vista, Dover, Clementi, Jurong East, Chinese Garden, Lakeside, Boon Lay, Pioneer, Joo Koon, Gul Circle, Tuas Crescent, Tuas West Road, Tuas Link

=EastWestLine (CG)=
Tanah Merah, Expo, Changi Airport

=NorthSouthLine=
Jurong East, Bukit Batok, Bukit Gombak, Choa Chu Kang, Yew Tee, Kranji, Marsiling, Woodlands, Admiralty, Sembawang, Canberra, Yishun, Khatib, Yio Chu Kang, Ang Mo Kio, Bishan, Braddell, Toa Payoh, Novena, Newton, Orchard, Somerset, Dhoby Ghaut, City Hall, Raffles Place, Marina Bay, Marina South Pier
#%%
def is_palindrome(num):
    my_list=str(num)
    index=0
    last_index=len(my_list)-1
    while index<len(my_list):
        front=index
        back=last_index-front
        if my_list[front]!=my_list[back]:
            return False
        
        index+=1
    return True

is_palindrome(123212)
#%%
l=[1,2,3]
l[2:]=[]





print(l)
#%%
def find_average(lst):
    total_average=[]
    total=0
    counter=0
    
    for i in range(len(lst)):
        if len(lst[i])==0:
            total_average.append(0)
        else:
            indiv_total=sum(lst[i])
            indiv_counter=len(lst[i])
            total+=indiv_total
            counter+=indiv_counter
            indiv_ave=indiv_total/indiv_counter
            total_average.append(indiv_ave)
            
    overall_ave=total/counter
    
    return total_average,overall_ave

#find_average([[3,4], [5,6,7], [-1,2,8]])           
find_average([[13.13,1.1,1.1], [], [1,1,0.67]])            
#%%
def transpose_matrix(a): 
    c_new=len(a)
    r_new=len(a[0])
    new_mat=[]
    
    for i in range(r_new):
        mini_mat=[]
        for j in range(c_new):
            mini_mat.append(a[j][i])
        new_mat.append(mini_mat)
    return new_mat


transpose_matrix([[-11,0,3], [4,0,6]]) 
#%%
phonebook =[
{ 'name': 'Andrew', 
 'mobile_phone' :9477865, 
 'office_phone' : 6612345, 
 'email': 'andrew@sutd.edu.sg'} ,
 { 'name': 'Bobby' , 
  'mobile_phone' :8123498 , 
  'office_phone' :6654321 , 
  'email': 'bobby@sutd.edu.sg'} ] 

def get_details(name, key, phonebook):
    for dd in phonebook:
        if dd['name']==name:
            return dd[key]
    
    
    
    
    
    
    
    
print(get_details('Andrew','mobile_phone',phonebook))

#%%

def get_base_counts(dna):
    dd={'A':0,'T':0,'G':0,'C':0}
    validchar='ATCG'
    for i in dna:
        if i in validchar:
            dd[i]+=1
        else:
            pass
    return dd

        
get_base_counts('GATTACA')
#%%
def max_list(inlist):
    list_ofmax=[]
    
    
    for i in range(len(inlist)):
        changing_max=inlist[i][0]
        for j in range(len(inlist[i])):
            if inlist[i][j]>changing_max:
                changing_max=inlist[i][j]
            else:pass
        list_ofmax.append(changing_max)
    return list_ofmax


max_list([[100], [1,7], [-8,-2,-1], [2]])
#%%
import copy
a=2
b=copy.deepcopy(a)
a=1
print(b)
#%%
def multiplication_table(n):
    if n<1:
        return none
    else:
        bigrow=[]
        for i in range(1,n+1,1):
            row=[]
            for j in range(i,n*i+1,i):
                row.append(j)
            bigrow.append(row)
        return bigrow
        
multiplication_table(7)
#%%
def diff(p):
    dp={}
    keys=p.keys()
    for i in keys:
        if i!=0:
            dp[i-1]=i*p[i]
    retrun dp
#%%
def longest_common_prefix(string1, string2):
    common_pref=''
    if string1[0]!=string2[0]: 
        return ''
    else:
        len_str1=len(string1)
        len_str2=len(string2)
        if len_str1<len_str2:
            shortest_len=len_str1
        else:
            shortest_len=len_str2
        for i in range(shortest_len):
            if string1[i]==string2[i]:
                common_pref=common_pref + str(string1[i])
            else:
                break
    return common_pref

longest_common_prefix("distancetion", "distance")  

#%%
class Coordinate:
    x = 0
    y = 0

def get_maxmin_mag(f):
    lines=f.readlines()
    for line in lines:
        line=line.strip()
        line=line.split()
    #%%
my_list=[1,2,3,4,5,6,7,8,9]
print(my_list[0:4:1])
print(my_list[2:3])
#%%

x=[1,2,3,4]
x[2:3:1]=[0]
print(x) 

        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
            




































































	