def variable_length_arguments(*args):
    for arg in args:
        print(arg)


variable_length_arguments(1, "String", True, 4, 5.09, 6, 7, 8, 9, 10)


def variable_length_arguments2(**dict_type):
    for key, value in dict_type.items():
        print(f"{key} : {value}")


variable_length_arguments2(name="John", age=25, is_student=True, is_employed=False, is_married=False)


def variable_length_arguments3(*args, **kwargs):
    for arg in args:
        print(arg)
    for key, value in kwargs.items():
        print(f"{key} : {value}")


variable_length_arguments3(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, name="John", age=25, is_student=True, is_employed=False,
                           is_married=False)


def variable_length_arguments_default_values(pet_name, pet_type="Dog", *args, **kwargs):
    print(f"I have a {pet_type} named {pet_name}.")
    for arg in args:
        print(f"Additional info: {arg}")
    for key, value in kwargs.items():
        print(f"{key}: {value}")


variable_length_arguments_default_values("Buddy","Dog","loves to play", age=5, color="brown")
