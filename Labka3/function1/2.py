def celcius(Farenheit):
    C = (5 / 9) * (Farenheit - 32)
    print(f'{Farenheit} farenheit = {C} celcius')

F = int(input())
celcius(F)