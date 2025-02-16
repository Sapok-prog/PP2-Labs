def return_pokie(n):
    for i in range(n , -1 , - 1):
        yield i

n = int(input("Input a number : "))
for i in return_pokie(n):
    print(i , end = " ")