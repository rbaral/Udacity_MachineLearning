#!/usr/bin/python
__author__ = 'rbaral'

import numpy as np
import matplotlib
matplotlib.use('agg')

import matplotlib.pyplot as plt
from studentRegression import studentReg
from class_vis import prettyPicture, output_image

from ages_net_worths import ageNetWorthData

ages_train, ages_test, net_worths_train, net_worths_test = ageNetWorthData()

reg = studentReg(ages_train, net_worths_train)

#predict the networth for a sample age
sampleData = np.array(29).reshape(-1,1) # this was required to avoid the deprecated warning message
print "At age 29, the predicted networth is:",reg.predict(sampleData)
#get the slope
print "slope is:",reg.coef_
#get the intercept
print "intercept is:",reg.intercept_
#get the r-squared for the train and test data
r_squared_train = reg.score(ages_train, net_worths_train)
print "r_squared_train is:",r_squared_train
r_squared_test = reg.score(ages_test, net_worths_test)
print "r_squared_test:",r_squared_test
plt.clf()
plt.scatter(ages_train, net_worths_train, color="b", label="train data")
plt.scatter(ages_test, net_worths_test, color="r", label="test data")
plt.plot(ages_test, reg.predict(ages_test), color="black")
plt.legend(loc=2)
plt.xlabel("ages")
plt.ylabel("net worths")


plt.savefig("test.png")
output_image("test.png", "png", open("test.png", "rb").read())
