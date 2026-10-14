# A. Assignment and mutation
# Prediction and reason:
a = [1, 2]
b = a
b.append(3)
print("A:", a, b, a is b)
#ans: A:[1, 2, 3] [1, 2, 3] true -> because here b have stored refrence of a so modifing b will affect a. 

# B. Immutable integers
# Prediction and reason:
x = 10
y = x
y += 5
print("B:", x, y)
#ans: B: 10, 15 because here value of y is got replaced.

# C. Copying a flat list
# Prediction and reason:
a = [1, 2]
b = a.copy()
b.append(3)
print("C:", a, b, a == b, a is b)
# C: [1, 2] [1, 2, 3], false, false
# got copy by value instead of refrences.

# D. Copying a nested list
# Prediction and reason:
a = [[1, 2], [3, 4]]
b = a.copy()
b[0].append(99)
print("D:", a, b, a is b, a[0] is b[0])
# D: [[1, 2, 99], [3, 4]], [[1, 2, 99], [3, 4]], false, true 
# it's creating a shallow copy and internal array refrence are still there that's why modifying internal value will be in sync with a internal and a and refrece object is diffrent but a[0] and b[0] refrence are same
