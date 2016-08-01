__author__ = 'rbaral'

def testGNB1():
    from sklearn import datasets
    iris = datasets.load_iris()
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    y_pred = gnb.fit(iris.data, iris.target)
    print y_pred
    y_pred = y_pred.predict(iris.data)
    print y_pred
    print iris.target
    print("Number of mislabeled points out of a total %d points : %d"
          % (iris.data.shape[0],(iris.target != y_pred).sum()))

def testGNB():
    import numpy as np
    X = np.array([[-1, -1], [-2, -1], [-3, -2], [1, 1], [2, 1], [3, 2]])
    Y = np.array([1, 1, 1, 2, 2, 2])
    from sklearn.naive_bayes import GaussianNB
    clf = GaussianNB()
    print clf.fit(X, Y)
    #GaussianNB()
    print(clf.predict([[-0.8, -1]])) # need to pass 2-d array, as the 1-d array passing is deprecated in latest version of Sklearn
    #[1]
    #example of a partial fit
    clf_pf = GaussianNB()
    print clf_pf.partial_fit(X, Y, np.unique(Y))
    #GaussianNB()
    print(clf_pf.predict([[-0.8, -1]]))
    #[1]

if __name__=="__main__":
    testGNB()