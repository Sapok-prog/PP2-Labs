def calculate_up_lw(txt):
    lower_case = sum(1 for x in txt if x.islower())
    upper_case = sum(1 for a in txt if a.isupper())
    print( f"Sum of lower case letters:{lower_case}, upper case letters:{upper_case}")

a = input()
calculate_up_lw(a)