def square(num):
    for i in range(num + 1):
        yield i ** 2
        

sum_num_N = int(input("Input some number : "))
for i in square(sum_num_N):
    print(i , end = ' ')