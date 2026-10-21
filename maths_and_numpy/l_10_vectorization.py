import numpy as np

deliveries = np.array([
    [5, 3],
    [2, 1],
    [8, 4],
])
weights = np.array([2, 4])
# @ combines the two features into one number per delivery.
# * keeps each feature’s contribution separately.
seprateContribution = deliveries * weights  # Shape (3, 2): separate contributions
sumPrediction = deliveries @ weights  # Shape (3,):   summed prediction per row
print(f"seprate contribuotion \n {seprateContribution}")
print(f"sum prediction : \n {sumPrediction}")

scores = np.array([1000.0, 1001.0, 1002.0])

# exp_scores = np.exp(scores) #  RuntimeWarning: overflow encountered in exp exp_scores = np.exp(scores)
# print(exp_scores)
# print(exp_scores / exp_scores.sum())

shifted = scores - scores.max()
# [-2, -1, 0]

exp_scores = np.exp(shifted)
probabilities = exp_scores / exp_scores.sum()

print(f"probalities {probabilities}")
print(f"probalities sum {probabilities.sum()}")


## Each row is a separate message, so each row needs its own probabilities summing to 1, a separate total for each row.
scores = np.array([
    [2.0, 4.0, 2.0],  # Message 1: three category scores
    [1.0, 1.0, 1.0],  # Message 2: three category scores
])
# In NumPy, axis=1 means we combine values across the columns, separately for each row:
row_max = scores.max(axis=1, keepdims=True) # keepdims=True keeps each row’s maximum and total in shape (2, 1), so broadcasting applies them to their corresponding rows.
exp_scores = np.exp(scores - row_max)

row_totals = exp_scores.sum(axis=1, keepdims=True)
probabilities = exp_scores / row_totals

print(f"matrix probalites \n {probabilities}")
print(f"matrix probalites sum \n {probabilities.sum(axis=1)}")