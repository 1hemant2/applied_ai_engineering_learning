profile = ("Hemant", 2, "Python")

# 1. Print the first and last items, and the tuple's length.
print(f"f: {profile[0]} l: {profile[-1]}")

# 2. Unpack profile into name, experience and language.
name, experience, language = profile

# 3. Using those variables and an f-string, print:
# Hemant has 2 years of experience and is learning Python.
print(f"{name} has {experience} year of experience and is learning {language}")

# 4. Create a one-item tuple containing "FastAPI".
# Print its value and type.
framework = ("FastApi",)
print(framework[0])

# 5. Predict what happens below and explain why.
# Keep this line commented so the other tasks can run.
# profile[1] = 3
#output: TypeError