import numpy as np
import pandas as pd


s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s)


print(type(s))
print(s.name)  


s['a']


s = pd.Series([8,7,6,5], name='test_data')
print('Name: ',s.name)
print('Data:\n',s)
print('Type of Object: ',type(s))
print('Type of elements:',type(s.values))


libs_dict = {'Library1': 'Numpy', 
               'Library2': 'Pandas', 
               'Library3': 'Matplotlib'}
s = pd.Series(libs_dict)
print(s)
print(type(s))


s['Library2']


libs_dict = {'Library1': 'Numpy', 'Library2': 'Pandas', 'Library3': 'Matplotlib'}
s = pd.Series(libs_dict)
print(s)

s['Library2'] = 'Pandas 2.0'
s['Library4'] = 'GeoPandas'
print(s)

s.pop('Library4')
print(s)


data = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
    'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(data)
print('Dataframe:\n',df)
print('Type of Object:',type(df))
print('Type of elements:',type(df.values))


print('Index: ',df.index)
print('Columns: ',df.columns)
print('Values of Column one: ',df['one'].values)
print('Values of Column two: ',df['two'].values)


df2 = pd.DataFrame([{'a': 1, 'b': 2, 'c':3, 'd':None}, 
                    {'a': 2, 'b': 2, 'c': 3, 'd': 4}],
                   index=['one', 'two'])
print('Dataframe: \n',df2)

# Ofcourse you can also transpose the result:
print('Transposed Dataframe: \n',df2.T)


df = pd.DataFrame(data)

df['three'] = None
print('Added third column: \n',df)

# The del keyword can be used delete columns:
del df['three']
print('\nDeleted third column: \n',df)
# You can also use df.drop(). We shall see that later

df.loc['a','one'] = 9000
print('\nEdited a value: \n',df)


data = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
    'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(data)
df


# Reindex in descending order.
df.reindex(['d','c','b','a'])


df.reindex(['a','b','c','d','e'])


df.reindex(['a','b','c','d','e'], fill_value=0)
# Guess why the df['one']['d'] was not filled with 0 ?


data = {'one' : pd.Series([1., 2., 3.], index=['a', 'b', 'c']),
    'two' : pd.Series([1., 2., 3., 4.], index=['a', 'b', 'c', 'd'])}
df = pd.DataFrame(data)
df


df.drop(['c', 'a'])


print("Dataframe: \n",df)
# Slicing and selecting only column `one` for row 0 and row 4
df['one'][['a', 'd']]


# Slicing df from row b to row 4 for column `one`
df['one']['b':'d']


df.loc[['a','c'],['one']]


df.loc[df.one > 1]


dt = pd.Series(np.random.randint(3, 10, size=7), 
               index=['g','c','a','b','e','d','f'])
print('Original Data: \n', dt, end="\n\n")
print('Sorted by Index: \n',dt.sort_index())


df1 = pd.DataFrame(np.random.randn(10, 4), columns=['A', 'B', 'C', 'D'])
df2 = pd.DataFrame(np.random.randn(7, 3), columns=['A', 'B', 'C'])

print('df1:')
display(df1)
print('df2:')
display(df2)
print('Sum:')
display(df1.add(df2))


df1.add(df2, fill_value=0)


print("Dataframe:")
display(df1)
print("Operand (0th row):")
display(df1.loc[0])
print('Subtraction:')
display(df1.sub(df1.loc[0]))


ind1 = pd.date_range('06/1/2017', periods=10)
df1.set_index(ind1)


np.abs(df1)


# Convert to numpy array
np.asarray(df1)


def fn(x):
    """
    Get max and min of the columns
    """
    return pd.Series([x.min(), x.max()], index=['min', 'max'])

df1.apply(fn)


fmt = lambda x: "{:.3f}".format(x)
df1.applymap(fmt)


df = pd.read_csv('data/train.csv')
df.head()


df.shape


df.dtypes


df.isnull().sum()


df['Age'].head()


df['Age'].mean()


df['Sex'].value_counts()


df_survived = df[df.Survived==1]
df_survived.head()


df_survived['Age'].mean()


df_survived['Sex'].value_counts()



