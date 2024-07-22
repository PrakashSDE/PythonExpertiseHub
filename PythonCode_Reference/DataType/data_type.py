# Numeric Types
a = 10         # int
b = 3.14       # float
c = 1 + 2j     # complex

# Sequence Types
list_example = [1, 2, 3]         # list
tuple_example = (1, 2, 3)        # tuple
range_example = range(0, 10)     # range

# Text Type
string_example = "hello"         # str

# Binary Types
bytes_example = b'hello'         # bytes
bytearray_example = bytearray(b'hello')  # bytearray
memoryview_example = memoryview(b'hello') # memoryview

# Set Types
set_example = {1, 2, 3}          # set
frozenset_example = frozenset([1, 2, 3]) # frozenset

# Mapping Type
dict_example = {'name': 'Alice', 'age': 25} # dict

# Boolean Type
bool_example = True              # bool

# None Type
none_example = None

# type() function can be used to get the data type of an object
a = 10
print(type(a))

# isinstance() function can be used to check if an object is of a particular data type
a = 10
print(isinstance(a, int))