class Animal:
    total = 0

    def __init__(self, name, age, species):
        self.name = name
        self._age = age
        self.species = species

    def __repr__(self):
        return f"The {self.species} named {self.name} is {self.age} years old"

    def make_sound(self):
        print(f"{self.name} is making a wierd sound")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if new_age > 0:
            self._age = new_age
        else:
            raise ValueError("The value of age cannot be negative")

class Cat(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Cat")
        self.breed = breed

cate = Cat("Catty", 5, "Pinoy Cate")
cate.age = 100
print(cate)
cate.make_sound()