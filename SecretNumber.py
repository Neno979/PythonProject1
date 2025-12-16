import random

secret = random.randint(1,30)
while True:
    try:
        guess = int(input("Please enter your integer guess number between 0 and 30:"))
        if guess == secret:
            print("you guessed right")
            break
        elif 31 > guess > secret:
            print("try lower number")
        elif secret > guess > -1:
            print("try higher number")
        else:
            print("number is out of range")
    except ValueError:
        print("number is not an integer")