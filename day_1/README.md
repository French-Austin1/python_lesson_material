
<style> .markdown-body { font-size: 1em; } .markdown-body h1 { color: #409f42; } .markdown-body h2 { color: #409f42; } .markdown-body h3 { text-decoration: underline; } .markdown-body p { color: #909090 } </style>
# Python Day 1

## What is Python?

Python is a high level programming language that is used for general purpose programming. It is a very popular language and is used in many different fields such as web development, data science, and machine learning.

## Why Python?

Many developers choose to use python because it is easy to learn and has a large community of developers. It is also a very versatile language and can be used for many different purposes. 

Other reasons to use python are:
- It is free and open source
- It is easy to read and understand
- It is easy to learn
- It has a vast ecosystem of libraries and frameworks

Some examples of uses for python are:
- Web Development
- Data Science
- Machine Learning
- Game Development
- Scripting

## How to use Python

Python can be used in many different ways. It can be used in the command line, in a text editor, or in an IDE.

We will be using the command line to run our python code. To run python code in the command line you can use the `python` command.

```bash
python my_file.py
```

## Python Syntax

Python is a very simple language and has a very simple syntax. It is very similar to english and is easy to read and understand.
One of the main differences between python and other languages is that python uses indentation to define blocks of code. 

```python
if 5 > 2:
  print("Five is greater than two!")
```

## Python Comments

Comments are used to explain code. They are ignored by the python interpreter and are not executed.

```python
# This is a comment
print("Hello World")
```

## Python docstrings

Docstrings are used to explain code. They are ignored by the python interpreter and are not executed. They are used to explain what a function does and how to use it. They are surrounded by triple quotes.

```python
def my_function():
  """This is a docstring. It explains what the function does."""
  print("Hello World")
```

## Python Variables and Constants

Variables are used to store data in a program. They are used to store information that can be used later in the program.

```python
x = 5
y = "Hello World"
```

Constants are used to store data in a program. They are used to store information that cannot be changed later in the program.

```python
PI = 3.14
```

## Python Data Types

There are 5 main data types in python: strings, integers, floats, booleans, and lists. There are also some compound data types such as tuples, sets, and dictionaries.

### Strings

Strings are used to store text. They are surrounded by either single or double quotes.

```python
x = "Hello World"
y = 'Hello World'
```

### Integers

Integers are used to store whole numbers.

```python
x = 5
```

### Floats

Floats are used to store decimal numbers.

```python
x = 5.5
```

### Booleans

Booleans are used to store true or false values.

```python
x = True
y = False
```

### Lists

Lists are used to store multiple values in a single variable. They are surrounded by square brackets and the values are separated by commas.

```python
x = ["apple", "banana", "cherry"]
```

Lists can contain different data types and can be changed after they are created (mutable).

```python
x = ["apple", 1, ["cherry", "orange"]]
# this is how you would change the first value in the list
x[0] = "blackcurrant"
print(x)
```

### Tuples

Tuples are used to store multiple values in a single variable. They are surrounded by parentheses and the values are separated by commas.

```python
x = ("apple", "banana", "cherry")
```

Tuples can contain different data types but cannot be changed after they are created (immutable). You have to typecast it to a list to change it.

```python
x = ("apple", 1, ["cherry", "orange"])
# this is how you would change the first value in the list
x = list(x)
x[0] = "blackcurrant"
x = tuple(x)
print(x)
```

### Sets

Sets are used to store multiple values in a single variable. They are surrounded by curly brackets and the values are separated by commas.

```python
x = {"apple", "banana", "cherry"}
```

Sets can contain different data types and can be changed after they are created (mutable). What makes sets different from lists is that they cannot contain duplicate values.

```python
x = {"apple", "banana", "cherry", "apple"}
print(x)
# This returns {"apple", "banana", "cherry"}
```

### Dictionaries

Dictionaries are used to store data values in key:value pairs. They are surrounded by curly brackets and the values are separated by commas. Each key is separated from its value by a colon.

```python
x = {"name" : "John", "age" : 36}
```

Dictionaries can contain different data types and can be changed after they are created (mutable).

```python
x = {"name" : "John", "age" : 36}
# this is how you would change the age
x["age"] = 40
print(x)
```

Dictionaries cannot have duplicate keys.

```python
x = {"name" : "John", "age" : 36, "name" : "Bob"}
print(x)
# This returns {"name" : "Bob", "age" : 36}
```

## Python Operators

Operators are used to perform operations on variables and values.

### Arithmetic Operators

Arithmetic operators are used with numeric values to perform common mathematical operations.

| Operator | Name | Example |
|----------|------|---------|
| + | Addition | x + y |
| - | Subtraction | x - y |
| * | Multiplication | x * y |
| / | Division | x / y |
| % | Modulus | x % y |
| ** | Exponentiation | x ** y |
| // | Floor division | x // y |

### Assignment Operators

Assignment operators are used to assign values to variables.

| Operator | Example | Same As | Result |
|----------|---------|---------|--------|
| = | x = 5 | x = 5 | 5 |
| += | x += 3 | x = x + 3 | 8 |
| -= | x -= 3 | x = x - 3 | 2 |
| *= | x *= 3 | x = x * 3 | 15 |
| /= | x /= 3 | x = x / 3 | 1.6666666666666667 |
| %= | x %= 3 | x = x % 3 | 2 |
| //= | x //= 3 | x = x // 3 | 1 |
| **= | x **= 3 | x = x ** 3 | 125 |
| &= | x &= 3 | x = x & 3 | 1 |
| |= | x |= 3 | x = x | 3 |
| ^= | x ^= 3 | x = x ^ 3 | 0 |
| >>= | x >>= 3 | x = x >> 3 | 0 |
| <<= | x <<= 3 | x = x << 3 | 40 |

### Comparison Operators

Comparison operators are used to compare two values.

| Operator | Name | Example |
|----------|------|---------|
| == | Equal | x == y |
| != | Not equal | x != y |
| > | Greater than | x > y |
| < | Less than | x < y |
| >= | Greater than or equal to | x >= y |
| <= | Less than or equal to | x <= y |

### Logical Operators

Logical operators are used to combine conditional statements.

| Operator | Description | Example |
|----------|-------------|---------|
| and | Returns True if both statements are true | x < 5 and  x < 10 |
| or | Returns True if one of the statements is true | x < 5 or x < 4 |
| not | Reverse the result, returns False if the result is true | not(x < 5 and x < 10) |

### Identity Operators

Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.

| Operator | Description | Example |
|----------|-------------|---------|
| is | Returns True if both variables are the same object | x is y |
| is not | Returns True if both variables are not the same object | x is not y |

### Membership Operators

Membership operators are used to test if a sequence is presented in an object.

| Operator | Description | Example |
|----------|-------------|---------|
| in | Returns True if a sequence with the specified value is present in the object | x in y |
| not in | Returns True if a sequence with the specified value is not present in the object | x not in y |

### Bitwise Operators

Bitwise operators are used to compare (binary) numbers.

| Operator | Name | Description |
|----------|------|-------------|
| & | AND | Sets each bit to 1 if both bits are 1 |
| \| | OR | Sets each bit to 1 if one of two bits is 1 |
| ^ | XOR | Sets each bit to 1 if only one of two bits is 1 |
| ~ | NOT | Inverts all the bits |
| << | Zero fill left shift | Shift left by pushing zeros in from the right and let the leftmost bits fall off |
| >> | Signed right shift | Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off |

# Control Structures

Control structures are the way we tell the computer what to do and when to do it. There are 3 main control structures in python: if statements, loops, and functions.

## loops

A loop is a way to repeat a block of code a certain number of times.

You would use a for loop when you know how many times you want to repeat the code.

Example of a for loop:
```python
for i in range(5,=):
  print(i)

x = ['alice','bob','charlie']
for i in x:
  print(i)
```

Or you can use a while loop when you don't know how many times you want to repeat the code.

Example of a while loop:
while loop
```python
i = 0
while i < 5:
  print(i)
  i += 1
```

## if statements

An if statement is a way to tell the computer to do something if a condition is met.

```python
x = 5
if x > 5:
  print("x is greater than 5")
```
You can also use an if statement to tell the computer to do something if a condition is not met.
  
```python
x = 5
if x > 5:
  print("x is greater than 5")
else:
  print("x is less than or equal to 5")
```

There is also the elif statement which is used to tell the computer to do something if a condition is met and if the previous conditions were not met.

```python
x = 5
if x > 5:
  print("x is greater than 5")
elif x < 5:
  print("x is less than 5")
else:
  print("x is equal to 5")
```

## functions

A function is a way to group a block of code together so that it can be called multiple times without having to rewrite the code. 

Example of a function:

```python
def my_function():
  print("Hello World")

my_function()
```

Functions can also take in parameters and return a value.

```python
def my_function(x):
  return x + 5

print(my_function(5))
```
There are also anonymous functions which are functions that are not bound to a name. They are used when you want to pass a function as a parameter to another function.

```python
x = lambda a : a + 5
print(x(5))
```

## Exception Handling

Exception handling is a way to handle errors that may occur in your code. It is used to prevent your program from crashing when an error occurs.

```python
try:
  print(x)
except:
  print("An exception occurred")
```

you can return the error message by using the `as` keyword.

```python
try:
  print(x)
except Exception as e:
  print(e)
```

or catch a specific error.

```python
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
```

# Built-in Functions

Python has a set of built-in functions that you can use without having to import any modules.

| Function | Description |
|----------|-------------|
| abs() | Returns the absolute value of a number |
| all() | Returns True if all items in an iterable object are true |
| any() | Returns True if any item in an iterable object is true |
| ascii() | Returns a readable version of an object. Replaces none-ascii characters with escape character |
| bin() | Returns the binary version of a number |
| bool() | Returns the boolean value of the specified object |
| bytearray() | Returns an array of bytes |
| bytes() | Returns a bytes object |
| callable() | Returns True if the specified object is callable, otherwise False |
| chr() | Returns a character from the specified Unicode code. |
| classmethod() | Converts a method into a class method |
| compile() | Returns the specified source as an object, ready to be executed |
| complex() | Returns a complex number |
| delattr() | Deletes the specified attribute (property or method) from the specified object |
| dict() | Returns a dictionary (Array) |
| dir() | Tries to return a list of valid attributes for the given object |
| divmod() | Returns the quotient and the remainder when argument1 is divided by argument2 |
| enumerate() | Takes a collection (e.g. a tuple) and returns it as an enumerate object |
| eval() | Runs Python code within a program |
| exec() | Executes the specified code (or object) |
| filter() | Use a filter function to exclude items in an iterable object |
| float() | Returns a floating point number |
| format() | Formats a specified value |
| frozenset() | Returns a frozenset object |
| getattr() | Returns the value of the specified attribute (property or method) |
| globals() | Returns the current global symbol table as a dictionary |
| hasattr() | Returns True if the specified object has the specified attribute (property/method) |
| hash() | Returns the hash value of a specified object |
| help() | Executes the built-in help system |
| hex() | Converts a number into a hexadecimal value |
| id() | Returns the id of an object |
| input() | Allows user input |
| int() | Returns an integer number |
| isinstance() | Returns True if a specified object is an instance of a specified object |
| issubclass() | Returns True if a specified class is a subclass of a specified object |
| iter() | Returns an iterator object |
| len() | Returns the length of an object |
| list() | Returns a list |
| locals() | Returns an updated dictionary of the current local symbol table |
| map() | Returns the specified iterator with the specified function applied to each item |
| max() | Returns the largest item in an iterable |
| memoryview() | Returns a memory view object |
| min() | Returns the smallest item in an iterable |
| next() | Returns the next item in an iterable |
| object() | Returns a new object |
| oct() | Converts a number into an octal |
| open() | Opens a file and returns a file object |
| ord() | Converts an integer representing the Unicode of the specified character |
| pow() | Returns the value of x to the power of y |
| print() | Prints to the standard output device |
| property() | Gets, sets, deletes a property |
| range() | Returns a sequence of numbers, starting from 0 and increments by 1 (by default) and ends at a specified number |
| repr() | Returns a readable version of an object |
| reversed() | Reverses the order of the iterable |
| round() | Rounds a numbers |
| set() | Returns a new set object |
| setattr() | Sets an attribute (property/method) of an object |
| slice() | Returns a slice object |
| sorted() | Returns a sorted list |
| @staticmethod() | Converts a method into a static method |
| str() | Returns a string object |
| sum() | Sums the items of an iterator |
| super() | Returns an object that represents the parent class |
| tuple() | Returns a tuple |
| type() | Returns the type of an object |
| vars() | Returns the __dict__ property of an object |
| zip() | Returns an iterator, from two or more iterators |

## Important built-in function examples

### abs()

```python
x = abs(-7.25)
print(x)
# returns 7.25
```

### all()

```python
x = all([1, 2, 3, 4])
print(x)
# returns True
```

### min()

```python
x = min(5, 10, 25)
print(x)
# returns 5
```

### max()

```python
x = max(5, 10, 25)
print(x)
# returns 25
```

### sum()

```python
x = sum([1, 2, 3, 4])
print(x)
# returns 10
```

### len()

```python
x = len("Hello World")
print(x)
# returns 11
```

### filter()

```python
def myfunc(n):
  if n < 18:
    return False
  else:
    return True

age = [5, 17, 18, 21, 32, 45, 60]

x = filter(myfunc, age)
print(list(x))
# returns [18, 21, 32, 45, 60]
```

### map()

```python
def myfunc(n):
  return len(n)

x = map(myfunc, ('apple', 'banana', 'cherry'))
print(list(x))
# returns [5, 6, 6]
```

### zip()

```python
x = zip(('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(list(x))
# returns [('apple', 'orange'), ('banana', 'lemon'), ('cherry', 'pineapple')]
```

# List and Dictionary Comprehensions

Useing comprehensions is a way to create lists and dictionaries in a single line of code. This is a very powerful feature and can make your code more readable and concise.

## List Comprehensions

List comprehensions are used for creating new lists from other iterables. As list comprehensions return lists, they consist of brackets containing the expression, which is executed for each element along with the for loop to iterate over each element.

```python
# Example
# Without list comprehension
numbers = [1, 2, 3, 4]
new_list = []

for n in numbers:
  add_1 = n + 1
  new_list.append(add_1)

print(new_list)
# returns [2, 3, 4, 5]

# With list comprehension
numbers = [1, 2, 3, 4]
new_list = [n + 1 for n in numbers]

print(new_list)
# returns [2, 3, 4, 5]
```

## Dictionary Comprehensions

Dictionary comprehensions are used for creating new dictionaries from other iterables. As dictionary comprehensions return dictionaries, they consist of curly brackets containing the expression, which is executed for each element along with the for loop to iterate over each element.

```python
# Example
# Without dictionary comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {}

for name in names:
  student_scores[name] = random.randint(1, 100)

for (student, score) in student_scores.items():
  if score >= 60:
    passed_students[student] = score

print(passed_students)
# returns {'Beth': 75, 'Caroline': 100, 'Dave': 100, 'Eleanor': 100, 'Freddie': 100}

# With dictionary comprehension
names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
student_scores = {student: random.randint(1, 100) for student in names}

passed_students = {student: score for (student, score) in student_scores.items() if score >= 60}

print(passed_students)
# returns {'Beth': 75, 'Caroline': 100, 'Dave': 100, 'Eleanor': 100, 'Freddie': 100}
```

## Conditional List Comprehensions

Conditional list comprehensions just add an if statement to the end of the list comprehension. This allows you to filter the list based on a condition.

```python
# Example
# Without conditional list comprehension
numbers = [1, 2, 3, 4]
new_list = []

for n in numbers:
  if n % 2 == 0:
    new_list.append(n)

print(new_list)
# returns [2, 4]

# With conditional list comprehension
numbers = [1, 2, 3, 4]
new_list = [n for n in numbers if n % 2 == 0]

print(new_list)
# returns [2, 4]
```

# Generators

Generators are a special type of function that return a lazy iterator. This means that the items in the iterator are computed only when they are needed.

## Generator functions

Generator functions are functions that return a generator object. This is done by using the yield keyword instead of return. The yield keyword pauses the function and saves all its states and later continues from there on successive calls.

```python
# Example
def countdown():
  i = 5
  while i > 0:
    yield i
    i -= 1

x = countdown()
print(next(x))
# returns 5
print(next(x))
# returns 4
# or you can use a for loop
for i in countdown():
  print(i)
# returns 5 then 4 then 3 then 2 then 1
```

## Generator expressions

Generator expressions are generator objects that are created using generator comprehension syntax. This is done by using the same syntax as list comprehensions but with parentheses instead of square brackets.

```python
# Example
x = (i for i in range(5))
print(next(x))
# returns 0
print(next(x))
# returns 1
```

## context manager

Context managers are used to allocate and release resources precisely when you want to. This is done by using the with keyword. The with keyword allows you to get access to the resources you need, then it will automatically close the resources when you are done with them.

```python
# Example
with open("file.txt") as file:
  file.read()
```

The use of context managers is very common in Python. For example, when you open a file, it is opened in a context manager. This means that you don't have to worry about closing the file, because it will automatically be closed when you are done with it.

The with keyword is also used with database connections. This means that you don't have to worry about closing the database connection, because it will automatically be closed when you are done with it.

# Decorators

Decorators are functions that take other functions as arguments, add some functionality and then return another function. All this without altering the source code of the original function passed in.

```python
# Example
def decorator_function(original_function):
  def wrapper_function():
    print(f"wrapper executed this before {original_function.__name__}")
    return original_function()
  return wrapper_function

def display():
  print("display function ran")

decorated_display = decorator_function(display)
decorated_display()
# returns wrapper executed this before display
# returns display function ran
```

You can also use decorators in the form of @decorator_name. This is the same as doing display = decorator_function(display).

```python
# Example
def decorator_function(original_function):
  def wrapper_function():
    print(f"wrapper executed this before {original_function.__name__}")
    return original_function()
  return wrapper_function

@decorator_function
def display():
  print("display function ran")

display()
# returns wrapper executed this before display
# returns display function ran
```



