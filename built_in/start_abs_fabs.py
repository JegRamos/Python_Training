# Sum method
total = sum([1,3,5], 4) #? Will accept an iterable and an optional start
print(total)

# abs method
print(abs(-96))

# fabs method
from math import fabs #* It needs an import
print(fabs(-96))

# round method
print(round(3.5833, 2)) #* it will round it to an integer if you don't specify the number of digits

# zip method
names  = ["Jeg", "Sarah", "Jona"]
attack_power = [100, 2, 90]

combined = zip(names, attack_power) #* will return a list of tuples
combined = dict(combined)
print(combined)

#? You can also unpack tuples and lists
users = [
    ("jeg", "test engineeer"),
    ("sarah", "test engineer"),
    ("jona", "NTC")
]

unpacked_users = list(zip(*users))
print(unpacked_users)

# More complex examples
midterms = (80, 90, 85, 97)
finals = (90, 100, 95, 88)
names = ("jeg", "sarah", "jona", "gie")

midterms_finals = {g[0] : max(g[1], g[2]) for g in zip(names, midterms, finals)} #? get the hisgest grade
midterms_finals = {g[0] : ((g[1] + g[2]) / 2) for g in zip(names, midterms, finals)} #? average the grades

print(midterms_finals)