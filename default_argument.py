# 1. Predict both outputs BEFORE running. Explain why.
def add_tag(tag, tags=[]):
    tags.append(tag)
    return tags

print(add_tag("python"))
print(add_tag("fastapi"))
# Prediction and reason:
# python
# python, fastapi
# this happens because default values are evaluated when function defined not on every function calls


# 2. Define add_tag_safe using None as the default.
# Create a new list when tags is None.
# Append tag and return the list.
def add_tag_safe(tag, tags = None):
    if tags == None: 
        tags = []
    tags.append(tag)
    return tags



# 3. Call add_tag_safe twice without supplying tags.
# Print each result. They should be independent lists.
tags1 = add_tag_safe("red")
tags2 = add_tag_safe("blue")
print(tags1)
print(tags2)

# 4. Pass this list to add_tag_safe using KEYWORD arguments.
# Add "python", then print existing.
existing = ["backend"]
add_tag_safe(tags = existing, tag = "python")
print(existing)

# Explain why existing changes:
# existing changes because we pass the reference of existing in the function