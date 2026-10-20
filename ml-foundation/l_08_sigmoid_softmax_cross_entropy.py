#sigmoid: converts the model’s score into a probability. it converts one score into a probability of label 1.

# | Raw score | Sigmoid output: probability of spam |
# |---:|---:|
# | `-2` | ≈ 12% |
# | `0` | 50% |
# | `2` | ≈ 88% |


import math

def sigmoid(score):
    return 1 / (1 + math.exp(-score))

for score in [-2, 0, 2]:
    print(score, round(sigmoid(score), 3))



# Softmax: converts several competing scores into probabilities for one category choice.

# | Situation | Billing score | Technical score | Softmax probabilities |
# | Equal scores | 2 | 2 | Billing 50%, technical 50% |
# | Technical score rises | 2 | 4 | Billing ≈12%, technical ≈88% |


import math

def softmax(scores):
    # Subtracting the maximum prevents very large exponentials.
    # It preserves the resulting probabilities.
    shifted = [score - max(scores) for score in scores]
    exp_scores = [math.exp(score) for score in shifted]
    total = sum(exp_scores)
    return [value / total for value in exp_scores]

# here is the softmax program flow, 
#scores = [102, 104, 102]
#max_score = 104

#shifted = [-2, 0, -2]  # Last value is also 102 - 104 = -2. now normlaize it using exp_score and find probality for each ele.

print(softmax([102, 104, 102]))
print(softmax([2, 4, 2]))


# still it's blurry, why e^x, one reason is to make the value positive, then question why not other constant like 3 ^ x, i
#  will revisit this. 
# why substracting max score isn't changing the prbolity of the item, i will revist this later.


# cross entropic

# | Model prediction | Probability assigned to technical |
# |---|---:|
# | A | 80% |
# | B | 10% |
#Suppose a message’s actual category is technical:
#We need an error measure that penalises B more heavily. Cross-entropy does this


import math

# Order: billing, technical, account
actual_label = 0  # Billing

for probabilities in [[0.6, 0.3, 0.1], [0.1, 0.8, 0.1]]:
    p_correct = probabilities[actual_label]
    loss = -math.log(p_correct)
    print(f"p_correct={p_correct}, loss={loss:.3f}")

#will revisit this topic again.