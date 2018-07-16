number = 20

def add() : 
    global number
    number += 10
    return number

print(add())
print(number)

# There is also a nonlocal variable scope