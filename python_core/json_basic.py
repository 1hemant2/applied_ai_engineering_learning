import json

user = {"name": "Hemant", "learning": True, "project": None}

# 1. Convert user to JSON text.
# Print the text and its type.
text = json.dumps(user)
print(text)
print(type(text))

# 2. Parse that text back into a Python object.
# Print the object and its type.
restored = json.loads(text)
print(restored)
print(type(restored))

# 3. Print the restored user's name using dictionary access.
print(restored["name"])

# 4. This JSON has an invalid trailing comma.
# Try parsing it and catch json.JSONDecodeError.
# Print an error message without crashing.
invalid_text = '{"name": "Hemant",}'
try:
    invalidTxt = json.loads(invalid_text)
except json.JSONDecodeError as error:
    print(f"parsing error: {error}")

# 5. Predict the two types below.
parsed = json.loads('{"active": true, "score": null}')
print(type(parsed["active"])) # <class 'bool'>
print(type(parsed["score"])) # <class 'NoneType'>
# Prediction:
