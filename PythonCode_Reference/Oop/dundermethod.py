class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Person(name={self.name}, age={self.age})"

    def __repr__(self):
        return f"Person('{self.name}', {self.age})"

# Creating an instance of Person
person = Person("Alice", 30)

# Using the str() function
print(str(person))  # Output: Person(name=Alice, age=30)

# Using the repr() function
print(repr(person))  # Output: Person('Alice', 30)
