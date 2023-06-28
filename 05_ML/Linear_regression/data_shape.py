import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import datasets


X, y = datasets.make_regression(
    n_samples=100, n_features=1, noise=20, random_state=4
)

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=1234
)

print(X_train.shape)
print(y_train.shape)

print(X_test)
print(y_test)