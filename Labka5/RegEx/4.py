import re

def check(txt):
    patterns = r'[A-Z][a-z]+'
    if(re.search(patterns , txt)):
        return "Oh Yessssssss"
    return "no."

txt = input()
print(check(txt))