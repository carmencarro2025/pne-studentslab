import random

class NumberGuesser:
    def __init__(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = []

    def guess(self, number):
        if number is None:
            return "Welcome! Guess a number between 1 and 100"

        try:
            number = int(number)
        except ValueError:
            return "Please enter a valid number"

        self.attempts.append(number)
        attempts_count = len(self.attempts)

        if number == self.secret_number:
            result = f"You won after {attempts_count} attempts!"
        elif number > self.secret_number:
            result = f"Lower!"
        else:
            result = f"Higher!"
        return result
