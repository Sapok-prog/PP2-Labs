from itertools import permutations

def permut(slovo):
    permut_result = permutations(slovo)
    return permut_result

slovo = input()
result = permut(slovo)

for i in result:
    print(*i)