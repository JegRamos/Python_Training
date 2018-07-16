# Rasing your own errors
#? Syntax: raise ValueError("Invalid value")

def colorize(text, color):
    if type(text) is not str:
        raise TypeError("You need to pass in a string")
    if color not in ("red", "blue", "purple", "yellow", "green"):
        raise ValueError("Invalid color, boi")
    print(f"{text} in color {color}")

colorize("sad life", "blue")

# Handling Errors- Try Catch
cities= ["tarlac", "manila", "pasay", "makati"]
try:
    cities[5]
except IndexError:
    print("Wrong index boi")

#? Enter a damn number!
while True:
    try:
        number = int(input("Enter a number: "))
    except ValueError:
        print("That's not a number!")
    else:
        break
print("Rest of logic!")

#? Handling division errors
def divide(num1, num2):
    try:
        quotient = num1 / num2
    except ZeroDivisionError as err:
        print("Cannot divide by zero!")
        print(f"Error Logs: {err}")
    except TypeError as err:
        print("Please only divide with ints or floats")
        print(f"Error Logs: {err}")
    else:
        print(f"{num1} divided by {num2} is {quotient}")

divide(2, "kk")

#? Debugging with pdb
import pdb; pdb.set_trace()

first_name = "Jeg"
last_name = "Ramos"
full_name = first_name + last_name
print(full_name)
