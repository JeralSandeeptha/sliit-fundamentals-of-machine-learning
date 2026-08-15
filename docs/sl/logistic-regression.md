# Logistic Regression

To solve a classification problem

**Classificatioins** are 2 types

- Binary Classification
- Multi Class Classification

<br/>

Can't we solve classification problem using linear regression? `Yes` we can, but when if `X` axis data values getting larger data correctness becomes falsy / wrong / not accuracy. [Like Image]

![Image](../../images/logistic-r-01.png)

This is where we have low `X` axis value which is more truth. (But still not good because `X` axis can be larger value and it will not become good accuracy)
![Image](../../images/logistic-r-03.png)

But if we can get something like this, we can get better results

![Image](../../images/logistic-r-02.png)

<br/>

[View Logistic Regression Example](../../python/logistic-regression/Logistic_Regression.ipynb)

---

## Evaluate Classification Models / Confusion Matrix

`Confusion Matrix` is a table that evaluates a classification model's performance

<br>

## The Four Outcomes

**True Positive (TP)**: The model predicts positive, and the actual value is positive
**True Negative (TN)**: The model predicts negative, and the actual value is negative
**False Positive (FP)**: The model predicts positive, but the actual value is negative (Type I error)
**False Negative (FN)**: The model predicts negative, but the actual value is positive (Type II error)

<br/>

## Key Metrics Derived from the Matrix

**Accuracy**: (TP + TN) / (TP + TN + FP + FN) — Overall correct predictions
**Precision**: TP / (TP + FP) — Accuracy of positive predictions
**Recall (Sensitivity)**: TP / (TP + FN) — Ability to find all positive instances
**F1-Score**: Harmonic mean of precision and recall

<br>

![Image](../../images/confusion-matrix-01.png)

<br> 

![Image](../../images/confusion-matrix-02.png)

<br> 

![Image](../../images/confusion-matrix-03.png)
