import re

def check(txt):
    patterns = r'ab{2,3}'
    if(re.search(patterns , txt)):
        return "Oh Yessssssss"
    return "no."

txt = input()
print(check(txt))