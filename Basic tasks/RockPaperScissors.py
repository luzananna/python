# TASK: Rock – Paper – Scissors (Python Console Game)

# Write a Python program that lets the user play Rock–Paper–Scissors against the computer.

# Requirements

# 1. The program should:
# 	•Ask the user to enter one of three choices:
# 	•"rock"
# 	•"paper"
# 	•"scissors"
# 	•Validate the input:
# 	•If the user enters something else → print
# "Invalid choice. Please enter rock, paper, or scissors."
# …and ask again (loop until correct input).

# 2. Computer choice
# 	•The computer randomly picks:
# 	•"rock", "paper", or "scissors"

# 3. Decide the winner

# Print messages like:
# 	•"You win! Paper covers rock."
# 	•"You lose! Scissors cut paper."
# 	•"It's a tie!"

# 4. Game Loop

# After each round, ask:

# Play again? (yes/no):

# 	•If yes: start another round
# 	•If no: exit program with a friendly message
# 	•If something else: ask again until valid input

# 5. optional:
# 	•Count score:
# 	•user wins
# 	•computer wins
# 	•ties
# 	•Show the score before exiting:

# Example:

# Final score — You: 2 | Computer: 3 | Ties: 1
# Thanks for playing!

import random

def get_player_choice():
    
    while True:
        choice = input("Enter rock, paper, or scissors: ").lower().strip()
        if choice in ["rock", "paper", "scissors"]:
            return choice 
        print("Invalid choice. Please enter rock, paper, or scissors.")

def computer_choice():
    return random.choice(["rock", "paper", "scissors"])   

def process(player, computer):
    
    if player == computer:
        return "tie", "It's a tie!"    

    win_conditions = [
        ("rock", "scissors"),     
        ("paper", "rock"),
        ("scissors", "paper")
    ]

    if (player, computer) in win_conditions:
        return "win", f"You win! {player} beats {computer}."
    else:
        return "lose", f"You lose! {computer} beats {player}."

def play_again():
    while True:
        answer = input("Play again? (yes/no): ").lower().strip()
        if answer in ["yes", "y"]:
            return True
        if  answer in ["no", "n"]:
            return False
        print("Please answer yes or no.")

def main():

    user_wins = 0
    computer_wins = 0
    ties = 0

    while True:
        player = get_player_choice()
        computer = computer_choice()

        print(f"You chose:      {player}")
        print(f"Computer chose: {computer}")

        result, message = process(player, computer)
        print(message)

        if result == "win":
            user_wins += 1
        elif result == "lose":
            computer_wins += 1
        else:
            ties += 1
 
        if not play_again():
            break

    print("\nFinal score — You: {user_wins} | Computer: {computer_wins} | Ties: {ties}")
    print("Thanks for playing!")


if __name__ == "__main__":
    main() 