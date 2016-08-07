__author__ = 'rbaral'
'''
#create the dataset and labels
X = [[0], [1], [2], [3]]
y = [0, 0, 1, 1]
from sklearn.neighbors import KNeighborsClassifier
# instantiate the KNeighborsClassifier class
neigh = KNeighborsClassifier(n_neighbors=3)
# train the classifier
neigh.fit(X, y)
# predict the lable for the test data
print(neigh.predict([[1.1],[1.6]]))

print(neigh.predict_proba([[0.9]]))
'''
from  prep_terrain_data import makeTerrainData
# prepare the training and test data
features_train, labels_train, features_test, labels_test = makeTerrainData()
# create the classifier
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=200, weights="distance", algorithm="brute")
# train the classifier
clf = clf.fit(features_train, labels_train)# gets the classifier that is fitted to this training data (features and label)
'''
different ways to print the accuracy of the GNB classifier
'''
print clf.score(features_test,labels_test) # find the prediction score for the test data
pred = clf.predict(features_test)
from sklearn.metrics import accuracy_score
print accuracy_score(labels_test, pred)
### draw the decision boundary with the text points overlaid
from class_vis import  prettyPicture, output_image
prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())