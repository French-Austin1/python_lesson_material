# Functional programming

# First-class: functions are objects that can be passed around and used as arguments
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def apply(fn, a, b):
    return fn(a, b)

# higher-order: functions that operate on other functions,
# either by taking them as arguments or by returning them,
# are called higher-order functions.

# Immutability: in functional programming, data is immutable, even if it is a list or a dictionary.

# Pure functions: a pure function is a function that, given the same input,
# will always return the same output and does not have any observable side effect.

def pure_function(x, y):
    temp = x + 2*y
    return temp / (2*x + y)

# Recursion: a function that calls itself is called a recursive function.

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

# Object Oriented Programming

# Inheritance: a class can inherit attributes and methods from another class.

# Encapsulation: the idea of wrapping data and the methods that work on data within one unit.

# Abstraction: the process of hiding the implementation details from the user,
# only the functionality will be provided to the user.

# Polymorphism: the word polymorphism means having many forms.
# In python, polymorphism allows us to define methods in the child class with the same name as defined in their parent class.

class Person:
    '''A class that represents a person'''
    # constructor: the __init__ method is called the constructor and is always called when an object is created.
    def __init__(self, name, age) -> None: 
        self.name = name
        self.age = age

    # methods
    def get_name(self): 
        return self.name

    def set_name(self, name):
        self.name = name

# Abstraction

class Animal:
    def __init__(self, name, sound) -> None:
        self.name = name
        self.sound = sound

    def make_sound(self):
        print(self.sound)

class Dog(Animal): # Inheritance: Dog inherits from Animal
    def __init__(self, name, sound) -> None:
        super().__init__(name, sound)

    # The method make_sound is callabale from the Dog class because it is inherited from the Animal class.

class Cat(Animal):  
    def __init__(self, name, sound) -> None:
        super().__init__(name, sound)

    # The method make_sound has been overridden in the Cat class.
    def make_sound(self):
        print("The cat says: {}".format(self.sound))



def main():
    # __name__ is a built-in variable which evaluates to the name of the current module.
    print("-"*10+"__name__"+"-"*10)
    print(__name__)

    # Here we can call all the functions and classes defined in this module.
    print("-"*10+"Classes"+"-"*10)
    dog = Dog("Fido", "Woof!")
    dog.make_sound()

    cat = Cat("Garfield", "Meow!")
    cat.make_sound()

    print("-"*10+"First-class"+"-"*10)
    print(apply(add, 2, 3))
    print(apply(sub, 2, 3))

    print("-"*10+"Recursion"+"-"*10)
    print(factorial(5))
    print("-"*10+"Pure function"+"-"*10)
    print(pure_function(1, 2))


# This if statement evaluates to True if the module is being run directly by the Python interpreter.
if __name__ == "__main__":
    main()


