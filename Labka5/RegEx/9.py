import re

def space(txt):
    pattern = r'(?=[A-Z])'
    return re.sub(pattern , " " , txt)

txt = input()
print(space(txt))