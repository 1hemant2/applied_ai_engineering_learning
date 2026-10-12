# 1. Define add(a, b), which RETURNS their sum.
# Print the returned result for add(10, 20).
def add(a, b):
    return a + b
print(add(10, 20))


# 2. Define greet(name, language="Python").
# RETURN: "Hello Hemant, let's learn Python"
# using the supplied name and language.
def  greet(name, language="Python"):
    return f"Hello {name}, let's learn {language}"

# Call it once with only a name.
# Call it again using keyword arguments, with language="Java".
# Print both returned values.
learnPython = greet('Hemant')
learnJava = greet('Hemant', 'Java')
print(learnPython, learnJava)


# 3. Define count_even(numbers).
# Use a loop to count even numbers and RETURN the count.
# Test with [1, 2, 3, 4, 6]. Expected count: 3.
def count_even(numbers): 
    evenCount = 0
    for ele in numbers: 
        if(ele % 2 == 0): evenCount += 1
    return evenCount
print(count_even([1, 2, 3, 4, 6])) 


# 4. Predict the output BEFORE running. Explain why.
def show_message():
    print("Hello")

result = show_message()
print(result)
# Prediction and reason:
# Hello
# None
# show_message() displays "Hello", but has no return, so result becomes None.