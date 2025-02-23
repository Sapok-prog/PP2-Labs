import re 

def check(txt):
    patterns = r'[ ,.]'
    return re.sub(patterns , ":" , txt)

txt = input()
print(check(txt))