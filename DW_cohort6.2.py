# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 15:35:59 2019

@author: akmal
"""

s="hello"
print(s.strip("lo"))
#%%
check_input_length=False
check_alphanumeric=False
check_atleast2digit=False

if len(password)>=8:
    check_input_length=True
if password.isalnum():
    check_alphanumeric=True

count_digit=0

for i in range(0,len(password)):
    if (password[i].isdigit()):
        count_digit+=1
if count_digit>=2:
    check_atleast2digit=True
else:
    return False
    
if check_alphanumeric==True and check_atleast2digit==True and check_input_length==True:
    return True
else:
    return False

#%% opening file
filename="lyrics.txt" 
fileObject=open(filename,mode)
#filename- input.txt path/...
'''   'w' write only, 'w+'write and read, 
      'r' read only, 'r+' write and read
      
       'a+' read + append. will also create new
       file name if it doesnt exist'''
print(fileObject.read())
fileObject.close()

#%%
filename="lyrics.txt"
fileObject=open(filename)
string=fileObject.readline()

while (string!=''):
    print(string)
    string=fileObject.readline()
    #%%
mylist=["  1","2 "]
#for item in mylist:
#    item.strip(" ")    #COS STRING IS IMMUTABLE
#print(mylist)

'''better way'''

for i in range(0,len(mylist)):
    mylist[i]=int(mylist[i].strip())
    
print(mylist)
#%% how not to let python crash
def tryread():

    filename="nonexistantfile.txt"
    
    try:
        fileObject=open(filename,'r')
        
    for line in fileObject:
        print(line)
        
    except:
        print(f'File : {filename} not found.')
        exit()
            
fileObject.close()



    































