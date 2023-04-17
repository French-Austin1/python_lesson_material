<style> .markdown-body { font-size: 1em; } .markdown-body h1 { color: #409f42; } .markdown-body h2 { color: #409f42; } .markdown-body h3 { text-decoration: underline; } .markdown-body p { color: #909090 } </style>

# Python day 2

## Functional vs. Object Oriented Programming

Functional programming is a programming paradigm that treats computation as the evaluation of mathematical functions and avoids changing-state and mutable data. It is a declarative programming paradigm in that programming is done with expressions or declarations instead of statements. In functional programming, functions are first-class objects, which means that functions can be assigned to variables, passed as arguments to other functions, returned as the values from other functions, and can be included in data structures.

Object-oriented programming (OOP) is a programming paradigm based on the concept of "objects", which can contain data, in the form of fields, often known as attributes; and code, in the form of procedures, often known as methods. A feature of objects is that an object's procedures can access and often modify the data fields of the object with which they are associated (objects have a notion of "this" or "self"). In OOP, computer programs are designed by making them out of objects that interact with one another. There is significant diversity of OOP languages, but the most popular ones are class-based, meaning that objects are instances of classes, which also determine their types.

## Functional Programming

Some of the most common functional programming concepts are:

- Functions as first-class objects. This means that functions can be assigned to variables, passed as arguments to other functions, returned as the values from other functions, and can be included in data structures.
- Pure functions. A pure function is a function that has no side effects and always returns the same result given the same arguments.
- Immutability. Immutability is the concept that data should not be changed after it is created. This is a key concept in functional programming because it allows for the creation of pure functions.
- Higher-order functions. A higher-order function is a function that takes a function as an argument or returns a function as a result.
- Recursion. Recursion is the process of defining something in terms of itself. In functional programming, this is often used to define functions in terms of other functions.

Here are some examples of functional programming in Python:

```python
# Functions as first-class objects
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

# Higher-order functions
def math(a, b, fn):
    return fn(a, b)

print(math(2, 2, add)) # 4
print(math(2, 2, subtract)) # 0

# Pure functions
def pure_function(x, y):
    temp = x + 2*y
    return temp / (2*x + y)

# Immutability
x = 4
y = 5
x = 3
print(x) # 3
print(y) # 5

# Recursion
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print(factorial(5)) # 120
```

## Object Oriented Programming

Some of the most common object-oriented programming concepts are:

- Encapsulation. Encapsulation is the concept that data should be kept private within a class, and can only be accessed through public methods.
- Abstraction. Abstraction is the concept that complex details should be hidden from the user, and only high-level concepts should be presented.
- Inheritance. Inheritance is the concept that classes can inherit fields and methods from parent classes.
- Polymorphism. Polymorphism is the concept that methods can be overridden in child classes.

Here are some examples of object-oriented programming in Python:

```python
# Encapsulation
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name # Encapsulated: only accessible through getter

    def get_age(self):
        return self.age

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

# Abstraction
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self): 
        print(self.sound)

# here we are hiding the implementation details of the make_sound method
class Dog(Animal):  
    def __init__(self, name): 
        super().__init__(name, 'woof') 

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, 'meow')

dog = Dog('Rover')
cat = Cat('Fluffy')

dog.make_sound() # woof
cat.make_sound() # meow

# Inheritance
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self): # Inherited
        print(self.sound)

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, 'woof') # Call parent constructor and inherit fields


class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, 'meow')
        
dog = Dog('Rover')
cat = Cat('Fluffy')

dog.make_sound() # woof
cat.make_sound() # meow

# Polymorphism
class Animal:
    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(self.sound)

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, 'woof') # Call parent constructor

    def make_sound(self): # Override
        print('bark')

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, 'meow')

dog = Dog('Rover')
cat = Cat('Fluffy')

dog.make_sound() # bark
cat.make_sound() # meow
```

## Modules and Packages

A module is a file containing Python definitions and statements. The file name is the module name with the suffix .py appended. Within a module, the module’s name (as a string) is available as the value of the global variable __name__.

A package is a collection of modules. A package must contain a special file called __init__.py, which can be empty. This file indicates that the directory it contains is a Python package, so it can be imported the same way a module can be imported.

## Python Standard Library

The Python Standard Library is a set of modules that comes with Python. It is available to all Python programs. The Python Standard Library is divided into several sections:

- Built-in Functions
- Built-in Constants
- Built-in Types
- Built-in Exceptions
- Built-in Modules

we already know the built-in functions, so let's take a look at the most used built-ins in other sections.

## Built-in Constants

The built-in constants are:

- True
- False
- None

## Built-in Types

The built-in types are:

- Numeric Types
- Sequence Types
- Mapping Types
- Set Types
- Boolean Type
- Binary Sequence Types
- Text Sequence Type
- Context Manager Type

## Built-in Exceptions

Some of the most common built-in exceptions are:

- Exception
- ArithmeticError
- AssertionError
- AttributeError
- EOFError
- ImportError
- IndexError
- KeyError

## Built-in Modules

Some of the most common built-in modules are:

| Module | Description |
| :--- | :--- |
| os | Provides a portable way of using operating system dependent functionality. |
| sys | Provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter. |
| re | Provides regular expression matching operations similar to those found in Perl. |
| math | Provides access to the mathematical functions defined by the C standard. |
| random | Implements pseudo-random number generators for various distributions. |
| datetime | Supplies classes for manipulating dates and times. |
| json | Implements a JSON encoder and decoder. |
| csv | Implements classes to read and write tabular data in CSV format. |
| urllib | Provides a high-level interface for fetching data across the World Wide Web. |
| smtplib | Implements an SMTP client session object that can be used to send mail to any Internet machine with an SMTP or ESMTP listener daemon. |
| socket | Provides access to the BSD socket interface. |
| multiprocessing | Supports spawning processes using an API similar to the threading module. |
| numpy | Provides a high-performance multidimensional array object, and tools for working with these arrays. |

## PIP

PIP is a package manager for Python packages, or modules if you like. PIP is used to install and manage software packages written in Python. PIP comes with Python 3.4+.

### requirements.txt

A requirements.txt file is a file that contains a list of items to be installed using PIP. It is used to specify what packages need to be installed for a particular project to run correctly.

## Virtual Environments

A virtual environment is a tool that helps to keep dependencies required by different projects separate by creating isolated Python virtual environments for them. It solves the “Project X depends on version 1.x but, Project Y needs 4.x” dilemma, and keeps your global site-packages directory clean and manageable.

You can create a virtual environment using the venv module included with Python 3.3+.

```bash
$ python3 -m venv name_of_virtual_environment
```

## Python Interpreter

The Python interpreter is a program that reads Python code and executes it. The Python interpreter is usually installed as /usr/bin/python3.6 on Linux systems and as C:\Python36\python.exe on Windows systems. Python is both an interpreted language and a compiled language. When you run a Python program, the Python interpreter reads the source code and converts it into bytecode. The bytecode is then executed by the Python virtual machine.

## Writing Tests

Writing tests is a good practice to ensure that your code is working as expected. There are many testing frameworks for Python, but we are going to focus on pytest.

We will also use the pytest-cov plugin to generate a coverage report.

```bash
$ pip install pytest pytest-cov
```

### Unit Testing vs Functional Testing vs Integration Testing

Unit testing is a level of software testing where individual units or components of a software are tested. The purpose is to validate that each unit of the software performs as designed. A unit is the smallest testable part of any software. It usually has one or a few inputs and usually a single output.

Functional testing is a level of software testing where the complete, integrated software is tested. The purpose is to evaluate the compliance of a system or its components with specified functional requirements.

Integration testing is a level of software testing where individual software modules are combined and tested as a group. The purpose is to expose faults in the interaction between integrated modules.

### Test Driven Development

Test-driven development (TDD) is a software development process that relies on the repetition of a very short development cycle: requirements are turned into very specific test cases, then the software is improved to pass the new tests, only. This is opposed to software development that allows software to be added that is not proven to meet requirements.

### Pytest Basics

Pytest is a testing framework that makes it easy to write small tests, yet scales to support complex functional testing for applications and libraries.

```python
# test_example.py
def test_example():
    assert 1 == 1
```

```bash
$ pytest
```

What are we doing here? We are importing the pytest module and defining a function that starts with test_. The function will be executed by pytest. The assert statement is used to check if the expression is true. If the expression is false, an AssertionError exception is raised.

### Fixtures

Fixtures are functions that are called before each test function to prepare the test environment. Fixtures are used to inject dependencies into test functions, and they are used to set up and tear down test data.

```python
# test_example.py
import pytest

@pytest.fixture
def example_fixture():
    return 1

def test_example(example_fixture):
    assert example_fixture == 1
```

```bash
$ pytest
```

### Parametrizing Tests

Parametrizing tests is a way to run the same test with different arguments. It is useful when you want to test the same functionality with different inputs.

```python
# test_example.py
import pytest

@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    ("2+4", 6),
    ("6*9", 42),
])


def test_parameterized(test_input, expected):
    assert eval(test_input) == expected
```

```bash
$ pytest
```

### Coverage

Coverage is a tool for measuring code coverage of Python programs. It monitors your program, noting which parts of the code have been executed, then analyzes the source to identify code that could have been executed but was not.

```bash
$ pytest --cov=.
```

How to read the coverage report?

- Name: The name of the file.
- Stmts: The total number of statements.
- Miss: The number of statements that were not executed.
- Cover: The percentage of statements that were executed.

### Mocking

Mocking is a way to replace a dependency with a fake implementation. It is useful when you want to isolate the code you are testing from other dependencies.

```python
# test_example.py
import pytest
from unittest.mock import Mock

@pytest.fixture
def example_fixture():
    return 1

def test_example(example_fixture, mocker):
    mocker.patch('requests.get', return_value=Mock(status_code=200))
    assert example_fixture == 1
```

```bash
$ pytest
```

What did we do here? We are using the mocker fixture to patch the requests.get function. This means that when the requests.get function is called, it will return a Mock object with a status\_code attribute set to 200. We are also using the return\_value parameter to set the return value of the function.

## pylint

pylint is a Python source code analyzer. It looks for programming errors, helps enforcing a coding standard, sniffs for code smells and offers simple refactoring suggestions.

```bash
$ pip install pylint
```

```bash
$ pylint example.py
```

### Configuration

pylint can be configured using a configuration file. The configuration file is a Python module, which means you can execute arbitrary Python code in it. The configuration file is named .pylintrc and it is located in the current directory.

```python
# .pylintrc
[MASTER]
load-plugins=pylint.extensions.docparams
```

### Plugins

pylint can be extended using plugins. Plugins are Python modules that define new checkers, which are classes that implement the visit\_\* methods. The visit\_\* methods are called when pylint visits a node in the abstract syntax tree (AST).

```python
# pylint_example.py
"""Example module for pylint."""

def example_function():
    """Example function for pylint."""
    return 1
```

```python
# pylint_example_plugin.py
"""Example plugin for pylint."""

import astroid
from pylint.checkers import BaseChecker
from pylint.interfaces import IAstroidChecker

class ExampleChecker(BaseChecker):
    """Example checker for pylint."""

    __implements__ = IAstroidChecker

    name = 'example'
    msgs = {
        'E9999': (
            'Example message',
            'example',
            'Example message description',
        ),
    }

    def visit_functiondef(self, node):
        """Called when a function definition is found."""
        if node.name == 'example_function':
            self.add_message('E9999', node=node)

def register(linter):
    """Register the checker."""
    linter.register_checker(ExampleChecker(linter))
```

```bash
$ pylint --load-plugins=pylint_example_plugin pylint_example.py
```

What did we do here? We are defining a new checker that checks if a function is named example_function. If the function is named example_function, we are adding a message to the function node. The message is then displayed by pylint when the function is found.

### Disabling Checks

pylint can be configured to disable checks using the disable parameter.

```python
# pylint_example.py
"""Example module for pylint."""

def example_function():
    """Example function for pylint."""
    return 1
```

```bash
$ pylint --disable=missing-docstring pylint_example.py
```

What did we do here? We are disabling the missing-docstring check. This means that pylint will not check if the module, class or function has a docstring.

### pep8 style guide

pep8 is a style guide for Python code. It is a set of recommendations about how to write Python code that is more readable and consistent.




