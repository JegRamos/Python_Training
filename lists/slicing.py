# Make a new list using the slices of the old one
# some_list[ start : end : step ]

colors = [ "Blue", "Red", "Purple", "Yellow", "Teal", "Gold" ]
last_three_colors = colors[ 2 : ]
print(last_three_colors)

first_two_colors = colors[ : 2]
print(first_two_colors)

last_color = colors[ -1 : ]
print(last_color)

all_colors = colors[ : ]
print(all_colors)

middle_colors = colors[ 1 : -1 ]
print(middle_colors)

every_other_color = colors[ 1 : : 2 ]
print(every_other_color)

# Modifying portions of a list
name_list = [ "Jeg", 21, False, "C", "Sarah", "Jona" ]
name_list[ 1 : 4 ] = [ "Gie", "Shirley" ]
print(name_list)

# Swapping values
engineers = [ "Mark Zuckerberg", "Elon Musk", "Bill Gates" ]
engineers[0], engineers[1], engineers[2] = engineers[1], engineers[2], engineers[0]
print(engineers)