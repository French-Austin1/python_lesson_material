'''Some basic string examples'''

def string_reverse(string):
    '''Reverse a string'''
    return string[::-1]

def string_palindrome(string):
    '''Check if a string is a palindrome'''
    return string == string[::-1]

li_of_strings = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']

def enumerate_strings(li_of_strings):
    '''Enumerate a list of strings'''
    for index, string in enumerate(li_of_strings):
        return (index, string)
    
def string_concatenate(li_of_strings):
    '''Concatenate a list of strings'''
    return ''.join(li_of_strings)
    # return "" + li_of_strings[0] + li_of_strings[1] + li_of_strings[2] etc.


# different ways to format strings
def string_formatting():
    '''Different ways to format strings'''
    name = 'John'
    age = 30
    # old way
    # We don't use this because it is not type safe
    print('My name is %s and I am %d years old' % (name, age))
    # new way
    # This is type safe, but it is a little verbose
    print('My name is {} and I am {} years old'.format(name, age))
    # f-strings
    # This is type safe and concise but can lead to security issues if you are not careful.
    # Sql injection is a common problem with f-strings
    print(f'My name is {name} and I am {age} years old')

