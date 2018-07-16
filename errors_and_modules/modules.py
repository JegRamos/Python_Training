# pyfiglet package
from pyfiglet import figlet_format
from termcolor import colored

def print_art(user_text, user_color):
    available_colors = ("red", "green", "blue", "magenta", "cyan", "white")
    if user_color in available_colors:
        ascii_art = figlet_format(user_text)
        colored_ascii_art = colored(ascii_art, user_color)
        print(colored_ascii_art)
    else:
        print("Invalid Color!")
        print(f"Available colors are: {', '.join(available_colors).title()}")

user_text = input("Enter text: ")
user_color = input("Enter color: ").lower()
print_art(user_text, user_color)

#? Importing custom written modules
import do_math

print(do_math.add(22, 55, 12, 66))
print(do_math.divide(55, 55, 8))
print(do_math.multiply(55, 2, 1))
print(__name__)