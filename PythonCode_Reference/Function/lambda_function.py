"""Anonymous: Lambda functions are anonymous, meaning they do not have a name.
  Single Expression: They can only contain a single expression, which is evaluated and returned.
  Multiple Arguments: They can take multiple arguments, just like regular functions."""

add = lambda x, y: x + y
print(add(5, 3))

# Sorting with lambda
# Sort a list of tuples by the second value in each tuple.
tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
tuples.sort(key=lambda x: x[1])
print(tuples)

# Filter with lambda
# Filter a list of numbers to get only the even ones.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)

# Map with lambda
# Double all numbers in a list.
numbers = [1, 2, 3, 4, 5]
doubles = list(map(lambda x: x * 2, numbers))
print(doubles)

# Reduce with lambda
# Add up all numbers in a list.
from functools import reduce

numbers = [1, 2, 3, 4]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)
