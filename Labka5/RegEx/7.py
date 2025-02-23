import re

def to_camel_case(snake_case):
    x = re.sub("_[a-z]" , lambda m : m.group(0)[1].upper(), snake_case)
    return x

snake_case = input()
print(to_camel_case(snake_case))

