# *args packs arguments as tuples
def judge_favorite_colors(*args) :  # or any varible in this case
    have_great_taste = False
    if "purple" in args : 
        have_great_taste = True
        return have_great_taste
    return have_great_taste

print(judge_favorite_colors("red", "blue", "purple"))

# **kwargs packs keyword assigned arguments as a dictionary
def print_favorite_colors(**kwargs) : 
    for person, color in kwargs.items() : 
        print(f"{person.capitalize()}'s favorite color is {color}")

print_favorite_colors(jeg = "blue", carlo = "red", ramos = "orange")

# there is an order in using parameters in the event you need to use all
# parameters -> *args -> default parameters -> **kwargs