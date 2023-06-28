# Linear regression

Linear Regression is a supervised machine learning algorithm where the predicted output is continuous and has a constant slope. It’s used to predict values within a continuous range, (e.g. sales, price) rather than trying to classify them into categories (e.g. cat, dog). There are two main types.

Linear regression is a statistical modeling technique used to understand the relationship between a dependent variable and one or more independent variables. It assumes a linear relationship between the variables, where changes in the independent variable(s) are associated with a proportional change in the dependent variable.

The goal of linear regression is to find the best-fitting line, known as the regression line, that represents the relationship between the variables. This line can be used to make predictions or estimate the value of the dependent variable based on the values of the independent variable(s).

Simple linear regression uses traditional slope-intercept form, where m and b are the variables our algorithm will try to “learn” to produce the most accurate predictions. x represents our input data and y represents our prediction.

<p align="center">
  <img src="https://i.imgur.com/VuqEj3e.png" alt="Image" style="width: 500px; height: 400px;" />
</p>

Once the regression line is determined, it can be used for various purposes. It allows us to understand the direction and strength of the relationship between the variables. We can also use it to make predictions by plugging in values of the independent variable(s) into the equation and calculating the corresponding predicted values of the dependent variable.

Multiple linear regression extends the concept of linear regression to cases where there are multiple independent variables. The equation for multiple linear regression is similar to simple linear regression but includes coefficients for each independent variable

# Approximation

Simple linear regression uses traditional slope-intercept form, where **m** and **b** are the variables our algorithm will try to “learn” to produce the most accurate predictions. **x** represents our input data and **y** represents our prediction.

y = mx + b


where:
- y represents the dependent variable (also known as the response variable or target variable).
- x represents the independent variable (also known as the predictor variable or feature).
- m represents the weight or coefficient associated with X, indicating the impact of X on Y (slope).
- b represents the bias or intercept term, indicating the value of Y when X is zero.

The approximation formula suggests that the value of Y can be approximated by multiplying the weight (m) with X and adding the bias term (b). This represents a linear relationship between X and Y, where the slope (m) determines the direction and magnitude of the relationship, and the intercept (b) determines the starting point of the line.

# Cost Function

We use Mean Squared Error, or L2 loss. MSE measures the average squared difference between an observation’s actual and predicted values. The output is a single number representing the cost, or score, associated with our current set of weights. Our goal is to minimize MSE to improve the accuracy of our model.

![equation](https://latex.codecogs.com/svg.latex?\color{white}MSE=J(m,b)=\frac{1}{N}\sum_{i=1}^{n}(y_i-(mx_{1i}+x_{2i}))^2)

The minimum of the Mean Squared Error (MSE) function is important in linear regression because it represents the optimal values for the model's parameters (slope and intercept) that result in the best fit to the given data. 

The primary objective in linear regression is to find the values of the model parameters that minimize the MSE. This is because the MSE measures the average squared difference between the predicted values and the actual values. By minimizing the MSE, we are effectively minimizing the overall error or discrepancy between the predicted values and the actual values in the dataset.

When the MSE is minimized, it indicates that the model's predictions are as close as possible to the true values of the dependent variable. This is desirable because it means that the model is capturing the underlying relationship between the independent variable(s) and the dependent variable in the most accurate way.

Therefore, finding the minimum of the MSE function is crucial as it allows us to identify the optimal parameter values for the linear regression model, resulting in the best possible fit to the data and the most accurate predictions.

# Gradient Descent
To find the minimum of the Mean Squared Error (MSE) cost function using gradient descent, we iteratively update the parameter values in the opposite direction of the gradient until we converge to the minimum

![equation](https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Df%27%28m%2C%20b%29%20%3D%20%5Cbegin%7Bbmatrix%7D%20%5Cfrac%7B%5Cpartial%20f%7D%7B%5Cpartial%20m%7D%20%5C%5C%20%5Cfrac%7B%5Cpartial%20f%7D%7B%5Cpartial%20b%7D%20%5Cend%7Bbmatrix%7D%20%3D%20%5Cbegin%7Bbmatrix%7D%20%5Cfrac%7B1%7D%7BN%7D%20%5Csum%7B-2xi%28yi%20-%20%28mxi%20%2B%20b%29%29%7D%20%5C%5C%20%5Cfrac%7B1%7D%7BN%7D%20%5Csum%7B-2%28yi%20-%20%28mxi%20%2B%20b%29%29%7D%20%5Cend%7Bbmatrix%7D)


<p align="center">
  <img src="https://i.imgur.com/HmgbQB8.png" alt="Centered" width="450" height="270">
</p>


# Update Rule
In gradient descent, the update rules for the parameters (slope \(m\) and intercept \(b\)) are based on the gradient of the cost function and a learning rate (\(\alpha\)) that determines the step size of each parameter update. Here are the update rules:

Apologies for the oversight. Here are the update rules for gradient descent with the formulas replaced with LaTeX links for displaying in white color:

1. Update rule for slope \(m\):

   ![equation](https://latex.codecogs.com/svg.latex?\color{white}m%20%3A%3D%20m%20-%20%5Calpha%20%5Cfrac%7B%5Cpartial%20J%7D%7B%5Cpartial%20m%7D)

   Explanation: Update the slope \(m\) by subtracting the learning rate ![equation](https://latex.codecogs.com/svg.latex?\color{white}\alpha) times the partial derivative of the cost function with respect to \(m\).

2. Update rule for intercept \(b\):

   ![equation](https://latex.codecogs.com/svg.latex?\color{white}b%20%3A%3D%20b%20-%20%5Calpha%20%5Cfrac%7B%5Cpartial%20J%7D%7B%5Cpartial%20b%7D)

    Explanation: Update the intercept \(b\) by subtracting the learning rate ![equation](https://latex.codecogs.com/svg.latex?\color{white}\alpha) times the partial derivative of the cost function with respect to \(b\).

In these update rules, ![equation](https://latex.codecogs.com/svg.latex?\color{white}\frac{\partial%20J}{\partial%20m}%20\text{}%20\frac{\partial%20J}{\partial%20b}) represent the partial derivatives of the cost function with respect to the parameters \(m\) and \(b\) respectively.

The learning rate ![equation](https://latex.codecogs.com/svg.latex?\color{white}\alpha) determines the step size of each parameter update. It controls the convergence speed and influences the stability of the optimization process. A larger learning rate can lead to faster convergence but may cause overshooting, while a smaller learning rate can provide more stable but slower convergence.

Choosing an appropriate learning rate is important for effective gradient descent. The optimal value often requires experimentation and tuning based on the specific dataset and problem.

Note that these formulas are specific to gradient descent and are used to update the parameters iteratively in order to minimize the cost function and find the optimal values for \(m\) and \(b\).

<p align="center">
  <img src="https://i.imgur.com/hPE5ANb.png" alt="Centered" width="600" height="300">
</p>

# Links for additional learning
- [Linear Regression](https://ml-cheatsheet.readthedocs.io/en/latest/linear_regression.html)
- [Gradient Descent](https://ml-cheatsheet.readthedocs.io/en/latest/gradient_descent.html)

