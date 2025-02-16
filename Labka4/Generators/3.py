def diva_3_4(n):
    for i in range(n + 1):
        if (i % 3 == 0 and i % 4 == 0):
            yield i 

n = int(input("Input number : "))
for i in diva_3_4(n):
    print(i , "-This diva is divisible by 3 and 4")