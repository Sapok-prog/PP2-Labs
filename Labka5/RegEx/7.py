import re

def to_camel_case(snake_case):
    return re.sub(r'_' , '' , snake_case)

snake_case = input()
print(to_camel_case(snake_case))

