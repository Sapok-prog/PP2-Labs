import re

def check(txt):
    patterns = 'ab*?'
    if(re.search(patterns , txt)):
        return "Oh Yessssssss"
    return "no."

txt = input()
print(check(txt))