#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()




#########################################################
### your code goes here ###
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

num_features = len(features_train[0])
print "number of features = " + str(num_features)
dt_clf = DecisionTreeClassifier(min_samples_split=40)
dt_clf = dt_clf.fit(features_train, labels_train)
labels_predict = dt_clf.predict(features_test)
accuracy = accuracy_score(labels_predict, labels_test)
print "Accuracy without tuning parameters = " + str(accuracy)


#########################################################


