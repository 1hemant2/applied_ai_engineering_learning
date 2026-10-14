# Return two DISTINCT indices whose values add up to target.
# Use a dictionary.
# Aim for O(n) expected time.
# Return [] if no pair exists.

def two_sum(nums: list[int], target: int) -> list[int]:
    hm = {}
    for i, ele in enumerate(nums):
        if target - ele not in hm:
            hm[ele] = i
        else: 
            otherIdx = hm.get(target - ele)
            return [i, otherIdx]
    return []



print(two_sum([2, 7, 11, 15], 9))  # [0, 1]
print(two_sum([3, 2, 4], 6))       # [1, 2]
print(two_sum([3, 3], 6))          # [0, 1]
print(two_sum([1, 2, 3], 10))      # []

# Explain:
# 1. How do you prevent reusing the same index?
# Ans: I am traversing the each element only once
# 2. What are your time and space complexities?
# Ans: tc: O(n), sc: O(n)