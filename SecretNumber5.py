import random
import datetime
import json

class result:
    def __init__(self, name, attempts, wrong, time, guessed_number):
        self.name =name
        self.attempts = attempts
        self.wrong = wrong
        self.time = time
        self.guessed_number = guessed_number

