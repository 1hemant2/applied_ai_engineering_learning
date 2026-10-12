# A. Local versus global
language = "Python"

def choose_language():
    language = "Java"
    print(language)

choose_language()
print(language)
# Prediction and reason:
# Java
# Python
# because local variable shadow the global variable


# B. Reading a global
score = 10

def show_score():
    print(score)

show_score()
# Prediction and reason:
# 10, because locally score isn't present it will read global variable

# C. Block scope
if True:
    message = "Ready"

print(message)
# Prediction and reason:
#  Ready


# D. Assignment inside a function
count = 1

def update_count():
    print(count)
    count = 2

# Predict what happens if we call this.
# Uncomment only after predicting; an error will stop execution.
# update_count()
# Prediction and reason:
# UnboundedError, because we are trying to access count before defining, it is defined local but in local we are trying to access it before defining it