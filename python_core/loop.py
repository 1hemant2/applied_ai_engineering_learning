# 1.
for num in range(1, 11):
    if(num % 2 == 0):
        print("Even: " + str(num))
    else: 
        print("Odd: " + str(num))

#2.
total = 0
for num in range(1, 11): 
    total += num
print(total)

#3.
language = ["Python", "FastAPI", "DSA"]
for i, l in enumerate(language, start=1): 
    print(i, l)

#4.
num = 3
while(num > 0): 
    print(num)
    num -= 1
#5.
score = 75
if(score >= 80):
    print("Excellent")
elif(score >= 50):
    print("Pass")
else:
    print("retry")
