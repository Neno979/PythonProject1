import random
import json
import datetime

secret = random.randint(1, 30)
attempts = 0

with open("Score_sheet.json" , "r") as score_file:
    score_data = json.loads(score_file.read())
    #score_data.sort()
    print("all scores: " + str(score_data))

    for score_dict in score_data:
        print("Name: " + score_dict["name"] + ", attempts: " + str(score_dict["attempts"]) + ", wrong guess: " + str(score_dict["wrong"]) + ", time: " + str(score_dict["time"]) + ", guessed number " + str(score_dict["guessed_number"]))
name = input("please enter your name: ")
while True:
    guess = int(input("please guess integer number between 1 and 30: "))
    attempts += 1
    if guess == secret:
        wrong = attempts - 1
        score_data.append({"name": name, "attempts": attempts, "wrong": wrong, "time": str(datetime.datetime.now()), "guessed_number": str(guess) })

        with open("Score_sheet.json", "w") as score_file:
            score_file.write(json.dumps(score_data))
        print("Congratulations!, you guessed the number in " + str(attempts) + " attempts")
        break
    elif guess > secret:
        print("Sorry, you guessed too high! try lower")
    elif guess < secret:
        print("Sorry, you guessed too low! try higher")


