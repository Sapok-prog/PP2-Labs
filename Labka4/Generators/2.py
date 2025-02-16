def even_nums(n):
    for i in range(n + 1):
        if(i % 2 == 0):
            yield i
    
n = int(input("Input numver"))
for i in even_nums(n):
    print(i , " , ")
