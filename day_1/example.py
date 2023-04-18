'''This is a docstring'''


x = "austin"
print(x[0::2]) # this is how you slice a string, [start:stop:step]
print(x[0::-2]) # you can also slice backwards

y = 2
y = str(y) # this is how you cast a variable

print(type(y)) # this is how you check the type of a variable


lists = [] # mut -> can be changed
tuples = () # not-mut, can't be changed, faster than lists

l = [1, 2, 3, ("hello")]
t = (4, 6, 7, "goodbye")

# how to change a value in a list
l[0] = 2
# how to change a value in a tuple
t = list(t)
t[0] = 2
t = tuple(t)

# Sets are unordered, unindexed
sets = {1, 2, 3, 4, 4 ,2 ,1}


# Dictionaries are key value pairs, keys are unique, values can be duplicated
d = {"key":"value",}

# some important methods for dictionaries
d.keys() # returns a list of keys
d.values() # returns a list of values
d.items() # returns a list of tuples
d.get("key") # returns the value of the key
d.pop("key") # removes the key and value

# defining a function
def function_1():
    """This is a function Docstring"""
    print("Hello World!") # this is the action of the function


asdf = [1, 2, 3, 4]


# for loop syntax
for i in range(len(asdf)):
    print(i)

# while loop syntax
x = 0
while x < 10:
    print(x)
    x += 1


# function for use in other functions
def myfunc(n):
    if n < 18:
        return False
    else:
        return True

age = [5, 17, 18]

# You can use a for loop to filter out values
output =[]
for i in range(len(age)):
    if myfunc(age[i]) == True:
        output.append(age[i])

# Alternatively you can use a filter function and pass in the function and the list
f = filter(myfunc, age)


# Lambda functions are anonymous functions, they are used to create quick functions
lam = lambda x: x*x

m = list(map(lam, age))
print(m)

# you can zip together lists to create a list of tuples
names = ["austin", "tyler", "brandon"]
z = list(zip(age, names))
print(z)

# List Comprehensions
x = [i for i in range(0, 15) if i % 2 == 0]

# Dictionary Comprehensions
y = { i:j for i, j in list(zip(names, age))}
print(y)


# Gernerators
def countdown():
    i = 5
    while i > 0:
        yield i  # yield is used to return a value and then continue where it left off
        i -= 1

y = countdown() # Here we are creating a generator object, it is not a list. A generator object is an iterable that can only be iterated over once.
print(next(y))
print(next(y)) # next is used to iterate over the generator object
print(next(y))


x = (i for i in range(5)) # this is a generator expression, like a list comprehension but it creates a generator object.

for i in range(5):
    print(next(x))


# Working with files

f = open("file.txt", "w") # this is how you open a file
f.write("Hello World!")
f.close() # You must close the file after you are done with it

# Instead of using the close method, we can use the context manager to open the file and close it for us.
# The with statement is used to wrap the execution of a block with methods defined by the context manager, in this case the open method.
with open("file2.txt", "w") as f2: 
    f2.write("Hello Again!")


# Decorators

'''Decorators are functions that take in another function as an argument and then add some functionality to it and then return another function.
Decorators are used to add functionality to existing functions without having to change the original function.'''
def my_decorator(func): # this is a decorator function. It takes in a function as an argument and returns a function.
    def wrap_func():
        print("**********")
        func()              
        print("**********")
    return wrap_func

# We then call the decorator function and pass in the function we want to decorate by using the @ symbol
# and then defining the function we want to decorate.
@my_decorator 
def hello():
    print("hello")
