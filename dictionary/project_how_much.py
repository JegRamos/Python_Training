menu_price = {
    "cheese burger" : 25,
    "pizza" : 35,
    "apple pie" : 10,
    "orange juice" : 5
}

menu = ["Cheese Burger", "Pizza", "Apple Pie", "Orange Juice"]

print("Please decide what to order!")
for item in menu :
    print(f"* {item}")

user_input = input("Enter your choice: ").lower()
while menu_price.get(user_input) == None :
    user_input = input("Please enter a valid choice: ").lower()

order_price = menu_price.get(user_input)
order_name = None
for name, price in menu_price.items() :
    if  order_price == price :
        order_name = name

order_price = f"P{float(order_price)}"
order_name = order_name.title()
print(f"The price of {order_name} is {order_price}")
