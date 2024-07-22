class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age  # Instance attribute


# Creating instances
dog1 = Dog("Buddy", 5)
dog2 = Dog("Lucy", 3)

# Modifying class attribute
print(Dog.species)
Dog.species = "Canis lupus familiaris"
print(dog1.species)  # Output: Canis lupus familiaris
print(dog2.species)  # Output: Canis lupus familiaris

# Modifying instance attribute
dog1.name = "Max"
print(dog1.name)  # Output: Max
print(dog2.name)  # Output: Lucy

print(Dog.__dict__)
print(dog1.__dict__)