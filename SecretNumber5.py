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
Result.attempts = 0

with open("score_sheet.json" , "r") as data_file:
    score_data_d = json.load(data_file)
    score_data = [Result(data["name"],data["attempts"], data["wrong"], data["time"], data["guessed_number"]) for data in score_data_d]
    print(score_data)

for obj in score_data:
    print(vars(obj))
