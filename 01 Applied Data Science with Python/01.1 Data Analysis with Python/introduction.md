# Introduction  

This is reference from cognitiveclass.ai 

## Objectives

Capture some of my thoughts, discovery and lesson learnt after going through [Data Analysis with Python](https://courses.cognitiveclass.ai/courses/course-v1:CognitiveClass+DA0101EN+2017/course/):

## Ask the Right Question

To learn how to analyze data in Python, we need to ask the right question focusing on 'estimate' and 'predict' on what data source is currently available. E.g. 

*   Can we estimate the price of a used car based past transactions? and what is the prediction of tomorrow's weather based on Y-O-Y trend?

*   But questioning does not end here. Data does not mean information unless you go deeper (many angle to attack!) to decipher the information and insights from raw data
    *   Is there data on the prices of other cars and their characteristics?
    *   What features of cars affect their prices? Colour? Brand? Does horsepower also affect the selling price, or perhaps, something else?

To answer these questions, we will use various Python packages to (i) perform data cleaning, (ii) exploratory data analysis, (iii) model development and (iv) model evaluation.

## Three Main Packages in Python

Cognitiveclass.ai groups them into three categories

*   Scientific Computing Libraries
    *	Python – primarily a two-dimensional table consisting of column and row labels, which are called a DataFrame.
    *	NumPy - uses arrays for its inputs and outputs. It can be extended to objects for matrices, and with minor coding changes, developers can perform fast array processing.
    *	SciPy  - integrals, solving differential equations, optimization as well as data visualization.
*	Visualization Libraries
    *	Matplotlib - making graphs and plots, highly customizable.
    *	Seaborn - based on Matplotlib - very easy to generate various plots such as heat maps, time series, and violin plots.
*	Algorithmic Libraries – for machine learning
    *	Scikit-learn - statistical modeling, including regression, classification, clustering …
    *	StatsModels - explore data, estimate statistical models, and perform statistical tests.

*   Note that there are various formats for a dataset: .csv, .json, .xlsx  etc, stored either on local machine or online. 

| Data Formate |        Read       |            Save |
| ------------ | :---------------: | --------------: |
| csv          |  `pd.read_csv()`  |   `df.to_csv()` |
| json         |  `pd.read_json()` |  `df.to_json()` |
| excel        | `pd.read_excel()` | `df.to_excel()` |
| hdf          |  `pd.read_hdf()`  |   `df.to_hdf()` |
| sql          |  `pd.read_sql()`  |   `df.to_sql()` |
| ...          |        ...        |             ... |

## My recordings for the exercise 

*	Data source: https://archive.ics.uci.edu/ml/machine-learning-databases/autos/ 
*	[File](https://github.com/tkokhing/kiddyPython/blob/main/01%20Applied%20Data%20Science%20with%20Python/01.1%20Data%20Analysis%20with%20Python/myPandainout.py) is attached. 
