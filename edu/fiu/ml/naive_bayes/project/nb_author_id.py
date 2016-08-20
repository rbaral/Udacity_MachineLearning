#!/usr/bin/python
__author__ = 'rbaral'

"""
    This is the code to accompany the Lesson 1 (Naive Bayes) mini-project.
    Use a Naive Bayes Classifier to identify emails by their authors

    authors and labels:
    Sara has label 0
    Chris has label 1
"""

import sys, os
from time import time
sys.path.append("../../tools/")
print os.getcwd()
from email_preprocess import preprocess


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###
### import the sklearn module for GaussianNB
from sklearn.naive_bayes import GaussianNB
### create classifier
gnb = GaussianNB()
t0 = time()
### fit the classifier on the training features and labels
clf = gnb.fit(features_train,labels_train)
print "training time:", round(time()-t0, 3), "s"
#########################################################
'''
different ways to print the accuracy of the GNB classifier
'''
print "accuracy is:",clf.score(features_test,labels_test) # find the prediction score for the test data
t0 = time()
pred = clf.predict(features_test)
print "prediction time:", round(time()-t0, 3), "s"
from sklearn.metrics import accuracy_score
print "accuracy is:",accuracy_score(labels_test, pred)