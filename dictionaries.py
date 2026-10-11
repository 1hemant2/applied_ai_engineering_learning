learner = {"name": "Hemant", "experience": 2}

# 1. Print the name using its key.
print(learner["name"])

# 2. Update experience to 3.
learner["experience"] = 3

# 3. Add a language key with the value "Python".
learner["language"] = "Python"

# 4. Read city using get(), with "Unknown" as the fallback.
# Print the result.
print(learner.get("city", "unknown"))

# 5. Check whether the language key exists.
print("language" in learner)

# 6. Loop through all key–value pairs and print each pair.
for key, val in learner.items(): 
    print(f"key : {key} val : {val}")

# 7. Print the number of entries.
print(len(learner))

# 8. Delete experience, then print the dictionary.
del learner["experience"]

# 9. Predict the result of each line. Leave them commented.
# print(learner["city"]) -> TypeError
# print(learner.get("city")) -> None
