# A derivative tells us how quickly an output changes when an input changes. 
# In ML, this helps us work out how changing a weight affects prediction error.
# a derivative tells us how much the output changes per unit change in whichever input we’re examining.

# predicted_time = weight * distance + 10
#Change distance, holding weight fixed → derivative is weight.
#Change weight, holding distance fixed → derivative is distance.


# A gradient collects the error’s derivative for each weight. For example: 
# gradient = [6, -2]
#           w1  w2
#6: increasing w1 slightly increases error → decrease w1.
#-2: increasing w2 slightly decreases error → increase w2.


def error(w):
    return (w - 3) ** 2

w = 1.0
step = 0.001

slope = (error(w + step) - error(w)) / step

print(error(1.0))
print(error(1.1))

#The error dropped from 4.0 to 3.61, confirming that increasing the weight slightly reduced error, 
# as the negative derivative predicted.