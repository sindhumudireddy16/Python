
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
from sklearn.cluster import KMeans

dataset = pd.read_csv("data.csv")

X = dataset.iloc[:, [0,1]].values

kmeans = KMeans(n_clusters = 3, init = 'k-means++')
y_kmeans = kmeans.fit_predict(X)

plt.scatter(X[y_kmeans == 0, 0], X[y_kmeans == 0, 1], s = 100, c = 'red', label = 'Medium')
plt.scatter(X[y_kmeans == 1, 0], X[y_kmeans == 1, 1], s = 100, c = 'blue', label = 'Large')
plt.scatter(X[y_kmeans == 2, 0], X[y_kmeans == 2, 1], s = 100, c = 'green', label = 'Small')

plt.legend()
plt.show()
