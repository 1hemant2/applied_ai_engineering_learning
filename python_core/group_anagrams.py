# Group anagrams using a dictionary.
# Assume all words contain lowercase English letters.
# Keep duplicate words in the result.

def group_anagrams(words: list[str]) -> list[list[str]]:
    hm: dict[str, list[str]] = {}
    ans: list[list[str]] = []
    for word in words: 
        sortedWord = "".join(sorted(word))
        if sortedWord not in hm:
            hm[sortedWord] = []
        hm[sortedWord].append(word)

    for w, groupWords in hm.items(): 
        ans.append(groupWords)

    return ans


print(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
# Expected groups, in any order:
# [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]

print(group_anagrams([""]))        # [[""]]
print(group_anagrams(["a", "a"]))  # [["a", "a"]]
print(group_anagrams([]))          # []

# Explain:
# 1. What dictionary key do you use, and why?
#Ans: I want to use sorted key as key and it's value as list 
# 2. What is the time complexity?
#Ans: O(n * klogk) where k is number of character in word
# Use n = number of words, k = maximum word length.
