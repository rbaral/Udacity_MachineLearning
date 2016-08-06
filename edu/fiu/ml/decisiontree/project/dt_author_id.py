#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../../tools/")
from email_preprocess import preprocess

### your code goes here--should return a trained decision tree classifer
def classify(features_train, labels_train, minsplit):
    from sklearn import tree
    clf = tree.DecisionTreeClassifier(min_samples_split= minsplit)
    t0 = time()
    clf = clf.fit(features_train, labels_train)
    print "train time is:",str(time() - t0)+"s"
    return clf

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()


print "number of features:", len(features_train[0])

#########################################################
### your code goes here ###
clf = classify(features_train, labels_train, 40)
pred = clf.predict(features_test)
from sklearn.metrics import accuracy_score
acc_min_samples_split_2 = accuracy_score(labels_test, pred)
print "accuracy is:",acc_min_samples_split_2
#########################################################


