from math import sqrt 

def  l2_distance(a: list, b: list) -> float: 
    diff = []
    n = len(a)
    for i in range(0, n):
        diff.append(a[i] - b[i])
    dist = sqrt(sum(value ** 2 for value in diff)) 
    return dist

print(l2_distance([1, 2, 3], [4, 6, 3]))

# vector : it is an ordered list, l2_distance is to find the overall simillarity between two object. 
# just comparing two element will give the simillarity between two element not overall 
# l2_distance is one of the mechanism to find the distance between two object
# dimension -> number of properties in the list