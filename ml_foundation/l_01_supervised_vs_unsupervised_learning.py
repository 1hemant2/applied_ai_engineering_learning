# supervised: we already know the answer in advance, if model give the wrong answer we adjust the weight. 
# there are two types classification(classify in category eg: account, billing), and regression give the score(waiting time)

# Q. How we convert the text to vector ?
# Ans: this is the simple techninque, bag of words. where we count the number of count for each word.
# words = ["billing", "password"]
# [billing_count, password_count]
# "billing"          → [1, 0]
# "password"         → [0, 1]
# "billing password" → [1, 1] 

# "billing billing password" → [2, 1]

# Imagine a trained model has these weights for its account-category score: weights = [-1, 3]
# "billing" contributes -1 per occurrence.
# "password" contributes +3 per occurrence.
# account_score = 0 * (-1) + 2 * 3  # 6

# "password password"
#         ↓ Count words
# [0, 2]
#         ↓ Apply learned weights
# Category scores
#         ↓ Softmax
# Category probabilities

# Supervised: messages come with labels such as billing or account. Learn to predict those labels.
# Unsupervised: messages have no labels. Discover patterns, such as groups of similar messages.