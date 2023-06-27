import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
camp = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])

iris = datasets.load_iris()
X, y = iris.data, iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1234)

print(X_train.shape)
print(X_train)

print(y_train.shape)
print(y_train)


# plt.figure()
# plt.scatter(X[:, 0], X[:, 1], c=y, cmap=camp, edgecolor='k', s=20)
# plt.show()


from knn import KNN
clf = KNN(k=3)
clf.fit(X_train, y_train)
predictions = clf.predict(X_test)

acc = np.sum(predictions == y_test) / len(y_test)
print(acc)


