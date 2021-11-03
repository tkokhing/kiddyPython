import pandas as pd

df=pd.DataFrame({'a':[11,12,13,14],'b':[21,22,23,24],'c':[31,32,33,34],'d':[41,42,43,44],'e':[51,52,53,54],'f':[61,62,63,64]})


print('Experimenting df, df.head and df.iloc with single and double Sq and curve brackets\n')
print('Output of Output of Output of dataFrame df [\'a\'] will NOT display column header but with some details')
print(df['a'])

#     0    11
#     1    12
#     2    13
#     3    14
#     Name: a, dtype: int64


print('Output of query (True of False) on  whether dataFrame df [\'a\'] contents 11')
print(df['a']==11)
#     0     True
#     1    False
#     2    False
#     3    False
#     Name: a, dtype: bool

rowWith11 = df['a']==11
print('Row With 11, returns Boolean')
print(rowWith11)
#    returns the same as above
#     0     True
#     1    False
#     2    False
#     3    False
#     Name: a, dtype: bool

rowWith31 = df[df['a']==11]
print('Row With 11, with 2 sets of df. It filters by Col a and display whole row containing 11')
print(rowWith31)
#         a   b   c   d   e   f
#     0  11  21  31  41  51  61

rowWith31 = df[df['a']==31]
print('Row With 11, with 2 sets of df. It filters by Col a and display whole row containing 31 which is FALSE')
print(rowWith31)
# There is no 31 in Col a, hence as below
#     Empty DataFrame
#     Columns: [a, b, c, d, e, f]
#     Index: []

lessThan13 = df[df['a']<13]
print('Row With less than 13, with 2 sets of df. It filters by Col a and display whole row less than 13')
print(lessThan13,'\n')
print(df[df['a']<13])
print('\nAfter filtering to lessThan13, this dataFrame can be saved using, lessThan13.to_csv("myFile.csv")\n') 
#         a   b   c   d   e   f
#     0  11  21  31  41  51  61
#     1  12  22  32  42  52  62
#
#         a   b   c   d   e   f
#     0  11  21  31  41  51  61
#     1  12  22  32  42  52  62

print('df [[\'a\']] with Sq br x 2, which shows header')
print(df[['a']])

#         a
#     0  11
#     1  12
#     2  13
#     3  14


# Experiment df[] with other formats, below are incorrect

#print(df[['a'],3])
#print(df[['a'],'3'])
#print(df[['a'],['3']])
#print(df[['a'],[3]])

print('Output of df.head withOUT brackets, output is\
     is weird and comes with details enclosed in <>')
print(df.head)
#     <bound method NDFrame.head of     a   b   c   d   e   f
#     0  11  21  31  41  51  61
#     1  12  22  32  42  52  62
#     2  13  23  33  43  53  63
#     3  14  24  34  44  54  64>

print('Output of df.head() with brackets, output is everything in the DF incl header')
print(df.head())
#         a   b   c   d   e   f
#     0  11  21  31  41  51  61
#     1  12  22  32  42  52  62
#     2  13  23  33  43  53  63
#     3  14  24  34  44  54  64

print('Output of df.head Single bracket (2), showing\
     first two rows as specify by the 2 (2 is not serving as a index). ')
print(df.head(2))

#         a   b   c   d   e   f
#     0  11  21  31  41  51  61
#     1  12  22  32  42  52  62

print('Output of df.head Double Bracket((2)), which output is the SAME as single bracket.')
print(df.head((2)))
#         a   b   c   d   e   f
#     0  11  21  31  41  51  61
#     1  12  22  32  42  52  62

print('\n','df.head does not work with Sq bracket','\n')
print('\n','Yes! Output of df.head Single Sq bracket [\'a\']] ) will give ERROR')

# Below 2 lines give error
# print(df.head['a'])
# print(df.head[])

# Testing other common mistakes 
# The 2 lines below give error. .head() does not 
# print(df.head(0,2))
# print(df.head((0,2)))

# there is no more ix() method in 3.9.5, so here comes iloc()
# explore how different (or same) these methods are based on lesson notes of ix. And 
# compared with .head method

print('\nExperiment - df.iloc [[row index],[column index]] --- see comma carefully\n')

print('df.iloc[[1]] -- DO NOT see this as Double Bracket feature. It is specifying only row index of 1')
print(df.iloc[[1]])
#         a   b   c   d   e   f
#     1  12  22  32  42  52  62

print('Output of df.iloc df.iloc[[1],:], with row index 1 cum with all columns BUT\
      is meaningless since is showing all of row 1')
print(df.iloc[[1],:])
#         a   b   c   d   e   f
#     1  12  22  32  42  52  62

print('Output of df.iloc[[0,2]], which means row specify 0 and 2')
print(df.iloc[[0,2]])
#         a   b   c   d   e   f
#     0  11  21  31  41  51  61
#     2  13  23  33  43  53  63

print('Output of df.iloc[[0,0]], with row index 0 twice')
print(df.iloc[[0,0]])
#         a   b   c   d   e   f
#     0  11  21  31  41  51  61
#     0  11  21  31  41  51  61

print('Output of df.iloc[[0,1,2]], with row index 0, 1 and 2')
print(df.iloc[[0,1,2]])
#         a   b   c   d   e   f
#     0  11  21  31  41  51  61
#     1  12  22  32  42  52  62
#     2  13  23  33  43  53  63

print('\nOutput of df.iloc[:,[0]], with column index only --- see carefully\n')
print(df.iloc[:,[0]])
#         a
#     0  11
#     1  12
#     2  13
#     3  14

print('Output of df.iloc Double Bracket[:,[2]], with column index only --- see carefully')
print(df.iloc[:,[2]])
#         c
#     0  31
#     1  32
#     2  33
#     3  34

print('Output of df.iloc Double Bracket[[0],[1]], with row and column index --- see comma carefully')
print(df.iloc[[0],[1]])
#         b
#     0  21

# print('Single Bracket[0\,2]')
# print(df.iloc[0,2])
# The above output is error  

print('\nOutput of df.iloc Single Bracket[0,1], getting data at the specific location\n')
print(df.iloc[0,1])
#    21





'''


print('Just column a')
A_col = df.iloc[['a']]
print(A_col)

'''