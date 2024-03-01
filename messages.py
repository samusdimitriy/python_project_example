def print_message(number, guess):
    if number == guess:
        print("Congratulations! You guessed the number.")
    elif number > guess:
        print("The number is greater than your guess.")
    else:
        print("The number is less than your guess.")

print(__name__)
