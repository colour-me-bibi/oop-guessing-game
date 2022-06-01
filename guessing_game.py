

import random
from dataclasses import dataclass


# @dataclass
# class GuessingGame:
#     low: int = 1
#     high: int = 100

#     def play(self, answer=None):
#         if answer is None:
#             answer = random.randint(self.low, self.high)

#         while True:
#             guess = input(f"Guess a number between {self.low} and {self.high}: ")

#             try:
#                 number = int(guess)
#             except ValueError:
#                 print("Please enter a number.")
#                 continue

#             if number < self.answer:
#                 print("Too low!")
#             elif number > self.answer:
#                 print("Too high!")
#             else:
#                 break

#         print(f"You guessed it! The answer was {answer}!")


@dataclass
class GuessingGame:
    answer: int
    low: int = 1
    high: int = 100

    def __post_init__(self):
        self.is_solved = False

    def guess(self, number: int) -> str:
        if number < self.answer:
            return "Too low!"

        if number > self.answer:
            return "Too high!"

        self.is_solved = True
        return "You guessed it!"

    def solved(self) -> bool:
        return self.is_solved

    def play(self):
        while not self.is_solved:
            guess = input(f"Guess a number between {self.low} and {self.high}: ")

            try:
                number = int(guess)
            except ValueError:
                print("Please enter a number.")
                continue

            print(self.guess(number))


def main():
    game = GuessingGame(random.randint(1, 100))
    game.play()


if __name__ == "__main__":
    main()
