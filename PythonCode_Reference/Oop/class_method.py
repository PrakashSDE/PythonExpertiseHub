class myclass:
    @classmethod
    def mymethod(cls):
        print("This is a class method")
        print(cls)


myclass.mymethod()

"""When to Use Class Methods:
When you need to access or modify the class state.
When you need to create factory methods that return instances of the class.
When you want to define methods that logically belong to the class but do not operate on instance data."""




