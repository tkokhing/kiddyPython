import pandas as pd
headers = ['symboling', 'normalized-losses','make','fuel-type','aspiration','num-of-doors',\
    'body-style','drive-wheels','engine-location', 'wheel-base','length','width', 'height', \
        'curb-weight', 'engine-type',  'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', \
            'stroke', 'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg', 'highway-mpg','price']
sourcepath = 'https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data'

#df = pd.read_csv(sourcepath, header = None)

# Below add headers. The auto data source is not having header. It is in another file
df = pd.read_csv(sourcepath)
df.columns=headers

"""
print('Reading the first 5 rows')
print(df.head())
# not giving any number to head() which by default will returns 5 rows  

print('Reading the last 5 rows')
print(df.tail())
# not giving any number to tail() which by default will returns 5 rows

"""

# remember to HAVE bracket the describe. Without bracket, it will still produce some results 
# but it is not statistics analysis (or describe) the df. 
# By default, df.describe() function skips rows and columns that do not contain numbers hence show analysis of 10 col only
# # By using df.describe(include='all'), it analysed all 26 col. 
# So those non-statistical col like Object Type will be analsed in the form of which word (model of car)
#  appeared the most as e.g. 
# Rememeber to have quotes for all. 
# This code does exist ==> (df.describe(include=all) ==> do not get confuze!

print('Analyse all  the columns including non-statisticall inside the df')
print(df.describe(include='all'))

"""

Analyse all  the columns including non-statisticall inside the df
         symboling normalized-losses    make fuel-type aspiration num-of-doors  ... compression-ratio horsepower peak-rpm    city-mpg  highway-mpg  price
count   204.000000               204     204       204        204          204  ...        204.000000        204      204  204.000000   204.000000    204
unique         NaN                52      22         2          2            3  ...               NaN         60       24         NaN          NaN    186
top            NaN                 ?  toyota       gas        std         four  ...               NaN         68     5500         NaN          NaN      ?
freq           NaN                40      32       184        167          114  ...               NaN         19       37         NaN          NaN      4
mean      0.823529               NaN     NaN       NaN        NaN          NaN  ...         10.148137        NaN      NaN   25.240196    30.769608    NaN
std       1.239035               NaN     NaN       NaN        NaN          NaN  ...          3.981000        NaN      NaN    6.551513     6.898337    NaN
min      -2.000000               NaN     NaN       NaN        NaN          NaN  ...          7.000000        NaN      NaN   13.000000    16.000000    NaN
25%       0.000000               NaN     NaN       NaN        NaN          NaN  ...          8.575000        NaN      NaN   19.000000    25.000000    NaN
50%       1.000000               NaN     NaN       NaN        NaN          NaN  ...          9.000000        NaN      NaN   24.000000    30.000000    NaN
75%       2.000000               NaN     NaN       NaN        NaN          NaN  ...          9.400000        NaN      NaN   30.000000    34.500000    NaN
max       3.000000               NaN     NaN       NaN        NaN          NaN  ...         23.000000        NaN      NaN   49.000000    54.000000    NaN
"""


print('Describe the two selected columns length and compression-ratio please')
print(df[['length','compression-ratio']].describe())
"""
Describe the two selected columns length and compression-ratio please

           length  compression-ratio    
count  204.000000         204.000000    
mean   174.075000          10.148137    
std     12.362123           3.981000    
min    141.100000           7.000000    
25%    166.300000           8.575000    
50%    173.200000           9.000000    
75%    183.200000           9.400000    
max    208.100000          23.000000   

"""



print('\n')
print('Describe the selected columns num-of-doors and body-style please')
print(df[['num-of-doors','body-style']].describe())
print('\n')

'''
Describe the selected columns num-of-doors and body-style please
       num-of-doors body-style
count           204        204
unique            3          5
top            four      sedan
freq            114         96

# # num-of-doors unique is 3 is because two, four and ?  inside the data source. 
# Need to clean up later exercise

'''

print('\n')
print('Mix - Describe the two selected statistical columns length and compression-ratio and\
     two non-statistical column Object-type num-of-doors and body-style please')
print(df[['num-of-doors','length','compression-ratio','body-style']].describe())
print('\n')


'''
#   INTERESTING Finding! 
# Non-statistical cannot mixed with statistical column to display. 
# But can display together using == > include = 'all'

Mix - Describe the two selected statistical columns length and compression-ratio and non-statistical column Object-type body-style please
           length  compression-ratio
count  204.000000         204.000000
mean   174.075000          10.148137
std     12.362123           3.981000
min    141.100000           7.000000
25%    166.300000           8.575000
50%    173.200000           9.000000
75%    183.200000           9.400000
max    208.100000          23.000000

'''

print('\n')
print('List column num-of-doors only!')
print(df[['num-of-doors']])
print('\n')

"""

List column num-of-doors only!
    num-of-doors
0            two
1            two
2           four
3           four
4            two
..           ...
199         four
200         four
201         four
202         four
203         four

"""

# After adding header, now write a new csv file to local. Which is done, so OFF it.
# not only path dir, also got to give the file a name
#outpath = 'D:/TKH/1_Project/1_1_Python/Pro2_DV/myAutoCar.csv'
#df.to_csv(outpath)

# dtypes does not have brackets because it is a property, not a METHOD like describe and info  
print('Showing data type of every col of the df')
print(df.dtypes)

"""
Showing data type of every col of the df
symboling              int64
normalized-losses     object
make                  object
fuel-type             object
until 26th col. .  .
"""


# df.info ==> shows more resolution of the df than dtypes 
print('Showing INFO of the df')
print(df.info())

