# K-Nearest Neighbors (KNN)

The K-Nearest Neighbors (KNN) algorithm is a simple and widely used supervised machine learning algorithm used for both classification and regression tasks. It is a non-parametric method that makes predictions based on the similarity between the new input and the labeled data points in the training set.

Here's how the KNN algorithm works:

1. **Data Preparation**: First, you need to preprocess and prepare your data. This includes cleaning the data, handling missing values, and normalizing numerical features if necessary.

2. **Choosing the Value of K**: K is the number of nearest neighbors to consider for making predictions. You need to choose an appropriate value for K, which can significantly impact the performance of the algorithm. A small value of K makes the algorithm more sensitive to noise, while a large value of K can cause the algorithm to generalize too much and overlook local patterns.

3. **Calculating Distance**: The algorithm calculates the distance between the new input and all the labeled data points in the training set. Euclidean distance is commonly used, but other distance metrics like Manhattan distance or cosine similarity can also be used.

4. **Finding K Neighbors**: The KNN algorithm selects the K nearest neighbors based on the calculated distances. These neighbors are the K data points with the shortest distance to the new input.

5. **Majority Voting (Classification)**: In classification tasks, each of the K nearest neighbors "votes" for their class label, and the class with the highest number of votes is assigned to the new input as its predicted class.

6. **Averaging (Regression)**: In regression tasks, the algorithm averages the target values of the K nearest neighbors and assigns the mean value as the predicted value for the new input.

7. **Prediction**: Once the majority voting or averaging is done, the algorithm assigns the predicted class label (classification) or predicted value (regression) to the new input.

8. **Model Evaluation**: Finally, you evaluate the performance of the KNN model using appropriate evaluation metrics such as accuracy, precision, recall, F1 score, or mean squared error, depending on the task.

It's worth noting that KNN is a lazy learning algorithm, meaning it doesn't have a separate training phase. Instead, it memorizes the training data and uses it for making predictions directly.

However, KNN has some limitations. It can be computationally expensive, especially with large datasets, as it requires calculating distances for each new input. Additionally, the algorithm is sensitive to the choice of distance metric and the value of K. Also, it assumes that all features contribute equally to the similarity, which might not be true in some cases.

To mitigate some of these limitations, techniques like feature scaling, dimensionality reduction, and using weighted distances can be employed.

<br>
<br>

# Euclidean distance

Euclidean distance between two points in n-dimensional space:

![equation](https://latex.codecogs.com/svg.latex?\color{white}\text{Euclidean%20Distance}=\sqrt{\sum_{i=1}^n(x_{2i}-x_{1i})^2})

In this formula, ![equation](https://latex.codecogs.com/svg.latex?\color{white}x_{1i}) and ![equation](https://latex.codecogs.com/svg.latex?\color{white}x_{2i}) represent the coordinates of the two points in each dimension from i=1 to n. The formula computes the square of the differences in each dimension, sums them up, and then takes the square root of the sum to obtain the Euclidean distance.

For example, in 2D space, the formula would be:

Euclidean Distance: ![equation](https://latex.codecogs.com/svg.latex?\color{white}\sqrt{(x_2-x_1)^2+(y_2-y_1)^2})

And in 3D space, the formula would be:

Euclidean Distance: ![equation](https://latex.codecogs.com/svg.latex?\color{white}\sqrt{(x_2-x_1)^2+(y_2-y_1)^2+(z_2-z_1)^2})

<br>
<br>

# Data Set

The dataset used is the Iris dataset, which is a widely used dataset in machine learning. It contains measurements of four features (sepal length, sepal width, petal length, and petal width) of three different species of Iris flowers (Setosa, Versicolor, and Virginica). The dataset is loaded using the `datasets.load_iris()` function from the scikit-learn library.

Here's a breakdown of the code:

1. Import necessary libraries and define a color map for visualization:
   ```python
   import numpy as np
   from sklearn import datasets
   from sklearn.model_selection import train_test_split
   import matplotlib.pyplot as plt
   from matplotlib.colors import ListedColormap

   camp = ListedColormap(['#FF0000', '#00FF00', '#0000FF'])
   ```

   The required libraries are imported, including NumPy, scikit-learn's datasets module, Matplotlib, and a color map (`ListedColormap`) for plotting.

2. Load and split the Iris dataset into training and testing sets:
   ```python
   iris = datasets.load_iris()
   X, y = iris.data, iris.target

   X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1234)
   ```

   The Iris dataset is loaded using `datasets.load_iris()`. The features are stored in `X`, and the corresponding labels are stored in `y`. The dataset is then split into training and testing sets using `train_test_split()` function from scikit-learn. The training set consists of 75% of the data, while the remaining 25% is used for testing.
   - `X` represents the feature matrix and contains the measurements of the attributes of Iris flowers. Each row in `X` corresponds to a single flower, and each column represents a different attribute.
   - `y` represents the target vector and contains the corresponding species labels for each flower in `X`.



1. Instantiate and train the KNN classifier:
   ```python
   from knn import KNN

   clf = KNN(k=3)
   clf.fit(X_train, y_train)
   ```

   The code imports a custom KNN class from a file named `knn.py` and creates an instance of this class with `k=3`, indicating that the KNN algorithm will be used with 3 neighbors. The classifier is then trained on the training data and labels using the `fit()` method.

2. Make predictions on the test data:
   ```python
   predictions = clf.predict(X_test)
   ```

   The trained classifier is used to make predictions on the test data (`X_test`) using the `predict()` method of the KNN class.

3. Calculate and print the accuracy of the classifier:
   ```python
   acc = np.sum(predictions == y_test) / len(y_test)
   print(acc)
   ```

   The code calculates the accuracy of the classifier by comparing the predicted labels (`predictions`) with the true labels of the test data (`y_test`). The accuracy is computed as the ratio of correct predictions to the total number of test samples and is then printed.