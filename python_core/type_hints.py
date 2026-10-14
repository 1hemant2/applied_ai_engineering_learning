# 1. Write add(a, b) with int parameter and return hints.
# Return their sum and test it.
def add(a: int, b: int) -> int:
    return a + b

print(add(5, 6))

# 2. Write count_even(numbers).
# Accept a list of integers and return an integer count.
# Test with [1, 2, 4, 7].
def count_even(numbers: list[int]) -> int: 
        evenEle: int = 0
        for ele in numbers: 
            if(ele % 2 == 0):
                evenEle += 1
        return evenEle
print(count_even([1, 2, 4, 7]))
            
# 3. Write word_lengths(words).
# Accept a list of strings.
# Return a dictionary mapping each word to its length.
# Add parameter and return hints.
# Test with ["Python", "API"].
def word_lengths(words: list[str]) -> dict[str, int]: 
    wl: dict[str, int] = {}
    for word in words: 
        wl[word] = len(word)
    return wl

print(word_lengths(["Python", "API"]))
# Expected: {'Python': 6, 'API': 3}

# 4. Predict the output. Does Python automatically reject this?
value: int = "hello"
print(value) # hello
# Prediction and reason: 
# reason: python doesn't reject it type check and ide use it to spot the mistake 

# 5.
# Define greet with:
# - name: str
# - prefix: str | None, defaulting to None
# - return type: str
#
# If prefix is None, use "Hello".
# Return an f-string containing the prefix and name.

# Test:
# greet("Hemant")       -> "Hello, Hemant"
# greet("Hemant", "Hi") -> "Hi, Hemant"
# Print both results.

def greet(name: str, prefix: None | str = None) -> str: 
    if prefix is None: 
        return f"Hello, {name}"

    return f"{prefix}, {name}"

res1 = greet("Hemant")
res2 = greet("Hemant", "Hi")
print(res1)
print(res2)