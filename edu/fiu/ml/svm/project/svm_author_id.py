#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../../tools/")
from email_preprocess import preprocess
from class_vis import prettyPicture, output_image
import numpy as np

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#slice the training data to see the time difference in training small data set
#features_train = features_train[:len(features_train)/100]
#labels_train = labels_train[:len(labels_train)/100]


#########################################################
### your code goes here ###
from sklearn.svm import SVC
clf = SVC(kernel="rbf", C = 10000.0) # initialize a svm classifier
t0 = time()
clf.fit(features_train, labels_train) # train the classifier
print "training time:", round(time()-t0, 3), "s"
t0 = time()
pred = clf.predict(features_test) # make the prediction
print "prediction time:", round(time()-t0, 3), "s"
#find the predictions of some elements
#print pred[10], pred[26], pred[50]
#find the number of test elements, predicted for Chris (1) class
chrisClass = np.where((np.array(pred))>0)[0]
print "ChrisClass count:", len(chrisClass)
# now find the accuracy of the prediction
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)
print "accuracy is:",accuracy
#########################################################
### draw the decision boundary with the text points overlaid
#prettyPicture(clf, features_test, labels_test)
#output_image("test.png", "png", open("test.png", "rb").read())

