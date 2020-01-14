def simpsons_rule(f, n, a, b):
    
    if n<=0 or type(n)!=type(1):
        return None
    else:
        
        h=(b-a)/n
        
        first_term=f(a)
        
        sum_part2=0
        for j in range (1,int(n/2),1):
            x2j=a + j*h*2
            sum_part2=sum_part2+f(x2j)
        sum_part2=2*sum_part2
        
#        sum_part3=0
#        for k in range (1,n/2,1):
#            x2k=2*k-1
#            sum_part2=sumpart2+f(x2k)
#        sum_part3=4*sum_part2
        sum_part3=0
        for k in range (1,int(n/2)+1,1):
            x2j_minus1= a + 2*j*h - 1
            sum_part3 = sum_part3 + f( x2j_minus1 )
        sum_part3=sum_part3*4


        part4=f(b)

        finalsum=(h/3)*(first_term + sum_part2 + sum_part3 + part4)  
    return finalsum
            
def f(x):                                                                                                                                                                                                                                                                  
   return x**2    
                                                                                                                                                                                                                                                         
print(round(simpsons_rule(f,1000,1,3), 2))

