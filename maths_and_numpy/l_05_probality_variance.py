# Probability describes how likely an event is, using a number between 0 and 1, 0 means impossible,  1 means certain, 0.25 -> 25 % chance.
# Observed failure rate is 15/50 = 30%.
# This estimates the next request's failure probability
# if conditions remain similar; it isn't a guaranteed probability.

# Variance: average squared distance from the mean.
# It is NOT the farthest value from the mean.
# mean: sum(ele) / number of element
# variance: farthest value from mean, 
# A larger standard deviation means more spread around the mean; a smaller standard deviation means values cluster closer to the mean.

from math import sqrt

def mean(values: list[float]) -> float:
    if not values:
        raise ValueError("Values must not be empty")
    return sum(values) / len(values)

def variance(values: list[float]) -> float:
    mean_val = mean(values)
    squared_differences = [
        (value - mean_val) ** 2
        for value in values
    ]
    return mean(squared_differences)


if __name__ == "__main__":
    a = [300, 300, 300, 300] 
    b = [100, 500, 100, 500]
    print(f"a mean: {mean(a)}")
    print(f"b mean: {mean(b)}")
    print(f"a variance: {variance(a)}")
    print(f"b variance: {variance(b)}")

    print(f"b standard deviation:{sqrt(variance(b))}")
