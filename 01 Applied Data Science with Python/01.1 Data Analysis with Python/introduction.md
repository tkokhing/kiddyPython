# Introduction  

This is reference from cognitiveclass.ai 

## Objectives

Capture some of my thoughts, discovery and lesson learnt after going through [Data Analysis with Python](https://courses.cognitiveclass.ai/courses/course-v1:CognitiveClass+DA0101EN+2017/course/):

Data source: https://archive.ics.uci.edu/ml/machine-learning-databases/autos/ 

*   Note that there are various formats for a dataset: .csv, .json, .xlsx  etc, stored either on local machine or online. 

| Data Formate |        Read       |            Save |
| ------------ | :---------------: | --------------: |
| csv          |  `pd.read_csv()`  |   `df.to_csv()` |
| json         |  `pd.read_json()` |  `df.to_json()` |
| excel        | `pd.read_excel()` | `df.to_excel()` |
| hdf          |  `pd.read_hdf()`  |   `df.to_hdf()` |
| sql          |  `pd.read_sql()`  |   `df.to_sql()` |
| ...          |        ...        |             ... |


To learn how to analyze data in Python, we'll be answering the following question: Can we estimate the price of a used car based on its characteristics?
*   To answer this question, we are going to (i) use various Python packages to perform data cleaning, (ii) exploratory data analysis, (iii) model development and (iv) model evaluation.
    *   Data does not mean information unless you decipher the information and insights from raw data
    *   For example, is there data on the prices of other cars and their characteristics?
    *   What features of cars affect their prices? Colour? Brand? Does horsepower also affect the selling price, or perhaps, something else?

## Main packages relevant to analysis in Python

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

## My recordings for the exercise 
'''

