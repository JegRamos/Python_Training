# This is too easy
#! This is the old way of doing things
my_file = open("readme.txt")

content = my_file.read()
my_file.seek(0) #? Puts the cursor back on top of the file

print(content)

content2 = my_file.readlines()
print(content2)

my_file.close()

#* New and best way
with open("readme.txt") as my_file:
    content = my_file.read()
    my_file.seek(0) #? reset the cursor back on top of the file
    print(content)
    #* No need to close

#* Appending things to your file
with open("appendme.txt", mode = "a") as my_file: #? or use a+ to also be able to read the file
    my_file.write("\nThis text is appended")

#* Writing/Overwriting
with open("overwrite.txt", mode = "w") as my_file: #? or use w+ to also be able to read the file
    my_file.write("\nI created this file!")