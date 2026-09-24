import random

def guess():
    random_number = random.randint(1,9)
    while True:
        guess = int(input("Guess : "))
        if guess == random_number:
            print("You guessed it right ! ")
            break
        else:
            continue

guess()