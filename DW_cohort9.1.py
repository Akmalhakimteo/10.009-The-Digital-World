'''STATE FUNCTIONS WEEK 9'''

from libdw import sm

class SM:
    def start(self):
        self.state = self.startState
    def step(self,input):
        (state,output)= self.getNextValues(self.state,input)
        self.state =state
        return output
    def transduce(self,inputs):
        outputs = []
        for input_value in inputs:
            output.append(self.step(input_value))
        return outputs

class CM(sm.SM):
    def __init__(self):
        self.start_state=0
    
    def get_next_values(self,state,inp):
        if state==0 and inp==100:  #all cases of table
            return (0 ,(0,"coke",0 ))
        
        elif state==1 and inp==100:
            return (0,(0,'coke',50))
        
        elif state==1 and inp==50:
            return (0,(0,'coke',0))
        
        elif state==0 and inp==50:
            return (1,(50 , '-', 0))
        else:                     #this part handles illegal input
            if state==1:          
                balance=50
            else:
                balance=0
            return (state,(balance,'-',inp))            
        
mycokemachine=CM()
mycokemachine.start()
print(mycokemachine.step(50))
print(mycokemachine.step(100))
print(mycokemachine.transduce(100,100,50,50))        


            
    
    
    
# '''   def start(self):
#        self.state=self.startState #refer to next hashtag
#        
#    def step(self,input):
#        (state, output) = self.getNextValues(self.state,input)
#        self.state=state           #these have to be implemented by the class that inherits the SM
#        return output 
#    '''
#%% FROM VOCAREUM qn 1

''' class CM(sm.SM):
    start_state = None

    def get_next_values(self,state, inp):
        pass '''
    
from libdw import sm

class CM(sm.SM):
    def __init__(self):
        self.start_state=0
    
    def get_next_values(self,state,inp):
        if state==0 and inp==100:  #all cases of table
            return (0 ,(0,"coke",0 ))
        
        elif state==1 and inp==100:
            return (0,(0,'coke',50))
        
        elif state==1 and inp==50:
            return (0,(0,'coke',0))
        
        elif state==0 and inp==50:
            return (1,(50 , '--', 0))
        else:                     #this part handles illegal input
            if state==1:          
                balance=50
            else:
                balance=0
            return (state,(balance,'--',inp))            
        
'''mycokemachine=CM()
mycokemachine.start()
print(mycokemachine.step(50))
print(mycokemachine.step(100))
print(mycokemachine.transduce(100,100,50,50))    '''   

#%% qn 2
from libdw import sm


class SimpleAccount(sm.SM):
            
    def __init__(self,money):
        self.balance=money
        if money>=100:
            self.startstate=1
        else:
            self.startstate=0
    
    def get_next_values(self,state,inp):
        new_balance=self.balance + inp
        if (new_balance>=100):
            self.balance=new_balance
            return 1,new_balance
        
        elif (inp<0 and state==0):
            self.balance=new_balance-5
            return 0, self.balance
        
        elif (inp<0 and state==1):
            self.balance=new_balance
            if self.balance>=100:
                return 1,new_balance
            else:
                return 0,new_balance
            
        elif (inp>0 and state==0):
            self.balance=new_balance
            if self.balance>=100:
                return 1,new_balance
            else:
                return 0,new_balance
            
        elif (inp>0 and state==1):
            self.balance = new_balance
            return 1,new_balance
        
        #%%
        
from libdw import sm

class CommentsSM(sm.SM):
    start_state = None

    def get_next_values(self, state, inp):
        pass
#%%
from libdw import sm

class CommentsSM(sm.SM):
    start_state = 0

    def get_next_values(self, state, inp):
        
        if state==0 and inp!='#':
            return (0,None)
        
        elif state==0 and inp=='#':
            return (1, inp)
            
        elif state==1 and inp!='\n':
            return (1, inp )
        
        elif state==1 and inp=='\n':
            return (0,None)
        
        pass
        


    
    
    
    
    
    
    
    

            
    





































