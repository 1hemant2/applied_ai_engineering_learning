nums = [1, 2, 3, 4, 5, 6]

# 1. Use a list comprehension to create squares.
# Expected: [1, 4, 9, 16, 25, 36]
squares = [num * num for num in nums]
print(squares)

# 2. Use a list comprehension to keep only even numbers.
# Expected: [2, 4, 6]
even = [num for num in nums if num % 2 == 0]
print(even)

# 3. Combine filtering and transformation: square only even numbers.
# Expected: [4, 16, 36]
evenSquare = [num * num for num in nums if num % 2 == 0]

words = ["Python", "API", "backend"]

# 4. Use a dict comprehension to map each word to its length.
# Expected: {"Python": 6, "API": 3, "backend": 7}
wordLenMap = {word: len(word) for word in words}

# Print each result above.

# 5. Predict both outputs before running.
x = 99
values = [x * 2 for x in [1, 2, 3]]
print(values) # [2, 4, 6], comprehension doesn't change outer value like loop
print(x) # 99
# Prediction and reason:
