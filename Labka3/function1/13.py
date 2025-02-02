import random
def quess_the_number():
    tsss_secret = random.randint(1 , 21)
    try_count = 0
    name = input("Hello! What is your name?")
    print(f'Well, {name} , I am thinking of a number between 1 and 20.')
    start_quess = 0 
    while(start_quess != tsss_secret):
        start_quess = int(input("Take a quess."))
        if(start_quess < tsss_secret):
            print("Your guess is too low.")
        else:
            print("Your guess is too high.")
        try_count += 1
    print(f'Good job, {name} ! You guessed my number in {try_count} guesses!')        

quess_the_number()