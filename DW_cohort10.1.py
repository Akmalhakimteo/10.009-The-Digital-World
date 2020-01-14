# -*- coding: utf-8 -*-
"""
Created on Mon Apr  1 13:15:10 2019

@author: akmal
"""

import numpy as np
a=np.array([[0,2,4,8],[1,2]])
print(a.shape) #return the smallest dimension

#%%
import numpy as np
from sklearn.metrics import confusion_matrix

def get_metrics(actual_targets, predicted_targets, labels):
    
    c_matrix = confusion_matrix(actual_targets, predicted_targets, labels)
    
    # your code here
    total=float(sum(sum(c_matrix)))
    correct_predictions=float(c_matrix[0][0]+c_matrix[1][1])
    correct_positives=float(c_matrix[1][1])
    total_negatives=float(sum(c_matrix[0,:]))
    total_positives=float(sum(c_matrix[1,:]))
    false_positives=float(c_matrix[0][1])
    
    output = {
        'confusion matrix': c_matrix,
        'total records': int(total),
        'accuracy': round(correct_predictions/total,3),
        'sensitivity': round(correct_positives/total_positives,3),
        'false positive rate': round(false_positives/total_negatives,3)
    
    
    }
    
    return output

#%%
from numpy import percentile
from numpy.random import rand

date=rand(1000)
quartiles= percentile(data, [25,50,75])
data_min , data_max = data.min(),data.max()

#%% COHORT 3
from sklearn.model_selection import train_test_split 
from sklearn import neighbors, datasets
from sklearn.metrics import confusion_matrix
import numpy as np

# place any functions you need from CS1-3 here

def knn_classifier(bunchobject, feature_list, size, seed , k ): 
    pass



#%%

from sklearn.model_selection import train_test_split 
from sklearn import neighbors, datasets
from sklearn.metrics import confusion_matrix
import numpy as np
import matplotlib.pyplot as plt

def display_bar_chart(positions,counts,names,title_name='default'):
    plt.bar(positions, counts, alighn='center')
    plt.xticks(positions,names)
    plt.show()
        
bunchobject = datasets.load_breast_cancer()

unique, counts = np.unique(bunchobject.target, return_counts=True)
display_bar_chart(unique,counts,bunchobject.target_names)

#%% qn 4?

from sklearn.model_selection import train_test_split

def knn_classifier(bunchobject, feauture_list, size, seed, k):
    data= bunchobject.data[:,feature_list]
    target = bunchobject.targer
    data =normalize_minmax(data)
    
    data_train, data_test, target_train, target_test = train_test_split (data, target, )
    
    clf = neighbors.KneighborsClassifier(k)
    clf.fit(data_train,target_train)
    
    predicted_targets = clf.predict (data_test)
    
    results = get_metrics(target_test, predicted_targets, [1,0])
    
    return results 
#%%
    
class Person():
    def __init__(self,name="", hair="brown"):
        self.name=name
        self.hair=hair
        
    def get_name(self):
        return self._name
    
    def set_name(self,new_name):
        self._name=new_name
        
    def get_hair(self):
        return self._hair
    
    def set_hair(self,new_hair):
        if new_hair in ["brown","blue","grey","violet","black"]:
            
        
    name=property(get_name,set_name)
    hair=property(get_hair,set_hair)
    
p1=Person("Akmal","black")
print(p1)
    
    
    


    























