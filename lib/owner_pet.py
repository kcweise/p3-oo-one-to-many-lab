class Pet:

    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name = None, pet_type = None, owner = None):
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)


    @property
    def pet_type(self):
        return self._pet_type

    @pet_type.setter
    def pet_type(self, pet_type):
        if pet_type not in Pet.PET_TYPES:
            raise Exception (f"pet_type must be one of these {Pet.PET_TYPES}")
        self._pet_type = pet_type


    pass

class Owner:

    def __init__(self, name = None):
        self.name = name

    def pets (self):           
        return [pet for pet in Pet.all if pet.owner ==self]

    def add_pet(self, pet):
        pet.owner = self

    def get_sorted_pets(self):
        my_pets = [pet for pet in Pet.all if pet.owner ==self]
        return sorted(my_pets, key = lambda  pet:pet.name)
        
    pass