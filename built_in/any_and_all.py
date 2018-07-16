# all method
names = [ "Jeg", "John", "Jeremy", "Japeth", "Joyce" ]
all_starts_J = all([ name if name[0].lower() == "j" else None for name in names ])
print(all_starts_J)

names.insert(1, "Mark")
print([ name[0] == "J" for name in names ])

# any method
any_starts_M = any([ name[0] == "M" for name in names ])
print(any_starts_M)