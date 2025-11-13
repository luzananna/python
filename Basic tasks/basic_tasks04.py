# The program should:
# 	1.	Import the random module.
# 	2.	Generate a random number from 1 to 10.
# 	3.	Ask the user to enter a number from 1 to 10.
# 	4.	Convert the user’s input to an integer.
# 	5.	Check if the input is valid:
# 	If the number is less than 1 or greater than 10 → print:
# "Invalid number. Please enter between 1 and 10."
# 	6.	If the number is valid:
# 	If the user’s guess is equal to the random number → print:
# "Correct! You guessed the number."
# 	7.	Finally, print a message:
# "Game Over!"


import random

def get_number(question):

    while True:
        value = input(question).strip()

        if value.isdigit():
            num = int(value)
            if 1 <= num <= 10:
                return num
            else:
                print("Enter a number between 1 and 10.")
        else:
            print("Please enter digits only.")


def main():
    secret = random.randint(1, 10)
    guess = get_number("Guess the number (1–10): ")

    while guess != secret:
        print("Too low!" if guess < secret else "Too high!")
        guess = get_number("Try again: ")

    print("Correct! You win!")


if __name__ == "__main__":
    main()