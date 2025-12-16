import random

secret = random.randint(1,30)
attempts = 0

with open("SnumData.txt","r") as score_data:
    best_score = int(score_data.read())
    print("Best Score:" + str(best_score))
while True:
    guess = int(input("Guess a number between 1 and 30:"))
    attempts += 1

    if guess == secret:
        if attempts < best_score:
            with open("SnumData.txt","w") as score_data:
                score_data.write(str(attempts))
        print("You guessed my number in " + str(attempts) + " attempts")
        break
    elif guess > secret:
        print("You guess is not correct. try smaller number")
    elif guess < secret:
        print("You guess is not correct. try larger number")