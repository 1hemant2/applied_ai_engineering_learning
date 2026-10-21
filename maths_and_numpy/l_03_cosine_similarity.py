# what is l1 norm of vector [6, 8], it will be 14, go 6 east then 8 north. this is also call distance.
# l1_norm get calculated abs(a[0]) + abs(a[1]) 
# what is l2 norm of vector a = [6, 8], it's a sqrt(a[0] ** 2 + a[i] ** 2), L2 norm gives the magnitude of displacement 
# in cosine simillarity we normalize the vector using l2_norm and do a dot product between vector. 

from math import sqrt

def l2_norm(a: list[float]) -> float:
    return sqrt(sum(value ** 2 for value in a))

def cosine_similarity(a: list[float], b: list[float]) -> float:
    if len(a) != len(b):
        raise ValueError("Vectors must have the same dimensions")

    norm_a = l2_norm(a)
    norm_b = l2_norm(b)

    if norm_a == 0 or norm_b == 0:
        raise ValueError("Cosine similarity is undefined for zero vectors")

    return sum(
        (a[i] / norm_a) * (b[i] / norm_b)
        for i in range(len(a))
    )

#[1, 0] and [-1, 0]

print(cosine_similarity([1, 2], [2, 4]))
print(cosine_similarity([1, 2], [10, 0]))
print(cosine_similarity([1, 0], [-1, 0]))
print(cosine_similarity([1, 0], [0, 1]))
