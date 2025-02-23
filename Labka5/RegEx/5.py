import re

def check(txt):
    patterns = r'a[a-z]+b$'
    if(re.search(patterns ,txt)):
            return "Oh Yessssssss"
    return "no."
txt = input()
print(check(txt))