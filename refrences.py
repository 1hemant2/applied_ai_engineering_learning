# A. Assignment and mutation
# Prediction and reason:
a = [1, 2]
b = a
b.append(3)
print("A:", a, b, a is b)

# B. Immutable integers
# Prediction and reason:
x = 10
y = x
y += 5
print("B:", x, y)

# C. Copying a flat list
# Prediction and reason:
a = [1, 2]
b = a.copy()
b.append(3)
print("C:", a, b, a == b, a is b)

# D. Copying a nested list
# Prediction and reason:
a = [[1, 2], [3, 4]]
b = a.copy()
b[0].append(99)
print("D:", a, b, a is b, a[0] is b[0])