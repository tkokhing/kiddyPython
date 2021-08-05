<center>
    <img src="https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Module%201/images/IDSNlogo.png" width="300" alt="cognitiveclass.ai logo"  />
</center>

# Introduction  Notebook

Estimated time needed: **10** minutes

## Objectives

After completing this lab you will be able to:

*   Acquire data in various ways
*   Obtain insights from data with Pandas library


<h2>Table of Contents</h2>

<div class="alert alert-block alert-info" style="margin-top: 20px">
<ol>
    <li><a href="#data_acquisition">Data Acquisition</a>
    <li><a href="#basic_insight">Basic Insight of Dataset</a></li>
</ol>

</div>
<hr>


<h1 id="data_acquisition">Data Acquisition</h1>
<p>
There are various formats for a dataset: .csv, .json, .xlsx  etc. The dataset can be stored in different places, on your local machine or sometimes online.<br>

In this section, you will learn how to load a dataset into our Jupyter Notebook.<br>

In our case, the Automobile Dataset is an online source, and it is in a CSV (comma separated value) format. Let's use this dataset as an example to practice data reading.

<ul>
    <li>Data source: <a href="https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDA0101ENSkillsNetwork20235326-2021-01-01" target="_blank">https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data</a></li>
    <li>Data type: csv</li>
</ul>
The Pandas Library is a useful tool that enables us to read various datasets into a dataframe; our Jupyter notebook platforms have a built-in <b>Pandas Library</b> so that all we need to do is import Pandas without installing.
</p>



```python
# import pandas library
import pandas as pd
import numpy as np
```

<h2>Read Data</h2>
<p>
We use <code>pandas.read_csv()</code> function to read the csv file. In the brackets, we put the file path along with a quotation mark so that pandas will read the file into a dataframe from that address. The file path can be either an URL or your local file address.<br>

Because the data does not include headers, we can add an argument <code>headers = None</code> inside the <code>read_csv()</code> method so that pandas will not automatically set the first row as a header.<br>

You can also assign the dataset to any variable you create.

</p>


This dataset was hosted on IBM Cloud object. Click <a href="https://cocl.us/DA101EN_object_storage?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDA0101ENSkillsNetwork20235326-2021-01-01">HERE</a> for free storage.



```python
# Import pandas library
import pandas as pd

# Read the online file by the URL provides above, and assign it to variable "df"
other_path = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"
df = pd.read_csv(other_path, header=None)
```

After reading the dataset, we can use the <code>dataframe.head(n)</code> method to check the top n rows of the dataframe, where n is an integer. Contrary to <code>dataframe.head(n)</code>, <code>dataframe.tail(n)</code> will show you the bottom n rows of the dataframe.



```python
# show the first 5 rows using dataframe.head() method
print("The first 5 rows of the dataframe") 
df.head(5)
```

<div class="alert alert-danger alertdanger" style="margin-top: 20px">
<h1> Question #1: </h1>
<b>Check the bottom 10 rows of data frame "df".</b>
</div>



```python
# Write your code below and press Shift+Enter to execute 
df.tail(10)
```

<details><summary>Click here for the solution</summary>

```python
print("The last 10 rows of the dataframe\n")
df.tail(10)
```


<h3>Add Headers</h3>
<p>
Take a look at our dataset. Pandas automatically set the header with an integer starting from 0.
</p>
<p>
To better describe our data, we can introduce a header. This information is available at:  <a href="https://archive.ics.uci.edu/ml/datasets/Automobile?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDA0101ENSkillsNetwork20235326-2021-01-01" target="_blank">https://archive.ics.uci.edu/ml/datasets/Automobile</a>.
</p>
<p>
Thus, we have to add headers manually.
</p>
<p>
First, we create a list "headers" that include all column names in order.
Then, we use <code>dataframe.columns = headers</code> to replace the headers with the list we created.
</p>



```python
# create headers list
headers = ["symboling","normalized-losses","make","fuel-type","aspiration", "num-of-doors","body-style",
         "drive-wheels","engine-location","wheel-base", "length","width","height","curb-weight","engine-type",
         "num-of-cylinders", "engine-size","fuel-system","bore","stroke","compression-ratio","horsepower",
         "peak-rpm","city-mpg","highway-mpg","price"]
print("headers\n", headers)
```

We replace headers and recheck our dataframe:



```python
df.columns = headers
df.head(10)
```

We need to replace the "?" symbol with NaN so the dropna() can remove the missing values:



```python
df1=df.replace('?',np.NaN)

```

We can drop missing values along the column "price" as follows:



```python
df=df1.dropna(subset=["price"], axis=0)
df.head(20)
```

Now, we have successfully read the raw dataset and added the correct headers into the dataframe.


 <div class="alert alert-danger alertdanger" style="margin-top: 20px">
<h1> Question #2: </h1>
<b>Find the name of the columns of the dataframe.</b>
</div>



```python
# Write your code below and press Shift+Enter to execute 
print(df.info())
```

<details><summary>Click here for the solution</summary>

```python
print(df.columns)
```

</details>


<h2>Save Dataset</h2>
<p>
Correspondingly, Pandas enables us to save the dataset to csv. By using the <code>dataframe.to_csv()</code> method, you can add the file path and name along with quotation marks in the brackets.
</p>
<p>
For example, if you would save the dataframe <b>df</b> as <b>automobile.csv</b> to your local machine, you may use the syntax below, where <code>index = False</code> means the row names will not be written.
</p>

df.to_csv("automobile.csv", index=False)
We can also read and save other file formats. We can use similar functions like **`pd.read_csv()`** and **`df.to_csv()`** for other data formats. The functions are listed in the following table:


