class Chicken:
    num_chickens = 0

    def __init__(self, name):
        self.name = name
        Chicken.num_chickens += 1

    def lay_eggs(self, num_eggs):
        Chicken.num_chickens += num_eggs
        print(f"{self.name} has laid {num_eggs}\nNumber of Chickens: {Chicken.num_chickens}")

    @classmethod #? This is a decorator
    def get_chicken_total(cls):
        print(f"Total Chickens: {Chicken.num_chickens}")

c1= Chicken("Hella")
c2 = Chicken("Gabriela")
Chicken.get_chicken_total()
c1.lay_eggs(5)
Chicken.get_chicken_total()
c2.lay_eggs(4)
Chicken.get_chicken_total()
