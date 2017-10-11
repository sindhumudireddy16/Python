from sklearn import datasets
from sklearn import svm   # To fit the svm classifier
from sklearn import cross_validation as cv
import numpy as np
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
#load the dataset
digits = datasets.load_digits()
X = digits.data[:,2:4]  # we only take the Sepal two features.
y = digits.target
X_train,X_test,y_train,y_test=cv.train_test_split(X,y,test_size=0.2)
C = 1.5  # SVM regularization parameter

# SVC with linear kernel
model=svm.SVC(kernel='linear', C=C)
svc = model.fit(X_train, y_train)
y_predict=model.predict(X_test)
print('SVM with linear kernel')
print('accuracy score',accuracy_score(y_test,y_predict))

model1=svm.SVC(kernel='rbf', gamma=0.7, C=C)
# SVC with RBF kernel
rbf_svc = model1.fit(X_train, y_train)
y_predict=model1.predict(X_test)
print('SVM with rbf kernel')
print('accuracy score',accuracy_score(y_test,y_predict))



h = .02  # step size in the mesh

# create a mesh to plot in
x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h),
                     np.arange(y_min, y_max, h))
# title for the plots
titles = ['SVC with linear kernel',
          'SVC with RBF kernel']

for i, clf in enumerate((svc, rbf_svc)):
    # Plot the decision boundary. For that, we will assign a color to each
    # point in the mesh [x_min, x_max]x[y_min, y_max].
    plt.subplot(2, 2, i + 1)
    plt.subplots_adjust(wspace=0.4, hspace=0.4)

    Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

    # Put the result into a color plot
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, cmap=plt.cm.coolwarm, alpha=0.8)

    # Plot also the training points
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm)
    plt.xlabel('age')
    plt.ylabel('Sex')
    plt.xlim(xx.min(), xx.max())
    plt.ylim(yy.min(), yy.max())
    plt.xticks(())
    plt.yticks(())
    plt.title(titles[i])

plt.show()