print("Hello" + "world")

#this is a comment
'''this
is
a 
comment'''

n = 4
x = True
z = "hello"
b = 'hello'
# we use a comma for concantentation rather than a +
print('x =', x)
'''in python, the space after the string is added automatically
we can get rid of it by doing the following:'''
print('x =', x, sep = '')

x = 4+4
print(x)

#python does division like a calculator rather than int division like Java
x = 3/4
print('x =', x)

#we can do int division like Java by doing the following:
x = 3//4
print('x =', x)

#in order to do exponents, just use the coefficient value, then ** followed by the exponent value
x = 2**3
print('x =', x)

#mod is exactly the same as Java
x = 4 % 2
print('x =', x)

#casting works as follows:
x = 3.5
x = int(3.5)
print('x =', x)

#finding maximums
x = max(3, 4)
print('x =', x)

#finding mins
x = min(3,4)
print('x =', x)

#UI
'''
print('Enter a number: ', end = '')
x = input()
print('You entered: ', x)
#or you can do:
x = input('Enter a number: ')
print('You entered', x)
'''
#strings
x = 'input'
print(len(x))
print('Length =', len(x))

#substring
print('Substring 1:', x[2: ])
print('Substring 1:', x[1:3])
print("Substring 3:", x[-3:])
print('Substring 4:', x[-3:-1])

#contains
print('Contains', ('p' in x))
print('Contains:', ('pu' in x))

#lists (mutible, can be changed)
list = []
list.append('house')
list.append('mouse')
list.append('blouse')

print(list)
print("Length:", len(list))
print('Index 1:', list[1])
'''
list.insert(1, 'grouse')
print(list)
del(list[1])
print(list)
del(list[1:2])
print(list)
'''
list2 = []
list2.append('house')
list2.append('mouse')
list2.append('blouse')

list.extend(list2)
print(list)

list3 = list + list2
print(list3)

list4 = []
list4.append(list)
list4.append(list2)
print(list4)
print(list4[1][2])
list4[0] = 4
print(list4)

#touple, (immutible), cannot be changed
x = 2, 3, 4, 5
print(x)
y = x, 5, 'hello'
print(y)
print(y[0])
print(y[1:3])

x = 5,
print(x)

x = 5, 3, 3, 4
print(len(x))
print(3 in x)
print(7 in x)

#comparison operators
# python has == (like Java) and "is"
x = 4
y = 5

print(x == y)

y = 4
print(x == y)

'''x = input()
y = 'house'

#this one checks if the characters in the strings are identical, hence, if we input 'house' it returns true
print (x == y)
#this one checks if the values are the same object, so if we input 'house' it returns false, even though the strings are the same
print(x is y)'''

#operators 

print(4 < 5)
print(4 != 5)
print(not (4 < 5))

#logical operators
print(4 < 5 and 6 < 7)
print(4 < 5 or 6 > 7)

#control statements
if 4 > 5:
    print('1')
elif 4 > 3:
    print('3')
else :
    print('2')

#loops
x = 0
while x < 5:
    print(x, end = ' ')
    x+=1

#gives us 0-4
for x in range(5):
    print(x, end = ' ')

#gives us 2-9
for x in range (2, 10):
    print(x, end = ' ')

#gives us 2-9 by increments of 3
for x in range (2, 10, 3):
    print(x, end = ' ')

print('\n')
list = [1, 2, 3, 4]
for x in list:
    print(x, end = ' ')

print('\n')
for x in list:
    if x ==3:
        break
    print(x, end = ' ')

print('\n')
for x in list:
    if x == 3:
        continue
    print(x, end = ' ')

print('\n')
for x in range(5):
    if x == 6:
        break
else:
    print('entered else')

#functions
def sum(a, b, c):
    return a + b + c

print(sum(1, 2, 3))

mystery = sum
print(mystery(1, 2, 3))
#python supports optional parameters
def sum2(a, b, c = 0):
    return a + b + c

print(sum2(3, 4))

#class structure and objects
class Dog:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def get_age(self):
        return self._age
    def get_name(self):
        return self._name
    
    def set_name(self):
        self._name = name

    def set_age(self, age):
        self._age = age

    def random():
        return 7

    def __str__(self):
        return 'Dog:\nName: ' + self._name + '\nAge: ' + str(self._age)

d1 = Dog('Scruffy', 5)
print(d1)
print(d1.get_age())
print(Dog.random())