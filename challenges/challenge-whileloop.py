import random

highest = 10
answer = random.randint(1,highest)
guess = 0

while guess != answer:
    print("Please guess a number between 1 and {}: ".format(highest))
    guess = int(input())
    if guess == 0:
        print("goodbye")
        break
    elif guess < answer:
        print("guess higher")
    elif guess > answer:
        print("guess lower")
    else:
        print("you got it")