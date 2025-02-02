def histogram(list):
    for i in list:
        print(int(i) * "*")

list = list(input().split())
histogram(list)