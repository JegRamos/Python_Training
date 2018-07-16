# def name_of_function() : 

def print_hello_world() :
    print("Hello World!")

print_hello_world()

# happy birthday
def sing_happy_birthday(name) :
    print("Happy Birthday to You") 
    print("Happy Birthday to You")
    print(f"Happy Birthday Dear {name}")
    print("Happy Birthday to You")

sing_happy_birthday("Jeg")

# returning a value
def calc_num_chars(word) :
    return len(word) 

num_chars = calc_num_chars("Jego")
print(num_chars)

def add_num(num1, num2) :
    return num1 + num2

added_numbers = add_num(10, 56)
print(added_numbers)

# setting a default parameter value
def get_exponent(num, power = 2) : 
    return num ** power

print(get_exponent(4))
print(get_exponent(2, 6))
print(get_exponent(10))

# passing functions to other functions
def add(num1, num2) : 
    return num1 + num2

def subtract(num1, num2) : 
    return num1 - num2

def math(num1, num2, fn=add) : 
    return fn(num1, num2)

print(math(2, 2))
print(math(2, 2, subtract))