# These are formal mathematical sets. Every item is unique and there is no order. You can't use index coz there is no order
# Syntax
# s = { 1, 2, 4, 6 } # just like a dictionary without pairing

numbers = { 55, 55, 69, 1, 2, 3, 1 }
print(numbers)

# access values
for number in numbers : 
    print(number)

# converting a list to a set and back
universities = [ "Adamson", "UE", "Ateneo", "La Salle", "Adamson", "NU", "UE", "UP", "Ateneo", "UP", "FEU", "UST" ]
universities = set(universities)
print(universities)

universities = list(universities)
universities.sort()
print(universities)

# add method
subjects = { "Physics", "Java OOP", "Technical English" }
subjects.add("Statistics")

# remove method
subjects.remove("Java OOP") # you can also use .discard() if you don't want to return an error
print(subjects)

# copy method
subjects2 = subjects.copy()
print(subjects2)

# clear method
subjects2.clear()
print(subjects2)

# Set Math
math_students = { "Jeg", "Sarah", "Jona", "Virgie", "Roj", "Shirley", "Rommy" }
science_students = { "Jona", "Elaine", "Malou", "Jeg", "Paolo", "Symoun", "Sarah" }

# Union - combine sets withou duplication
all_students = math_students | science_students
print(all_students)

# Intersection - outputs equal values in sets (in both subjects)
math_science_students = math_students & science_students
print(math_science_students)