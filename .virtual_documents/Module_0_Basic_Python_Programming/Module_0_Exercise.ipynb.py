# Place your imports here

import numpy as np



def exercise_1(n):
    # your code here.
    return [i for i in range(n)]
    #raise NotImplementedError


# these are test scripts
ans = exercise_1(5)
assert ans==[0, 1, 2, 3, 4]

ans = exercise_1(25)
assert ans==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]


def exercise_2(nums):
    # your code here.
    return np.array(nums)
    #raise NotImplementedError


ans = exercise_2([0, 1, 2, 3, 4])
assert (ans==np.arange(5)).sum()==5

ans = exercise_2(exercise_1(5))
assert (ans==np.arange(5)).sum()==5

ans = exercise_2(exercise_1(25))
assert (ans==np.arange(25)).sum()==25


def exercise_3(nums, n):
    # your code here.
    return [i+n for i in nums]
    #raise NotImplementedError


ans = exercise_3([0, 1, 2, 3, 4], 20)
assert (ans==np.arange(20, 25)).sum()==5

ans = exercise_3([0, 1, 2], 60)
assert (ans==np.arange(60, 63)).sum()==3


def exercise_4(nums):
    # your code here.
    return i for i in nums if i < i 
    #raise NotImplementedError


ans = exercise_4([0.79, 4, 11.8, 99])
assert ans==None

ans = exercise_4([0.79, 4, 11.8, 99, 0.4, 76, 55, 66])
assert ans==0.4

ans = exercise_4([0.79, 4, 4, 11.0, 11, -10, -11, 12])
assert ans==-10


def exercise_5(n):
    # your code here.
    raise NotImplementedError


ans = exercise_5(1)
assert ans==[]

ans = exercise_5(4)
assert ans==[2]

ans = exercise_5(1265)
assert ans==[5, 11, 23]

ans = exercise_5(3674)
assert ans==[2, 11, 167]


def exercise_6(nums, n1, n2):
    # your code here.
    raise NotImplementedError


ans = exercise_6(np.arange(20), 3, 4)
assert ans==[3, 6, 9, 12, 15, 18]

ans = exercise_6(np.arange(300), 17, 27)
assert ans==[17, 34, 51, 68, 85, 102, 119, 136, 153, 170, 187, 204, 221, 238, 255, 272, 289]


def exercise_7():
    # your code here.
    raise NotImplementedError


assert exercise_7()==[38, 26, 35, 27, 14]


def exercise_8():
    # your code here.
    raise NotImplementedError


assert exercise_8()==71.16
