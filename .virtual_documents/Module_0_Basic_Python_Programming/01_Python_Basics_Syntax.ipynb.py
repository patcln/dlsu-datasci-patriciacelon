a = 12
if a == 12:
    print("a is 12 :) ")
else:
    print("a is not 12 :( ")


a = 12
if a == 12:
    print("a is 12 :) ") # this uses 4 spaces
    print("hey") # this uses a tab, this is possible but not recommended
else:
    print ("a is not 12 :( ")


a = 12
if a == 12:
    print("a is 12 :) ")
else:
print ("a is not 12 :( ")


a = 12
if a == 12:
    print("a is 12 :) ") # this uses 4 spaces
        print("hey") # this uses 2 tabs, indentation mismatch
else:
    print ("a is not 12 :( ")


a = "Hello 
World"
print(a)


a = "Hello \
World"
print(a)


num = ['one', 'two', 'three'
       'four', 'five']
num


name = 'DSI'
school = "De La Salle University"
text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, 
sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui 
officia deserunt mollit anim id est laborum.'''

print(name)
print(school)
print(text)


# I wont be evaluated
a = 12
a


x = 100  # Setting x to 100 (this is unnecessary)


def my_func():
    """
    This function will
    perform .....
    """
    pass


my_func?


my_func.__doc__


import sys

a = None
print(sys.getsizeof(a))
a = "heyy"
print(sys.getsizeof(a))
a = "hey"
print(sys.getsizeof(a))
a = "hi"
print(sys.getsizeof(a))
a = "0"
print(sys.getsizeof(a))


var = 'I am in DLSU'
print(var)


type(var)


var = 123
type(var)


x = y = z = a = 1
print(x,y,z,a)

x, y, z, a = 'Hello', 'World', 1, 2
print(x,y,z,a)


var = 'Hello World'
print("Contents of var: ", var)
print("Type of var: ", type(var))


print('''C:\name\of\dir''')  # even using triple quotes won't save you!


print(r'C:\name\of\dir')


var1 = 'Hello'  # String 1
var2 = 'World'  # String 2
var3 = var1 + var2  # Concatenate two string as String 3
print(var3)


var1 = 'Hello' 'World'
print(var1)


var1 = 'Hello'
var2 = 1
print(var1+var2)


var1 = 'Python'
len(var1)


var1[0]


var1[5]


var1[6]


var1[0] = 'J'


var1[-1]


var1[-6]


var1[0:2]


var1[0:5]


var1[0:6]


var1[0:7]


var1[:4]


var1[:-4]


var1[:2]+var1[-4:]


"I have {} dogs".format(2)


text = "I have {} dogs"
text.format(2)


text = "I have {} dogs"
num = 2
text.format(num)


"{} {:.2f} {:.3f} {:.2get_ipython().run_line_magic("}".format(1,", " 20, 3.14, 0.4)")


f"I have {2} dogs"


f"I have {2:.2f} dogs"


num = 2
f"I have {num:.2f} dogs"


f"{1} {20:.2f} {3.14:.3f} {0.4:.2get_ipython().run_line_magic("}"", "")


print("original string:", 'HELLO')
print("lower:", 'HELLO'.lower())

print('---')

print("original string:", var1.capitalize())
print("capitalize:", var1.capitalize())
print("center with length of 9 and # padding:", var1.center(9, '#'))
print("center with length of 10 and @ padding:", var1.center(9, '#'))
print("y count:", var1.count('y'))
print("endswith 'on'?", var1.endswith('on'))
print("endswith 'yes'?", var1.endswith('yes'))

print('---')

sequence = ('P','y','t','h','o','n')
print("join using blank space:", ' '.join(sequence))
print("join using --:", '--'.join(sequence))

var1_padded = "  Python     "
print('Before rstrip:', var1_padded)
print("After rstrip:", var1_padded.strip())

words = 'How are you?'
print('Original sentence:', words)
print('After split:', words.split(' '))


# this will crash on C
2 ** 120


int('20')


2.0


float(2)


2e4


c_val = complex(2, 3)
print(c_val)


print(c_val.real)
print(c_val.imag)
print(c_val.conjugate()) # complex conjugate of c_val


abs(c_val)


print(2 + 2)  # addition 
print(2 - 2)  # subtraction 
print(2 * 2)  # multiplication
print(2 / 2)  # division
print(5 % 3)  # modulus - remainder
print(3 ** 2)  # exponential
print(5 // 3)  # floor division - division without remainder


a, b = 10, 10

print(a==b)  # Equal to
print(aget_ipython().getoutput("=b)  # Not equal to")
print(a>b)  # Greater than
print(a<b)  # Less than
print(a>=b)  # Greater than or equal to
print(a<=b)  # Less than or equal to


a = 10


a += 10  # It is equivalent to a = a + 10
a -= 10  # It is equivalent to a = a - 10
a *= 10  # It is equivalent to a = a * 10
a /= 10  # It is equivalent to a = a / 10
a get_ipython().run_line_magic("=", " 10  # It is equivalent to a = a % 10")
a **= 10  # It is equivalent to a = a ** 10
a //= 10  # It is equivalent to a = a // 10


c, d = True, False
print(c and d)
print(c or d)
print(f'{c} to {not c}')


sequence


'P' in sequence


'0' not in sequence


c == d


c is d


c get_ipython().getoutput("= d")


c is not d


result = 1
if result == 1:
    print("Yayget_ipython().getoutput("")")
elif result <= 3:
    print("You're so closeget_ipython().getoutput("")")
else:
    print("Alas! You got it wrongget_ipython().getoutput("")")


for i in [0,1,2]:
    print(f"{i}")


i = 2
while i >= 0:
    print(f"{i}")
    i -= 1


range(8)


list(range(8))


list(range(5,8))


for i in range(3):
    print(f"{i}")


for i in range(1, 10):
    if i == 3:
        print('Condition satisfied')
        break
    print(i)  # What would happen if this is placed before if condition?


for i in range(1, 5):
    if i == 3:
        print('Condition satisfied')
        continue
        print("whatever.. I won't get printed anyways.")
    print(i)


for i in range(1, 5):
    if i == 3:
        print('Condition satisfied')
        pass
    print(i)


my_list = ['Jude', 'Sash', 'Unisse', 1, True, 3.0]
my_list


my_list[0]


my_list[1:4]


list1 = ['Jude', 'Sash', 'Unisse']
list2 = [1, True, 3.0]
my_list = list1+list2
my_list


my_list = ['Jude', 'Sash', 'Unisse', 1, True, 3.0]
my_list[0] = 'Teves'
my_list


my_list = ['Jude', 'Sash', 'Unisse', 1, True, 3.0]
my_list.append(None)
my_list


my_list = ['Jude', 'Sash', 'Unisse', 1, True, 3.0]
my_list.insert(1, 'Teves')
my_list


my_list = ['Jude', 'Sash', 'Unisse', 1, True, 3.0]
my_list.pop(0)
my_list


list1 = ['Jude', 'Sash', 'Unisse']
list2 = [1, True, 3.0]
my_list = [list1, list2]
my_list


my_list[0]


list1 = [1, 2, 3, 4]
list2 = [elem for elem in list1 if elem % 2 == 0]
print(list2)


list1 = [1, 2, 3, 4]
list2 = [elem+1 for elem in list1]
print(list2)


my_list = [1, 2, 3, 4]
print('Max:', max(my_list))  # should only contain numbers
print('Min:', min(my_list))  # should only contain numbers
print('Length:', len(my_list)) 


my_list = [1, 2, 3, 4]
my_list.reverse()  # after this, the list is reversed
print('Reverse:', my_list) 


my_list[::-1]


my_list


my_list = [3, 4, 2, 1]
my_list.sort()
my_list


my_list = ['Sash', 'Jude', 'Unisse']
my_list.sort()
my_list


my_list = [3, 4, 2, 1]
sorted(my_list)


my_tuple = ('Jude', 'Sash', 'Unisse', 1, True, 3.0)
my_tuple


my_set = [1, 1, 2, 4]
set(my_set)


my_set = {1, 1, 2, 4}
my_set


my_set.union([1, 5])


my_set.intersection([1, 5])


my_dict = {'key': 'value',
           'dsi': 100,
           'programming': 9000.00}

my_dict


my_dict = dict(key='value', dsi=100, programming=9000.00)
my_dict


my_dict['key']


my_dict.get('key')


my_dict.get('time')  # returns None


my_dict.keys()


my_dict.values()


my_dict = dict(key='value', dsi=100, programming=9000.00)
my_dict['time'] = '6PM'
my_dict


my_dict = dict(key='value', dsi=100, programming=9000.00)
my_dict.pop('key')


my_dict


dict1 = {'key': 1, 'time': '6 PM'}
dict2 = {'key': 4, 'num': '6 PM'}

dict1.update(dict2)
dict1


dict2


my_dict = dict(key='value', dsi=100, programming=9000.00)
my_dict.clear()
my_dict


def kg_to_lbs(kg):
    return kg*2.2

kg = 10
print(f'{kg} kg = {kg_to_lbs(kg)} lbs')
# some code
kg = 87
print(f'{kg} kg = {kg_to_lbs(kg)} lbs')


def something(num1, num2, num3):
    return (num1+num2)*num3

something(1,2,3)


something(num2=2, num3=3, num1=1)


something(2, 3, 1)  # this will have a different output
