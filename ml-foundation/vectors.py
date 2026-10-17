from math import sqrt 

# vector : it is an ordered list, l2_distance is to find the overall simillarity between two object. 
# just comparing two element will give the simillarity between two element not overall 
# l2_distance is one of the mechanism to find the distance between two object
# dimension -> number of properties in the list

def  l2_distance(a: list, b: list) -> float: 
    diff = []
    n = len(a)
    if len(a) != len(b):
        raise ValueError("Vectors must have the same number of dimensions")
    for i in range(0, n):
        diff.append(a[i] - b[i])
    dist = sqrt(sum(value ** 2 for value in diff)) 
    return dist


def l1_distance(a: list[int], b: list[int]) -> int:
    if len(a) != len(b):
        raise ValueError("Vectors must have the same number of dimensions")
    diff = []
    for i in range(len(a)):
        diff.append(abs(a[i] - b[i]))
    return sum(diff)


A = [0, 0]
B = [3, 0]
C = [2, 2]

print("L1 — A to B:", l1_distance(A, B))
print("L1 — A to C:", l1_distance(A, C))

print("L2 — A to B:", l2_distance(A, B))
print("L2 — A to C:", l2_distance(A, C))
