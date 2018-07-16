# systax
# tuple_sample = ( 1, 2, 3, 4 )
# It is immutable, cannot be changed! And it's lightweight

numbers =  tuple(range(1, 11))
print(numbers)
numbers[2] == "A" # Not gonna happen!
print(numbers)

# Using tuples in a dictionary as keys
students = {
    ("201312416") : "Jeg Ramos",
    ("666666666") : "Totally not Satan",
    ("777777777") : "Man Luck"
}
print(students["201312416"])

manila = {
    (6552, 2552) : "SM Manila",
    (66963, 5522) : "Adamson University",
    (45521, 5522) : "La Salle",
    (45552, 4478) : "Pedro Gil"
}
print(manila[(66963, 5522)])

# the .items() method of the dictionary will return tuples

# iteratin tuples
names = ( "Jeg", "Pepper", "Tony", "Albert" )
for name in names : 
    print(name)

# count method
grades = ( 95, 55, 80, 80, 95, 80, 95 )
print(grades.count(95))

# index
print(grades.index(80)) # will only return the first matching value

# PS. Slicing also works
