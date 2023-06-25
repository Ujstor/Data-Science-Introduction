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

# Dataset Summary Statistics

This repository contains summary statistics for a given dataset. The summary statistics provide an overview of the dataset and describe various characteristics of the data. The following summary statistics are included:

## Mean (Average)

The mean represents the average value of the dataset, indicating the central tendency.

Example:
Given a dataset [3, 4, 5, 6, 7], the mean is 5.


![Mean Formula](https://latex.codecogs.com/png.latex?\dpi{120}&space;\bg_white&space;\fn_phv&space;\large&space;\text{mean}&space;=&space;\frac{1}{n}\sum_{i=1}^{n}x_i)

## Median

The median represents the middle value in a sorted dataset, dividing it into two equal halves.

Example:
Given a dataset [3, 4, 5, 6, 7], the median is 5.

Formula:
If \(n\) is odd, the median is the value at position \(\frac{n+1}{2}\).
If \(n\) is even, the median is the average of the values at positions \(\frac{n}{2}\) and \(\frac{n}{2} + 1\).

## Mode

The mode represents the most frequently occurring value(s) in a dataset.

Example:
Given a dataset [3, 4, 5, 5, 6, 7], the mode is 5.

Formula:
No specific formula - it is the value(s) that occur with the highest frequency.

## Variance

The variance measures the spread or dispersion of a dataset around its mean.

Example:
Given a dataset [3, 4, 5, 6, 7], the variance is calculated as:

![Variance Formula](https://latex.codecogs.com/png.latex?\dpi{120}&space;\bg_white&space;\fn_phv&space;\large&space;\text{var}&space;=&space;\frac{1}{n}\sum_{i=1}^{n}(x_i-\text{mean})^2)

## Standard Deviation

The standard deviation is the square root of the variance, providing a measure of the dispersion around the mean.

Example:
Given a dataset [3, 4, 5, 6, 7], the standard deviation is calculated as:

![Standard Deviation Formula](https://latex.codecogs.com/png.latex?\dpi{120}&space;\bg_white&space;\fn_phv&space;\large&space;\text{std}&space;=&space;\sqrt{\text{var}})

## Range

The range represents the difference between the maximum and minimum values in a dataset.

Example:
Given a dataset [3, 4, 5, 6, 7], the range is 7 - 3 = 4.


![Range Formula](https://latex.codecogs.com/png.latex?\dpi{120}&space;\bg_white&space;\fn_phv&space;\large&space;\text{range}&space;=&space;\text{max}-\text{min})


## Effect Size: Cohen's d

Another way to convey the size of the effect is to compare the difference between groups to the variability within groups. Cohen’s d is a statistic intended to do that.

Cohen's d is defined as:

![Cohen's d Formula](https://latex.codecogs.com/png.latex?\dpi{120}&space;\bg_white&space;\fn_phv&space;\large&space;d&space;=&space;\frac{{x_1&space;-&space;x_2}}{{s}})

where \(x_1\) and \(x_2\) are the means of the groups, and \(s\) is the "pooled standard deviation".



These summary statistics provide valuable insights into the dataset and help understand its central tendency, dispersion, and shape.


