import json

def load():
    with open("Score_sheet.json", "r") as score_file:
        score_data = json.loads(score_file.read())
        return score_data

def save(sd):
    with open("Score_sheet.json", "w") as score_file:
        score_file.write(json.dumps(sd))

def printscore(x,d):
    if x == 0:
        print("all scores: " + str(d))
    elif x == 1:
        print("Congratulations!, you guessed the number in " + str(d) + " attempts")
    else:
        sorted_score_data = sorted(d, key=lambda a: a["attempts"])[:x]
        for score_dict in sorted_score_data:
            print("Name: " + score_dict["name"] + ", attempts: " + str(score_dict["attempts"]) + ", wrong guess: " + str(
                score_dict["wrong"]) + ", time: " + str(score_dict["time"]) + ", guessed number " + str(
                score_dict["guessed_number"]))

