# First way of making a dictionary
jeg = { "half dead" : True, "age" : 21, "favorite color" : "anything that resembles pain" }
print(jeg)

# More vulgar way of making a dictionary
jeg = dict(half_dead = True, age = 21, favorite_color = "anything that resembles pain")
print(jeg)

print(jeg["age"]) # accessing data or jeg.get("age")

jeg["half dead"] = False # update data
print(jeg["half dead"])

students =  { 
            201312416 : "Jeg Ramos",
            201312455 : "Carlo Ramos",
            201356699 : "Ramirez",
            666666666 : "Totally not Satan"
            }

for value in students.values() : # iterate the values
    print(value)

for key in students.keys() : # iterate the keys
    print(key)

for key,value in students.items() : # iterate using both
    print(f"{key} - {value}")

is_he_there = 201312416 in students # check for existence using the key
print(is_he_there)

is_he_there = "Jeg Ramos" in students.values() # check existence using values
print(is_he_there)