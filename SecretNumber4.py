import random
import datetime

from func import *



secret = random.randint(1, 30)
attempts = 0

#load data from json file to variables
score_data = load()

#print all results
printscore(0, score_data)

#print best x scores
printscore(3, score_data)

name = input("please enter your name: ")
while True:
    guess = int(input("please guess integer number between 1 and 30: "))
    attempts += 1
    if guess == secret:
        wrong = attempts - 1
        score_data.append({"name": name, "attempts": attempts, "wrong": wrong, "time": str(datetime.datetime.now()), "guessed_number": str(guess) })

        #save new data from variables to json file
        save(score_data)

        #print winning message
        printscore(1, attempts)

        break
    elif guess > secret:
        print("Sorry, you guessed too high! try lower")
    elif guess < secret:
        print("Sorry, you guessed too low! try higher")

