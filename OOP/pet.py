class Pet:
    allowed_pets = ["cat", "dog", "fish"]

    def __init__(self, pet_name, species):
        species = species.lower()
        if species not in Pet.allowed_pets:
            raise ValueError(f"You can't have a {species} as a pet!")
        else:
            self.pet_name = pet_name
            self.species = species

    def get_pet_info(self):
        print(f"Name: {self.pet_name}\nSpecies: {self.species}")

    def set_species(self, species):
        if species not in Pet.allowed_pets:
            raise ValueError(f"You can't have a {species} as a pet!")
        else:
            self.species = species

pet1 = Pet("Good Doggo", "dog")
pet2 = Pet("Bad Cate", "cat")
pet1.get_pet_info()
pet2.get_pet_info()
print(pet1.allowed_pets)
pet2.set_species("tiger") #! Will raise a ValueError
pet2.get_pet_info()