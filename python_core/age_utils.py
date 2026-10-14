# 1. Move your working parse_age function here.
def parse_age(ageStr: str) -> int: 
    age = int(ageStr)
    if age < 0:
        raise ValueError("Age cannot be negative")
    return age

# 2. Inside an if __name__ == "__main__": block,
# print the result of parse_age("30").
if __name__ == "__main__":
    print(parse_age("30"))