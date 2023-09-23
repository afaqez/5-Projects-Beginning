import random

userWins = 0
compWins = 0
options = ["rock", "paper", "scissors"]

while True:
    userPick = input("Rock, Paper or Scissors? (Press \"q\" to quit): ").lower()
    if userPick == "q":
        print("Your score:", userWins)
        print("Comp score:", compWins)
        quit()

    if userPick not in options:
        print("Enter a correct option!")
        continue

    randomNumber = random.randint(0, 2)
    compPick = options[randomNumber]

    if userPick == "rock" and compPick == "scissors":
        print("You win! The computer choosed", compPick )
        userWins += 1

    elif userPick == "scissors" and compPick == "scissors":
        print("You win! The computer choosed", compPick )
        userWins += 1

    elif userPick == "paper" and compPick == "rock":
        print("You win! The computer choosed", compPick )
        userWins += 1

    elif userPick == compPick:
        print("You tied! The computer also choosed", compPick)

    else:
        print("You lose! The computer choosed", compPick)
        compWins += 1