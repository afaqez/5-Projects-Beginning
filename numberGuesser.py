import random

def check(guess, randomNumber, attempts):
    if guess == randomNumber:
        print("Congratulations! You won in", attempts, "attempts!")
        quit()
    elif guess > randomNumber:
        print("Too high, try again.")
    else:
        print("Too low, try again.")

endNumber = input("Enter a number for the range end: ")
if endNumber.isdigit():
    endNumber = int(endNumber)
    if endNumber <= 0:
        print("Enter a number greater than 0 next time!")
        quit()
else:
    print("Enter a number next time!")
    quit()

randomNumber = random.randint(1, endNumber)
attempts = 0

while True:
    guess = input("Guess a number: ")
    if guess.isdigit():
        guess = int(guess)
        if guess <= 0 or guess > endNumber:
            print("Enter a valid number within the range!")
            continue
        else:
            attempts += 1
            check(guess, randomNumber, attempts)
    else:
        print("Enter a number next time!")
        quit()
