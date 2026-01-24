import random
import datetime
import json

class Result:
    def __init__(self, name, attempts, wrong, time, guessed_number):
        self.name =name
        self.attempts = attempts
        self.wrong = wrong
        self.time = time
        self.guessed_number = guessed_number

secret = random.randint(1,30)
att = 0

with open("score_sheet.json" , "r") as data_file:
    score_data_d = json.load(data_file)
    score_data = [Result(data["name"],data["attempts"], data["wrong"], data["time"], data["guessed_number"]) for data in score_data_d]
    print(score_data)
    sorted_score_data = sorted(score_data, key=lambda o: o.attempts)
    print(sorted_score_data)
for obj in score_data:
    print(vars(obj))
for obj in sorted_score_data[:3]:
    print(vars(obj))

nm = input("Enter your name: ")
while True:
    guess = int(input("Please enter integer number between 1 and 30: "))
    att += 1
    if guess == secret:
        t = str(datetime.datetime.now())

        wr = att -1
        new_result = Result(nm, att, wr, t, guess)
        score_data.append(new_result)
        score_data_d = [score.__dict__ for score in score_data]
        with open("score_sheet.json" , "w") as data_file:
            json.dump(score_data_d, data_file)
        print("Congratulations! You scored in " + str(new_result.attempts) + " attempts!")
        break
    elif guess > secret:
        print("Sorry, you guessed too high! Try lower")
    elif guess < secret:
        print("Sorry, you guessed too low! Try higher")

