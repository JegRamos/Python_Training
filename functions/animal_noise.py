def get_noise(animal="dog") :
    """Returns a noise string based on the argument

    Keyword Arguments:
        animal {str} -- [description] (default: {"dog"})

    Returns:
        [type] -- [description]
    """

    noises = { "dog" : "bork bork", "cat" : "meow", "horse" : "hiyaaa", "pig" : "oink" }
    noise = noises.get(animal.lower())
    if noise :
        return f"{noise.upper()}!"
    return "wtf is that?"

animal_noise = get_noise("cat")
print(animal_noise)

# keyword arguments
def get_full_name(first_name, last_name) :
    return f"Your fullname is {first_name} {last_name}"

fullname = get_full_name(last_name = "Ramos", first_name = "Jeg")
print(fullname)
