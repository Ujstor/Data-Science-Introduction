# Logistic regression

In machine learning, logistic regression is a widely used algorithm for binary classification tasks. The mathematical formulation of logistic regression involves a hypothesis function, a cost function, and an optimization algorithm. The logistic regression hypothesis function calculates the probability of the binary outcome based on the predictor variables. It uses the logistic function (also known as the sigmoid function) to map the linear combination of predictors to a value between 0 and 1.

# Aproximation

![equation](https://latex.codecogs.com/svg.image?\inline&space;\bg{black}\color{white}{\mathbf{\hat{y}}=\mathbf{wx}&plus;b})

![equation](https://latex.codecogs.com/svg.image?\inline&space;\bg{black}\color{white}{\mathbf{\hat{y}}=h_\theta(\mathbf{x})=\frac{1}{1&plus;e^{-(\mathbf{wx}&plus;b)}}})


- 𝑤 represents the weights or coefficients associated with the input features (𝑥) in a linear regression model.
- 𝑏 is the bias term.
- y = 𝑤𝑥 + 𝑏 represents the linear combination of the input features and the weights, plus the bias term.
- hθ(x) is the hypothesis function, which is the logistic function in logistic regression.

The sigmoid function (σ) is then applied to the linear combination to obtain the predicted output (𝑦̂) of the logistic regression model. The sigmoid function squashes the linear combination to a value between 0 and 1, representing the estimated probability of the target variable belonging to a particular class.

The goal of logistic regression is to find the optimal values for the parameter vector θ that best fit the training data and maximize the likelihood of the observed class labels. This is typically achieved through optimization algorithms such as gradient descent.

# Sigmoid function


![equation](https://latex.codecogs.com/svg.image?\inline&space;\bg{black}\color{white}{\sigma(x)=\frac{1}{1&plus;e^{-x}}})

The sigmoid function has an S-shaped curve, which makes it suitable for modeling probabilities. When x is positive, the sigmoid function outputs a value close to 1, indicating a high probability of the target variable being in class 1. Conversely, when x is negative, the sigmoid function outputs a value close to 0, indicating a high probability of the target variable being in class 0.

![sigmoid](https://qph.fs.quoracdn.net/main-qimg-6b67bea3311c3429bfb34b6b1737fe0c-lq)




# Cost function

![equation](https://latex.codecogs.com/svg.image?\inline&space;\large&space;\bg{red}\bg{black}\color{white}J(w,b)=J(\theta)-\frac{1}{n}\sum_{i=1}^{n}[y^{i}\log(h_{\theta}(x^{i}))&plus;(1-y^{i})\log(1-h_{\theta}(x^{i}))])

The cost function for logistic regression, denoted as J(θ) or J(w, b), measures the error or the discrepancy between the predicted probabilities (hθ(x)) and the actual class labels in the training data. The most commonly used cost function in logistic regression is the binary cross-entropy or log loss.

where:

- J(θ) is the cost function.
- θ represents the parameter vector (weights) of the logistic regression model.
- hθ(x) is the hypothesis function, which calculates the predicted probability that the target variable belongs to class 1, given input features x.
- y represents the actual class labels in the training data (0 or 1).
- m is the number of training examples.

In the cost function, the first term - y * log(hθ(x)) penalizes the model when the actual class label is 1 but the predicted probability is low. The second term - (1 - y) * log(1 - hθ(x)) penalizes the model when the actual class label is 0 but the predicted probability is high. The summation is taken over all training examples, and the overall cost is averaged by dividing by m.

The goal of logistic regression is to minimize this cost function by adjusting the parameters θ (weights) through optimization algorithms such as gradient descent. Minimizing the cost function helps to find the optimal parameters that best fit the training data and make accurate predictions.

# Gradient descent
The goal of logistic regression is to find the optimal values of the coefficients (θ) that minimize the cost function. This is achieved through an optimization algorithm such as gradient descent.

Gradient descent iteratively updates the coefficients in the direction of steepest descent of the cost function. The algorithm calculates the gradient (partial derivatives) of the cost function with respect to each coefficient and updates the coefficients accordingly.

The update rule for gradient descent in logistic regression is:
θj := θj - α * ∂J(θ) / ∂θj

Where:
- α is the learning rate, which controls the step size in each iteration.
- ∂J(θ) / ∂θj is the partial derivative of the cost function with respect to the j-th coefficient.

The gradient descent algorithm continues to update the coefficients until it converges to a minimum of the cost function or reaches a predefined number of iterations.

By optimizing the cost function using gradient descent, logistic regression finds the best-fitting model that maximizes the likelihood of the observed data and provides the coefficients necessary for predicting probabilities and making binary classifications.

<p align="center">
  <img src="https://i.imgur.com/HmgbQB8.png" alt="Centered" width="450" height="270">
</p>

![equation](https://latex.codecogs.com/svg.latex?%5Ccolor%7Bwhite%7Df%27%28w%2C%20b%29%20%3D%20%5Cbegin%7Bbmatrix%7D%20%5Cfrac%7B%5Cpartial%20f%7D%7B%5Cpartial%20w%7D%20%5C%5C%20%5Cfrac%7B%5Cpartial%20f%7D%7B%5Cpartial%20b%7D%20%5Cend%7Bbmatrix%7D%20%3D%20%5Cbegin%7Bbmatrix%7D%20%5Cfrac%7B1%7D%7BN%7D%20%5Csum%7B-2x_{i}%28y_{i}%20-%20%28wx_{i}%20%2B%20b%29%29%7D%20%5C%5C%20%5Cfrac%7B1%7D%7BN%7D%20%5Csum%7B-2%28y_{i}%20-%20%28wx_{i}%20%2B%20b%29%29%7D%20%5Cend%7Bbmatrix%7D)


# Update rule

w = w - α * dw

b = b - α * db

   ![equation](https://latex.codecogs.com/svg.latex?\color{white}dw\=\frac{1}{N}\sum_{i=1}^{N}(-2x_{i}(y_{i}-(wx_{i}&plus;b)))=\frac{1}{N}\sum_{i=1}^{N}2x_{i}(\hat{y}-y_{i}))


   ![equation](https://latex.codecogs.com/svg.latex?\color{white}db\=\frac{1}{N}\sum_{i=1}^{N}(-2(y_{i}-(wx_{i}&plus;b)))=\frac{1}{N}\sum_{i=1}^{N}2(\hat{y}-y_{i}))

   # Links for additional learning
- [Logistic Regression](https://ml-cheatsheet.readthedocs.io/en/latest/logistic_regression.html)
- [Logistic Regression — Detailed Overview](https://towardsdatascience.com/logistic-regression-detailed-overview-46c4da4303bc)

