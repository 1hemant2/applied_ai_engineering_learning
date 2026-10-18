# dot product: dot product mathematically means sum(a[i] * b[i])
# suppose we have to estimate the time of dilevery each km take 2 min, and each stop contribute 4 additional minute. 
# so our calculation for 5 km and 3 stop will be : 5 * 2 + 3 * 4 = 24 min. 
# we use dot product to claculate the estimate result here 2 min and 4 min are weight and chaging it change the overall estmiate. 

def dot_product(a: list[float], b: list[float]) -> float:
    if(len(a) != len(b)):
        raise ValueError("vector dimension must be same to calcualte the dot")
    ans: int = 0
    n = len(a)
    for i in range(0, n):
        ans += a[i] * b[i]

    return ans


if __name__ == "__main__":
    a = [1, 2]
    b = [2, 4]
    c = [10, 0]
    print(dot_product(a, b))
    print(dot_product(a, c))