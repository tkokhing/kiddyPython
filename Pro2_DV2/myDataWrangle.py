import pandas as pd
import numpy as np
import matplotlib.pylab as plt


headers = ['symboling', 'normalized-losses','make','fuel-type','aspiration','num-of-doors',\
    'body-style','drive-wheels','engine-location', 'wheel-base','length','width', 'height', \
        'curb-weight', 'engine-type',  'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', \
            'stroke', 'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg','price']

#sourcepath = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'

filepath = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/Data%20files/auto.csv"

#df = pd.read_csv(sourcepath, header = None)
# Below add headers. The auto data source is not having header. It is in another file. 
# This is the method thought in module 1 
# df = pd.read_csv(sourcepath)
# df.columns=headers

# This is another method (names = headers) thought in Module 2, this works the same as 
# having second line calling ==> df.columns=headers
# Tested both path having files of different extension (*.csv and *.data), the method (names = headers) 
# gives same result

df = pd.read_csv(filepath, names = headers)  
print('Reading the first 10 rows')
print(df.head(5))
print('\n')
"""
Reading the first 5 rows
   symboling normalized-losses         make fuel-type aspiration num-of-doors  ... compression-ratio horsepower peak-rpm  city-mpg  highway-mpg  price
0          3                 ?  alfa-romero       gas        std          two  ...               9.0        111     5000        21           27  13495
1          3                 ?  alfa-romero       gas        std          two  ...               9.0        111     5000        21           27  16500
2          1                 ?  alfa-romero       gas        std          two  ...               9.0        154     5000        19           26  16500
3          2               164         audi       gas        std         four  ...              10.0        102     5500        24           30  13950
4          2               164         audi       gas        std         four  ...               8.0        115     5500        18           22  17450

[5 rows x 26 columns]
"""

# numpy method .nan to replace "?" with NaN
df.replace("?", np.nan, inplace = True)
print('\n')
print(df.head(5))
print('\n')

'''
# NaN has reaplced all "?"

   symboling normalized-losses         make fuel-type aspiration  ... horsepower peak-rpm city-mpg highway-mpg  price
0          3               NaN  alfa-romero       gas        std  ...        111     5000       21          27  13495
1          3               NaN  alfa-romero       gas        std  ...        111     5000       21          27  16500
2          1               NaN  alfa-romero       gas        std  ...        154     5000       19          26  16500
3          2               164         audi       gas        std  ...        102     5500       24          30  13950
4          2               164         audi       gas        std  ...        115     5500       18          22  17450

[5 rows x 26 columns]
'''

missing_data = df.isnull()
# above method writes 'True' to fields that are NULL/NaN, while 'False' to all other fields
# print(type(missing_data))
# <class 'pandas.core.frame.DataFrame'>
# print(missing_data.head(10))

#missing_data.to_csv("missingDataList.csv")

i = 1
for column in df:
   print(i,')', column)
   print('\n')
   i += 1

# the above prints 
# 1 ) symboling
# 2 ) normalized-losses
# 3 ) make
# ...
# 26 ) price

