import re

def splitik(txt):
    pattern = r'(?=[A-Z])'
    return re.split(pattern , txt)

txt = input()
print(splitik(txt))