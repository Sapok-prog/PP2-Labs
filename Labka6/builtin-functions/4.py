import math
import time

number = int(input())
milleseconds = int(input())

time.sleep(milleseconds/1000)

print(f"Square root of {number} after {milleseconds} miliseconds is {math.sqrt(number)}")