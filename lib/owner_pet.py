# lib/owner_pet.py
class Owner:
    def __init__(self, name):
        self.name = name
        
    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("Input must be an instance of Pet class")
        pet.owner = self
        
    def get_sorted_pets(self):
        my_pets = self.pets()
        return sorted(my_pets, key=lambda pet: pet.name)


class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    
    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type. Must be one of {Pet.PET_TYPES}")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
    
    @property
    def owner(self):
        return self._owner
    
    @owner.setter
    def owner(self, owner):
        if owner is not None and not isinstance(owner, Owner):
            raise Exception("Owner must be an instance of Owner class")
        self._owner = owner