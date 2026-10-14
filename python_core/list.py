nums = [10, 25, 30, 40, 50]

# 1. Print the first and last items using f-strings.
print(f"first: {nums[0]} last: {nums[-1]}")

# 2. Print the whole list and its length.
print(nums)
print(len(nums))

#3. 
nums.append(60)

#4.
nums[1] = 25

#5.
removed = nums.pop()
print(removed);

#6. 
for ele in nums: 
    print(ele)
print(len(nums))

#7.
print(30 in nums)

#8. 
for ele in nums: 
    print(ele)