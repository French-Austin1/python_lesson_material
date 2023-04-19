
def calc_factorial(n):
    if n == 1:
        return 1
    else:
        return n * calc_factorial(n-1)

def greet_user():
    print("Welcome to the factorial calculator!")

def get_user_input():
    user_input = input("Enter a number: ")
    return int(user_input)