<h2>Read/Save Other Data Formats</h2>

| Data Formate |        Read       |            Save |
| ------------ | :---------------: | --------------: |
| csv          |  `pd.read_csv()`  |   `df.to_csv()` |
| json         |  `pd.read_json()` |  `df.to_json()` |
| excel        | `pd.read_excel()` | `df.to_excel()` |
| hdf          |  `pd.read_hdf()`  |   `df.to_hdf()` |
| sql          |  `pd.read_sql()`  |   `df.to_sql()` |
| ...          |        ...        |             ... |


<h1 id="basic_insight">Basic Insight of Dataset</h1>
<p>
After reading data into Pandas dataframe, it is time for us to explore the dataset.<br>

There are several ways to obtain essential insights of the data to help us better understand our dataset.

</p>


<h2>Data Types</h2>
<p>
Data has a variety of types.<br>

The main types stored in Pandas dataframes are <b>object</b>, <b>float</b>, <b>int</b>, <b>bool</b> and <b>datetime64</b>. In order to better learn about each attribute, it is always good for us to know the data type of each column. In Pandas:

</p>



```python
df.dtypes

```

A series with the data type of each column is returned.



```python
# check the data type of data frame "df" by .dtypes
print(df.dtypes)
```

<p>
As shown above, it is clear to see that the data type of "symboling" and "curb-weight" are <code>int64</code>, "normalized-losses" is <code>object</code>, and "wheel-base" is <code>float64</code>, etc.
</p>
<p>
These data types can be changed; we will learn how to accomplish this in a later module.
</p>


<h2>Describe</h2>
If we would like to get a statistical summary of each column e.g. count, column mean value, column standard deviation, etc., we use the describe method:

dataframe.describe()
This method will provide various summary statistics, excluding <code>NaN</code> (Not a Number) values.



```python
df.describe()
```

<p>
This shows the statistical summary of all numeric-typed (int, float) columns.<br>

For example, the attribute "symboling" has 205 counts, the mean value of this column is 0.83, the standard deviation is 1.25, the minimum value is -2, 25th percentile is 0, 50th percentile is 1, 75th percentile is 2, and the maximum value is 3. <br>

However, what if we would also like to check all the columns including those that are of type object? <br><br>

You can add an argument <code>include = "all"</code> inside the bracket. Let's try it again.

</p>



```python
# describe all the columns in "df" 
df.describe(include = "all")
```

<p>
Now it provides the statistical summary of all the columns, including object-typed attributes.<br>

We can now see how many unique values there, which one is the top value and the frequency of top value in the object-typed columns.<br>

Some values in the table above show as "NaN". This is because those numbers are not available regarding a particular column type.<br>

</p>


<div class="alert alert-danger alertdanger" style="margin-top: 20px">
<h1> Question #3: </h1>

<p>
You can select the columns of a dataframe by indicating the name of each column. For example, you can select the three columns as follows:
</p>
<p>
    <code>dataframe[[' column 1 ','column 2', 'column 3']]</code>
</p>
<p>
Where "column" is the name of the column, you can apply the method  ".describe()" to get the statistics of those columns as follows:
</p>
<p>
    <code>dataframe[[' column 1 ','column 2', 'column 3'] ].describe()</code>
</p>

Apply the  method to ".describe()" to the columns 'length' and 'compression-ratio'.

</div>



```python
# Write your code below and press Shift+Enter to execute 
df[['length','compression-ratio']].describe()
```

<details><summary>Click here for the solution</summary>

```python
df[['length', 'compression-ratio']].describe()
```

</details>


<h2>Info</h2>
Another method you can use to check your dataset is:

dataframe.info()
It provides a concise summary of your DataFrame.

This method prints information about a DataFrame including the index dtype and columns, non-null values and memory usage.



```python
# look at the info of "df"
df.info()
```

<h1>Excellent! You have just completed the  Introduction Notebook!</h1>


### Thank you for completing this lab!

## Author

<a href="https://www.linkedin.com/in/joseph-s-50398b136/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDA0101ENSkillsNetwork20235326-2021-01-01" target="_blank">Joseph Santarcangelo</a>

### Other Contributors

<a href="https://www.linkedin.com/in/mahdi-noorian-58219234/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDA0101ENSkillsNetwork20235326-2021-01-01" target="_blank">Mahdi Noorian PhD</a>

Bahare Talayian

Eric Xiao

Steven Dong

Parizad

Hima Vasudevan

<a href="https://www.linkedin.com/in/fiorellawever/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDA0101ENSkillsNetwork20235326-2021-01-01" target="_blank">Fiorella Wenver</a>

<a href="https://www.linkedin.com/in/yi-leng-yao-84451275/?utm_medium=Exinfluencer&utm_source=Exinfluencer&utm_content=000026UJ&utm_term=10006555&utm_id=NA-SkillsNetwork-Channel-SkillsNetworkCoursesIBMDeveloperSkillsNetworkDA0101ENSkillsNetwork20235326-2021-01-01" target="_blank" >Yi Yao</a>.

## Change Log

| Date (YYYY-MM-DD) | Version | Changed By | Change Description                       |
| ----------------- | ------- | ---------- | ---------------------------------------- |
| 2020-10-30        | 2.3     | Lakshmi    | Changed URL of the csv                   |
| 2020-09-22        | 2.2     | Nayef      | Added replace() method to remove '?'     |
| 2020-09-09        | 2.1     | Lakshmi    | Made changes in info method of dataframe |
| 2020-08-27        | 2.0     | Lavanya    | Moved lab to course repo in GitLab       |

<hr>

## <h3 align="center"> © IBM Corporation 2020. All rights reserved. <h3/>

