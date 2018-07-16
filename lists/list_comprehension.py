# Syntax : [ __ for __ in __ ]

numbers = list(range(1, 11))
numbers_on_steroids = [ number * 10 for number in numbers ] # make a new list based upon the values of an existing one
print(numbers_on_steroids)

names = [ "jeg", "sarah", "jona" ]
capitalized_names = [ name.capitalize() for name in names ] # Capitalize the first letter of a name
print(capitalized_names)

numbers = list(range(1, 6))
string_numbers = [ str(number) for number in numbers ] # Cast the numbers to string
print(string_numbers)

# list comprehension with conditional logic

numbers_list = list(range(1, 11))
odd_numbers = [ number for number in numbers_list if number % 2 == 1 ]
even_numbers = [ number for number in numbers_list if number % 2 == 0 ]
print(f"Odd numbers: {odd_numbers}")
print(f"Even numbers: {even_numbers}")

modified_numbers = [ number * 2 if number % 2 == 0 else number / 2 for number in numbers_list ] # multiply by 2 if the number is even, else divide it by 2
print(f"Modified Numbers: {modified_numbers}")

no_vowels = [ char for char in "amazing" if char not in "aeiou" ]
print(no_vowels)

sentence = "The quick brown fox jumps over the lazy doggos"
all_consonants = ''.join([ char for char in sentence if char not in "aeiou" ]) # print all consonants
print(all_consonants)

sentence = "This string has four spaces" # count the spaces in a string
number_of_spaces = sentence.count(' ')
print(number_of_spaces)

# Multi-dimensional lists
songs = [
        ["All The Right Moves", "All This Time", "Counting Stars"], 
        ["Viva la Vida", "Paradise", "Fix You"],
        ["Murder Song", "The Seed", "Soft Universe"]
        ]

all_this_time = songs[0][1] # Multi-dimensional selection
print(all_this_time)

aurora_songs = ', '.join(songs[2][:]) # With splicing
print(aurora_songs)

# Print all songs
num = 1
for bands in songs : 
    for song in bands : 
        print(f"{num}. {song}")
        num += 1

# Multi-dimensional list comprehension
board = [ [ "*" for j in range(1,4) ] for i in range(1,4) ]
print(board) # [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*']]

board = [ [ "X" if j % 2 != 0 else "O" for j in range(1,4)] for i in range(1,4) ] # with conditions
print(board) # [['X', 'O', 'X'], ['X', 'O', 'X'], ['X', 'O', 'X']]

