from functools import reduce

list = list(input().split())

result = reduce(lambda x , y: int(x) * int(y) , list)

print("The product of all numbers in the list is:", result)