    def __mul__(self,p2):     
        length1=len(self.coeff)

#         print(self.coeff)
#         print(p2.coeff)
        length2=len(p2.coeff)
        new_length=length1+length2-1
        new_list=[0]*new_length
        for i in range(length1):
            
            for j in range(length2):
                
                counter=i+j
                print(self.coeff[i],p2.coeff[j])
                new_list[counter]+=self.coeff[i]*p2.coeff[j]
        
        return new_list
    
    def differentiate(self):
        new_polynomial=[]
        for i in range(len(self.coeff)):
            x=self.coeff[i]*i
            new_polynomial.append(x)
        return new_polynomial
    
    def derivative(self):
        newPoly=Polynomial(self.coeff)
        newPoly.differentiate()
        return newPoly

#checker for mul
p = Polynomial([1, 2, 3])                                                                                                                                        
# q = Polynomial([2, 3])   
# r = p * q    
# print(r)         #should be [2, 7, 12, 9]
# print(p.differentiate())            #TAKE NOTE


p2 = Polynomial ([0, 1, 0, 0, -6, -1]) 
p5 =p2.derivative
print(type(p2))
print(type(p5))

## ---(Thu Apr 11 21:29:39 2019)---
def wordcount(s):
    new_list=s.split
    return new_list



print(wordcount('Tom Dick Harry'))
def wordcount(s):
    new_list=s.split
    return new_list



print(wordcount('Tom Dick Harry'))

word='helllo thereeee'
list=word.split
print(list)
def wordcount(s):
    new_list=s.split
    return new_list



print(wordcount('Tom Dick Harry'))

word='helllo thereeee'
list=word.split()
txt='welcome to the jungle'
x=txt.split
print(x)
txt='welcome to the jungle'
x=txt.split()
print(x)

## ---(Sat Apr 13 13:22:34 2019)---
ord(a)
ord('a')
ord('a')
ord('b')
chr(97)
for i in range(27):
    print(chr(i))
chr(97)
for i in range(97,97+27):
    print(chr(i))
for i in range(97,97+26):
    print(chr(i))
97
97+26
chr(123)
97+26
chr(123)
chr(122)

## ---(Thu Sep 12 10:48:32 2019)---
runfile('C:/Users/akmal/.spyder-py3/trial_PDF.py', wdir='C:/Users/akmal/.spyder-py3')