print("Welcome to computer quiz!")
play = input("Do you want to play?")

if play.lower() != "yes":
    quit()
score = 0
print("Alright! Let's play then")

answer = input("What does CPU stands for?")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
answer = input("What does ROM stands for?")
if answer.lower() == "read only memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
answer = input("What does RAM stands for?")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("Your total score is ", score, "/3", sep = "")



'''

GPT Suggestion


print("Welcome to computer quiz!")
play = input("Do you want to play?")

if play.lower() != "yes":
    quit()
score = 0
print("Alright! Let's play then")

answer = input("What does CPU stands for?")
if answer.lower() == "central processing unit":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
answer = input("What does ROM stands for?")
if answer.lower() == "read only memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")
answer = input("What does RAM stands for?")
if answer.lower() == "random access memory":
    print('Correct!')
    score += 1
else:
    print("Incorrect!")

print("Your total score is ", score, "/3", sep = "")

'''


