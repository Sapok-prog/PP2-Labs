def solve(numheads , numlegs):
    for i in range(numheads + 1): #chicken
        for j in range(numheads + 1): #rabbit
            if(i + j == numheads and 2*i + 4*j == numlegs):
                return i , j
    return 0 , 0          
                

numheads = int(input())
numlegs = int(input())
a , b = solve(numheads , numlegs)
print(f'{a} chicken , {b} rabbits')