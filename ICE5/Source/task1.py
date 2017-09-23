import numpy as np
import matplotlib.pyplot as plt


X=np.array([0,1,2,3,4,5,6,7,8,9])
Y=np.array([1,3,2,5,7,8,8,9,10,12])
xMean=np.mean(X)
yMean=np.mean(Y)
B1=(np.sum((X-xMean)*(Y-yMean)))/(np.sum(np.power((X-xMean),2)))
B0=yMean-(B1*xMean)
print(np.mean(X)*np.mean(Y))
plt.scatter(X,Y)
ry=B1*X+B0
print(B1)
print(B0)
print(xMean)
print(yMean)
plt.plot(X,ry)
plt.show()