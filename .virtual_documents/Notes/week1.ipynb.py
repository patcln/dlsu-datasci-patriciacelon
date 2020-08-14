print("Hello")


print("Hello")


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style = "darkgrid")


df = pd.read_csv('/Users/Tasha/Desktop/dlsu/Notes/fortune500.csv')


df.head()


df.tail()


df.columns = ['year', 'rank', 'company', 'revenue', 'profit']


len(df)


df.dtypes


non_numeric = df.profit.str.contains('[^0-9.-]')
df.loc[non_numeric].head()


def exercise_1(n):
    """this returns a list form 0 to n-1"""
    ex1 = [i for i in range(n)]
    return ex1
exercise_1(20)


import numpy as np
blah = [[1, 2], [3, 4]]

def exercise_2(nums):
    """this returns a list as a numpy array"""
    # your code here.
    return np.array(nums)
exercise_2([0, 1, 2, 3, 4])


def exercise_4(nums):
    # your code here.
    for i in nums:
        j = nums(i)
        k = nums(i+1)
        if j > k:
            print(k)
        else:
            none
    #raise NotImplementedError


exercise_4([0.79, 4, 11.8, 99, 0.4, 76, 55, 66])


def prime_factors(n):
    i = 2
    prime_factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            prime_factors.append(i)
    if n > 1:
        prime_factors.append(n)
    return sorted(list(set(prime_factors)))


prime_factors(1)


def prime(n):
    faclist = []
    


def exercise_6(nums, n1, n2):
    # your code here.
    multiple = []
    for j in range (1, -1):
        for num in nums:
            if num % n1 == 0:
                multiple.append(num)
    return multiple


exercise_6(np.arange(20), 3, 4)


import pandas as pd

df = pd.read_csv('/Users/Tasha/Desktop/dlsu/Module_0_Basic_Python_Programming/data/train.csv')


df.head()


df.dtypes


survived = df[(df.Survived == 1) & (df.Sex == 'female') & (df.Age > 30)]


survived.tail()


survived.Fare.mean().round(2)


def ex8():
    df = pd.read_csv('/Users/Tasha/Desktop/dlsu/Module_0_Basic_Python_Programming/data/train.csv')
    survived = df[(df.Survived == 1) & (df.Sex == 'female') & (df.Age > 30)]
    return survived.Fare.mean().round(2)


ex8()


type(ex8())


survived1['Age'][:5].values.tolist()


survived1 = df[(df.Survived == 1) & (df.Sex == 'female')]



