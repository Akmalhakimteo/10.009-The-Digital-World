#def temp_convert(choice, temp):
#    if choice==C:
#    

#temp_convert(choice,temp)
def temp_convert(choice, temp):
    if choice!='C' and choice!='F':
        return None
    else:
        if choice=='F':
            t_fahrenheit=temp*(9/5)+32
            return t_fahrenheit
        elif choice=='C':
            t_celcius=(temp-32)*(5/9)
            return t_celcius
    
print(temp_convert('C',322))
    
#%%
def is_prime(n):
    if n==2:
        return True
    if n==1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
        
print(is_prime(9))
        
#%%
import math
def approx_ode(h,t0,y0,tn):
    while t0<tn:
        differential = 3 + math.e**(-t0) - (1/2)*y0
        y1 = y0 + h * differential
        t1 = h + t0
        t0=t1
        y0=y1
        
    return y0
    
print (approx_ode(0.1,0,1,0))

    
    
    
#    
#    for i in range(10):
#        differential= 3 + math.e**(-t0) - (1/2)*y0
#        y1= y0 + h * differential
#        y0=y1
#        t0=h+tn
#        return y0
#        return t0
#    
    



#take the values and compute y1
#take values and compute y2 
#take values of y2 and compute y3
    
    
    
    
    # Inputs - h  : step size
    #          t0 : initial t value (at step 0)
    #          y0 : initial y value (at step 0)
    #          tn : t value at step n
    # Add your code below!
    
    #%%
#    def approx_ode(h,t0,y0,tn):
#    # Inputs - h  : step size
#    #          t0 : initial t value (at step 0)
#    #          y0 : initial y value (at step 0)
#    #          tn : t value at step n
#    # Add your code below!
#    pass
#
    