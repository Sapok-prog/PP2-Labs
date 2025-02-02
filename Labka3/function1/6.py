def reverse(list):
    return list[::-1]

my_list = list(input().split())
print(*reverse(my_list))