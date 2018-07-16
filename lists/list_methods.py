# list methods are called after the dot (.) operator

# append method
first_list = list(range(1, 11))
second_list = ["purple", "red"]
first_list.append(second_list) # Can only take one parameter; adds the appended values/object as a single object/value
print(first_list)

# extend method
first_list = list(range(1, 11))
second_list = ["purple", "blue"]
first_list.extend(second_list) # Adds values individualy
print(first_list)

# insert method
first_list = ["Monsters", "Aliens", "Gilas Pilipinas"]
first_list.insert(1, "Mabuhay") # inserts a value at a specified index
print(first_list)

# clear method
first_list = ["Something", "is", "inserted", "here"]
first_list.clear() # delete everything from a list
print(first_list)

# pop method
first_list = ["Purple", "Teal", "Cyan", "Green", "Yellow"]
color = first_list.pop(1) # deletes an item from a list and returns it
print(color)

# remove method
first_list = ["Jeg", "Sarah", "Jona", "Gie", "Shirley"]
first_list.remove("Sarah") # takes a value and removes it
print(first_list)

# index method
first_list = ["Optimus Prime", "Bumble Bee", "Jazz", "Megatron"]
transformer_index = first_list.index("Optimus Prime") # returns the index of a given value
print(transformer_index)

# index method : handling duplicates
first_list = ["Optimus Prime", "Bumble Bee", "Optimus Prime", "Megatron", "Optimus Prime"]
transformer_index = first_list.index("Optimus Prime", 2) # you can pass in the starting and ending indeces
print(transformer_index)

# count method
first_list = ["Optimus Prime", "Bumble Bee", "Optimus Prime", "Megatron", "Optimus Prime"]
times = first_list.count("Optimus Prime") # counts how many times a value occurs in the list
print(times)

# reverse method
first_list = ["Jeg", "Sarah", "Jona"]
first_list.reverse()
print(first_list)

# sort method
first_list = ["Arya", "Ned", "Rob", "Jon", "Sansa"]
first_list.sort()
print(first_list)

# copy method
copied_list = first_list.copy()
print(copied_list)

# join method. This is a string method.
word_list = ["Python", "is", "great"]
sentence = " ".join(word_list)
print(sentence)

word_list = ["Mr", "Ramos"]
name = ". ".join(word_list)
print(name)