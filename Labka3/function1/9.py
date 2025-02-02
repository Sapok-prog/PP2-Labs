import math 

def volume(radious):
    V = (4/3) * radious * math.pi
    return V

radious = int(input())
print(f'Volume = {volume(radious)}')


