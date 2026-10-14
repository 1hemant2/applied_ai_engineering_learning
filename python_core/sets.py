numbers = [1, 2, 2, 3, 3, 4]

# 1. Convert numbers into a set. Print it and its length.
unique_num = set(numbers)

# 2. Check whether 3 is present.
print(3 in unique_num)

# 3. Add 5, then discard 2. Print the updated set.
unique_num.add(5)
unique_num.discard(2)
print(set)

# 4. Discard 99, which isn't present. Does it raise an error?
unique_num.discard(99) # no it will do nothing, if key isn't present

a = {1, 2, 3}
b = {3, 4, 5}

# 5. Print their union, intersection and a - b.
print(a | b)
print(a & b)
print(a - b)

# 6. Create an empty set and print its type.
set2 = set();
print(type(set2))

# 7. Predict these separately; leave them commented.
# print(type({})) -> dictionary
# print(a[0]) -> i think it doesn't accessible by index so it should throw error.