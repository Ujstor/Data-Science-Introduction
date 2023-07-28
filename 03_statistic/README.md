Examples and Exercises from Think Stats, 2nd Edition

http://thinkstats2.com

Copyright 2016 Allen B. Downey

MIT License: https://opensource.org/licenses/MIT

![purple-divider](https://user-images.githubusercontent.com/7065401/52071927-c1cd7100-2562-11e9-908a-dde91ba14e59.png)

# NSFG Cycle 6 (2002)
The National Survey of Family Growth (NSFG) gathers information on pregnancy and births, marriage and cohabitation, infertility, use of contraception, family life, and general and reproductive health.

[Codebooks and Documentation](https://www.cdc.gov/nchs/nsfg/nsfg_cycle6.htm)

## Variables

We have already seen two variables in the NSFG dataset, caseid and pregordr, and we have seen that there are 244 variables in total. Following variables are used:

- **caseid** is the integer ID of the respondent.
- **prglngth** is the integer duration of the pregnancy in weeks.
outcome is an integer code for the outcome of the pregnancy. The code 1 indicates a live birth.
- **pregordr** is a pregnancy serial number; for example, the code for a respondent’s first pregnancy is 1, for the second pregnancy is 2, and so on.
- **birthord** is a serial number for live births; the code for a respondent’s first child is 1, and so on. For outcomes other than live birth, this field is blank.
- **birthwgt_lb** and** birthwgt_oz** contain the pounds and ounces parts of the birth weight of the baby.
- **agepreg** is the mother’s age at the end of the pregnancy.
- **finalwgt** is the statistical weight associated with the respondent. It is a floating-point value that indicates the number of people in the U.S. population this respondent represents.

<br>

![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)

# Dataset Summary Statistics

This repository contains summary statistics for a given dataset. The summary statistics provide an overview of the dataset and describe various characteristics of the data. The following summary statistics are included:

## Mean (Average)

The mean represents the average value of the dataset, indicating the central tendency.

Example:
Given a dataset [3, 4, 5, 6, 7], the mean is 5.


![Mean Formula](https://latex.codecogs.com/svg.image?\bg{white}\colorbox{white}{$\displaystyle\bar{X}=\frac{1}{n}\sum_{i=1}^{n}X_i$})

## Median

The median is a statistical measure used to describe the central tendency of a dataset. It represents the middle value when the data points are arranged in ascending or descending order.

For a dataset with an odd number of data points, the median is the value that separates the lower and upper halves of the dataset. It is the middle value when the data points are arranged in order.

For a dataset with an even number of data points, the median is the average of the two middle values. It is the average of the two values that divide the dataset into equal halves when arranged in order.

The median is a robust measure of central tendency as it is less affected by extreme values or outliers compared to other measures like the mean

Formula:
If \(n\) is odd, the median is the value at position 

![](https://latex.codecogs.com/svg.image?\colorbox{white}{$\displaystyle\text{Median}=X_{\left(\frac{n&plus;1}{2}\right)}$})

If \(n\) is even, the median is the average of the values at positions 

![](https://latex.codecogs.com/svg.image?\colorbox{white}{$\displaystyle\text{Median}=\frac{X_{\left(\frac{n}{2}\right)}&plus;X_{\left(\frac{n}{2}&plus;1\right)}}{2}$})

## Mode

The mode represents the most frequently occurring value(s) in a dataset.

Example:
Given a dataset [3, 4, 5, 5, 6, 7], the mode is 5.

Formula:
No specific formula - it is the value(s) that occur with the highest frequency.

## Variance

The variance is a statistical measure that quantifies the spread or dispersion of a dataset. It provides a measure of how far each value in the dataset is from the mean.

In mathematical terms, the variance is defined as the average of the squared differences between each data point and the mean.



![Variance Formula](https://latex.codecogs.com/svg.image?\bg{white}\colorbox{white}{$\displaystyle&space;S^2=\frac{1}{n-1}\sum_{i=1}^{n}(X_i-\bar{X})^2$})

The formula calculates the squared difference between each data point and the mean, sums up these squared differences, and then divides the sum by the total number of data points.

The variance provides a measure of the variability or spread of the dataset. A higher variance indicates that the data points are more dispersed around the mean, while a lower variance indicates that the data points are closer to the mean.

It's worth noting that the formula shown above represents the population variance. For sample variance, the formula is adjusted by dividing the sum of squared differences by (n-1) instead of n.

## Standard Deviation

is a measure of the dispersion or variability of a dataset. It is calculated as the square root of the average of the squared differences between each data point and the mean. The formula provides a measure of how spread out the data is from the mean.


![Standard Deviation Formula](https://latex.codecogs.com/svg.image?\bg{white}\colorbox{white}{$\displaystyle\sigma=\sqrt{\frac{1}{n}\sum_{i=1}^{n}(X_i-\bar{X})^2}$})

## Range

The range represents the difference between the maximum and minimum values in a dataset.

Example:
Given a dataset [3, 4, 5, 6, 7], the range is 7 - 3 = 4.


![Range Formula](https://latex.codecogs.com/png.latex?\dpi{120}&space;\bg_white&space;\fn_phv&space;\large&space;\text{range}&space;=&space;\text{max}-\text{min})


## Effect Size: Cohen's d

Cohen's d is an effect size measure commonly used to quantify the standardized difference between two group means. It helps assess the magnitude of the difference between two groups, taking into account the variability within each group.
Cohen's d is defined as:

![Cohen's d Formula](https://latex.codecogs.com/svg.image?\bg{white}\colorbox{white}{$\displaystyle&space;d=\frac{\bar{X}_1-\bar{X}_2}{s}$})

The pooled standard deviation (ss) is calculated using the formula:

![](https://latex.codecogs.com/svg.image?\bg{white}\colorbox{white}{$\displaystyle&space;s=\sqrt{\frac{{(n_1-1)s_1^2&plus;(n_2-1)s_2^2}}{{n_1&plus;n_2-2}}}$})

where:
- \(n_1\) and \(n_2\) are the sample sizes of Group 1 and Group 2, respectively.
- \(s_1\) and \(s_2\) are the standard deviations of Group 1 and Group 2, respectively.



Interpreting Cohen's d:
Cohen proposed general guidelines to interpret the magnitude of Cohen's d:
- Small effect size: \(d \approx 0.2\)
- Medium effect size: \(d \approx 0.5\)
- Large effect size: \(d \approx 0.8\)

These guidelines help assess the practical significance of the difference between the group means.

Cohen's d is widely used in various fields, such as psychology, education, and social sciences, to evaluate the impact or strength of an intervention, treatment, or experimental manipulation. It provides a standardized measure of effect size, allowing for comparisons across different studies or contexts.

![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)

# Probability Mass Function (PMF)

A Probability Mass Function (PMF) is a function that describes the probability distribution of a discrete random variable. It assigns probabilities to each possible value that the random variable can take.

Mathematically, the PMF of a discrete random variable X is defined as:

P(X = x)

where P(X = x) represents the probability that X takes on the value x.

Properties of a PMF include:

1. Non-negativity: The PMF is non-negative, meaning that the probabilities assigned to each value are greater than or equal to zero.

2. Sum of probabilities: The sum of all probabilities in the PMF is equal to 1. This implies that the random variable must take on one of the possible values.

From the PMF, we can calculate various properties of the random variable. For example, the expected value or mean of a discrete random variable X can be calculated as:

E(X) = ∑(x * P(X = x))

where the summation is taken over all possible values of X.

The PMF allows us to compute probabilities associated with specific events or intervals. For example, the probability that X equals a particular value x can be obtained directly from the PMF:

P(X = x) = P(X = x)

Additionally, the probability that X lies within a range [a, b] can be computed as the sum of the individual probabilities within that range:

P(a ≤ X ≤ b) = ∑(P(X = x)) for all x in [a, b]

The PMF is commonly used in probability theory and statistics to analyze and model discrete random variables, such as the outcomes of rolling a dice or the number of successes in a series of independent Bernoulli trials.

![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# Precentiles

Percentiles are statistical measures that divide a set of data into hundredths. They represent specific points in a distribution, indicating the relative position of a particular value within the dataset.

To calculate a percentile, you first need to arrange the data in ascending order. Then, you can determine the position of a specific percentile using the following steps:

1. Sort the data in ascending order.
2. Calculate the rank of the percentile using the formula:
   Rank = (P / 100) * (N + 1)
   where P is the desired percentile (e.g., 50 for the median, 25 for the first quartile, 75 for the third quartile), and N is the total number of data points.
3. If the rank is a whole number, the value corresponding to that position in the sorted dataset is the desired percentile.
4. If the rank is not a whole number, round it up to the next whole number, and the percentile is the value at that position.

For example, to find the median (50th percentile) of the dataset [2, 4, 6, 8, 10], you would follow these steps:

1. Sort the data: [2, 4, 6, 8, 10]
2. Calculate the rank: Rank = (50 / 100) * (5 + 1) = 3
3. The rank is a whole number, so the value at the third position is the median, which is 6.

Percentiles provide insights into the distribution of data and help identify specific points of interest. For instance, the first quartile (25th percentile) represents the value below which 25% of the data falls, and the third quartile (75th percentile) represents the value below which 75% of the data falls. The minimum value corresponds to the 0th percentile, and the maximum value corresponds to the 100th percentile.

![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)
# Cumulative Distribution Function (CDF)

A cumulative distribution function (CDF) is a function that represents the cumulative probability of a random variable taking on a value less than or equal to a given value. It is often used in probability theory and statistics to describe the distribution of a random variable.

Mathematically, the CDF of a random variable X is defined as:

F(x) = P(X ≤ x)

where F(x) represents the cumulative probability that X takes on a value less than or equal to x. The CDF provides information about the probabilities associated with different values of X.

Properties of a cumulative distribution function include:

1. Monotonicity: The CDF is non-decreasing, meaning that as x increases, the cumulative probability also increases.

2. Right-Continuity: The CDF is right-continuous, meaning that the cumulative probability does not have any jumps or discontinuities.

From the CDF, we can calculate probabilities associated with specific intervals or events. For example, the probability that X lies within a particular range [a, b] can be computed as:

P(a ≤ X ≤ b) = F(b) - F(a)

Conversely, we can also obtain the probability of X being greater than a certain value by taking the complement of the CDF:

P(X > a) = 1 - F(a)

The CDF is closely related to the probability density function (PDF) of a random variable. In fact, the PDF can be derived from the CDF by taking the derivative. The relationship is given by:

f(x) = d/dx F(x)

where f(x) represents the PDF.

The CDF is a fundamental concept in probability and statistics, and it provides a way to analyze and understand the behavior of random variables and their distributions.

![green-divider](https://user-images.githubusercontent.com/7065401/52071924-c003ad80-2562-11e9-8297-1c6595f8a7ff.png)

# Modeling distributions
Common analytic distributions and uses them to model data from a variety of sources:

## Exponential distribution
The probability density function (PDF) of the exponential distribution is given by:

$f(x|\lambda) = \lambda \cdot e^{-\lambda x}$

Where:
- \( x \) is the random variable (usually representing time) for which we are calculating the probability density.
- $\lambda$ is the rate parameter of the exponential distribution.

The cumulative distribution function (CDF) for the exponential distribution is:

$F(x|\lambda) = 1 - e^{-\lambda x}$

These formulas describe the probability of an event occurring at a certain time \( x \) in the future, given a specific rate parameter $\lambda$that governs the rate of occurrence. The exponential distribution is commonly used in various fields, including reliability analysis, queuing theory, and survival analysis.

