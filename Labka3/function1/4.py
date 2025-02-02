def prime(list):
    new_list = []
    temp = 0
    for i in range(len(list)):
        for j in range(1 ,int(list[i]) + 1):
            if(int(list[i]) % j == 0):
                temp += 1
        if(temp == 2):
            new_list.append(list[i])
        temp = 0

    print('prime numbers' , *new_list)

my_list = list(input().split())
prime(my_list)
