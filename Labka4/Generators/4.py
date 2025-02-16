def squares(a , b):
    for i in range(a , b + 1):
        yield i**2

a , b = int(input("Input first number : ")) , int(input("Input second number : "))
for i in squares(a , b):
    print(i , "here is our square😍")
