# tuple and list unpacking
def sum__all_numbers(*args) :
    total = 0 
    for num in args : 
        total += num
    return total

numbers = [1, 9, 10, 60.6, 88]
sum = sum__all_numbers(*numbers) # just add a stupid star
print(sum)

# dictionary unpacking
def display_names(first, second):
    print(f"{first} says hello to {second}")

names = { "first": "Jeg", "second": "Rusty" }
display_names(**names)  # yup!

def add_and_multiply_numbers(a,b,c,**kwargs):
    print(a + b * c)
    print("OTHER STUFF....")
    print(kwargs)

data = dict(a=1,b=2,c=3,d=55,name="Tony")

add_and_multiply_numbers(**data) # 7
