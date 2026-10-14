# 1. Import parse_age from age_utils.
from python_core.age_utils import parse_age

# 2. Test each input using parse_age.
# Print valid ages; catch ValueError and print its message.
test_values = ["25", "abc", "-3"]
for ele in test_values: 
    try:
        val = parse_age(ele)
        print(val)
    except ValueError as error:
        print(f"error: {error}")

# 3. Will running this file also print the demo value 30
# from age_utils.py? Explain why.
# Answer: No running this file won't print 30 because that file doesn't load directly so python don't give that file lable as main instead app.py will get label as __main__