'''
Showing INFO of the df
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 204 entries, 0 to 203
Data columns (total 26 columns):
 #   Column             Non-Null Count  Dtype  
---  ------             --------------  -----  
 0   symboling          204 non-null    int64  
 1   normalized-losses  204 non-null    object 
 2   make               204 non-null    object 
 until 26th col. .  .

'''
print('Showing COLUMN header of the df')
print(df.columns)

""" 
# interesting way to display of columns !


Showing COLUMN header of the df
Index(['symboling', 'normalized-losses', 'make', 'fuel-type', 'aspiration',
       'num-of-doors', 'body-style', 'drive-wheels', 'engine-location',
       'wheel-base', 'length', 'width', 'height', 'curb-weight', 'engine-type',
       'num-of-cylinders', 'engine-size', 'fuel-system', 'bore', 'stroke',
       'compression-ratio', 'horsepower', 'peak-rpm', 'city-mpg',
       'highway-mpg', 'price'],
      dtype='object')

"""



''' 
From filename: imports-85.names
https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.names 
1. Title: 1985 Auto Imports Database

2. Source Information:
   -- Creator/Donor: Jeffrey C. Schlimmer (Jeffrey.Schlimmer@a.gp.cs.cmu.edu)
   -- Date: 19 May 1987
   -- Sources:
     1) 1985 Model Import Car and Truck Specifications, 1985 Ward's
        Automotive Yearbook.
     2) Personal Auto Manuals, Insurance Services Office, 160 Water
        Street, New York, NY 10038 
     3) Insurance Collision Report, Insurance Institute for Highway
        Safety, Watergate 600, Washington, DC 20037

3. Past Usage:
   -- Kibler,~D., Aha,~D.~W., \& Albert,~M. (1989).  Instance-based prediction
      of real-valued attributes.  {\it Computational Intelligence}, {\it 5},
      51--57.
	 -- Predicted price of car using all numeric and Boolean attributes
	 -- Method: an instance-based learning (IBL) algorithm derived from a
	    localized k-nearest neighbor algorithm.  Compared with a
	    linear regression prediction...so all instances
	    with missing attribute values were discarded.  This resulted with
	    a training set of 159 instances, which was also used as a test
	    set (minus the actual instance during testing).
	 -- Results: Percent Average Deviation Error of Prediction from Actual
	    -- 11.84% for the IBL algorithm
	    -- 14.12% for the resulting linear regression equation

4. Relevant Information:
   -- Description
      This data set consists of three types of entities: (a) the
      specification of an auto in terms of various characteristics, (b)
      its assigned insurance risk rating, (c) its normalized losses in use
      as compared to other cars.  The second rating corresponds to the
      degree to which the auto is more risky than its price indicates.
      Cars are initially assigned a risk factor symbol associated with its
      price.   Then, if it is more risky (or less), this symbol is
      adjusted by moving it up (or down) the scale.  Actuarians call this
      process "symboling".  A value of +3 indicates that the auto is
      risky, -3 that it is probably pretty safe.

      The third factor is the relative average loss payment per insured
      vehicle year.  This value is normalized for all autos within a
      particular size classification (two-door small, station wagons,
      sports/speciality, etc...), and represents the average loss per car
      per year.

   -- Note: Several of the attributes in the database could be used as a
            "class" attribute.

5. Number of Instances: 205

6. Number of Attributes: 26 total
   -- 15 continuous
   -- 1 integer
   -- 10 nominal

7. Attribute Information:     
     Attribute:                Attribute Range:
     ------------------        -----------------------------------------------
  1. symboling:                -3, -2, -1, 0, 1, 2, 3.
  2. normalized-losses:        continuous from 65 to 256.
  3. make:                     alfa-romero, audi, bmw, chevrolet, dodge, honda,
                               isuzu, jaguar, mazda, mercedes-benz, mercury,
                               mitsubishi, nissan, peugot, plymouth, porsche,
                               renault, saab, subaru, toyota, volkswagen, volvo
  4. fuel-type:                diesel, gas.
  5. aspiration:               std, turbo.
  6. num-of-doors:             four, two.
  7. body-style:               hardtop, wagon, sedan, hatchback, convertible.
  8. drive-wheels:             4wd, fwd, rwd.
  9. engine-location:          front, rear.
 10. wheel-base:               continuous from 86.6 120.9.
 11. length:                   continuous from 141.1 to 208.1.
 12. width:                    continuous from 60.3 to 72.3.
 13. height:                   continuous from 47.8 to 59.8.
 14. curb-weight:              continuous from 1488 to 4066.
 15. engine-type:              dohc, dohcv, l, ohc, ohcf, ohcv, rotor.
 16. num-of-cylinders:         eight, five, four, six, three, twelve, two.
 17. engine-size:              continuous from 61 to 326.
 18. fuel-system:              1bbl, 2bbl, 4bbl, idi, mfi, mpfi, spdi, spfi.
 19. bore:                     continuous from 2.54 to 3.94.
 20. stroke:                   continuous from 2.07 to 4.17.
 21. compression-ratio:        continuous from 7 to 23.
 22. horsepower:               continuous from 48 to 288.
 23. peak-rpm:                 continuous from 4150 to 6600.
 24. city-mpg:                 continuous from 13 to 49.
 25. highway-mpg:              continuous from 16 to 54.
 26. price:                    continuous from 5118 to 45400.

8. Missing Attribute Values: (denoted by "?")
   Attribute #:   Number of instances missing a value:
   2.             41
   6.             2
   19.            4
   20.            4
   22.            2
   23.            2
   26.            4






'''