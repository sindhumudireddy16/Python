from sklearn import linear_model
from sklearn import datasets
import matplotlib.pyplot as plt
import numpy as np
dataset=datasets.load_diabetes()

bmi=dataset.data[:,np.newaxis,2] #took bmi as x variable
x_train=bmi[:-20] # x train data
x_test=bmi[-20:] # x test data
y_train=dataset.target[:-20] # y train data
y_test=dataset.target[-20:] # y test data
model=linear_model.LinearRegression()
model.fit(x_train,y_train)  # build a model
y_predict=model.predict(x_test) # make prediction
#Training set visualization
plt.scatter(x_train, y_train, color = 'red')
plt.plot(x_train, model.predict(x_train), color = 'blue')
plt.title('Bmi vs diabetes levels')
plt.xlabel('Bmi')
plt.ylabel('diabetes levels')
plt.show()
#test set visualization
plt.scatter(x_test, y_test, color = 'red')
plt.plot(x_test, model.predict(x_test), color = 'blue')
plt.title('Bmi vs diabetes levels')
plt.xlabel('Bmi')
plt.ylabel('diabetes levels')
plt.show()