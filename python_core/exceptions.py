# 1. Define parse_age(text: str) -> int.
# Convert text to an integer.
# If the age is negative, raise ValueError("Age cannot be negative").
# Otherwise, return the age.
def parse_age(ageStr: str) -> int: 
    age = int(ageStr)
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age


# 2. Test each value below using a loop.
# INSIDE the loop:
# - Call parse_age inside try.
# - Print the returned age on success.
# - Catch ValueError as error and print its message.
# One failed input must not prevent testing the next input.
test_values = ["25", "abc", "-3"]
for ele in test_values: 
    try:
        val = parse_age(ele)
        print(val)
    except ValueError as error:
        print(f"error: {error}")


# 3. After the loop, print "Finished".
print("Finished")


# 4. Predict what happens when reject() is called.
def reject() -> int:
    raise ValueError("Rejected")
    return 10

# Does it return 10? Why?
# Answer: No, it doesn't because error is occuring before return, error will intrupt the normal flow of program and throw the error. 