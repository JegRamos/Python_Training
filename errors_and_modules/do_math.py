def add(*args):
    result = 0
    for num in args:
        result += num
    return result

def subract(*args):
    result = 0
    for num in args:
        result -= num
    return result

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

def divide(*args):
    result = 0
    try:
        for num in args:
            result /= num
    except ZeroDivisionError:
        print("You cannot divide by 0")
    else:
        return result

def print_name():
    print(__name__)