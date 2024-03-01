from messages import print_message
import random_number

guesses = 0
number = random_number.get_random_number()

guess = int(input("Enter your guess: "))

while guess != number:
    print_message(number, guess)
    guess = int(input("Enter your guess: "))
    guesses += 1

print("\n\nCongratulations! You guessed the number in", guesses, "guesses.")