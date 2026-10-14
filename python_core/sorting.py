nums = [8, 3, 5, 1]

# 1. Print a new ascending list using sorted().
# Then print nums to confirm it hasn't changed.
print(sorted(nums))
print(nums)

# 2. Print a new descending list.
print(sorted(nums, reverse=True))

words = ["Python", "API", "backend"]

# 3. Sort words by length using key=len. Print the result.
print(sorted(words, key=len))

users = [
    {"name": "Hemant", "experience": 2},
    {"name": "Asha", "experience": 5},
    {"name": "Ravi", "experience": 1},
]

# 4. Sort users by experience, highest first.
# Use a lambda key and print the result.b
print(sorted(users, key=lambda user: user["experience"]))

# 5. Predict both outputs before running.
values = [3, 1, 2]
result = values.sort()
print(values)
print(result)
# Prediction and reason:
# [1, 2, 3]
# python doesn't modify original list instead it return sorted copy of existing arrays. 