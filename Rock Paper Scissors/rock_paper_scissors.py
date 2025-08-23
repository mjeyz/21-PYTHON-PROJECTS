import random

options = ["rock", "paper", "scissors"]
user_wins = 0
computer_wins = 0

try:
    while True:
        user_choice = input("Enter rock, paper, or scissors (or 'quit' to exit): ").lower()
        if user_choice == 'quit':
            print("Thanks for playing!")
            break
        if user_choice not in options:
            print("Invalid choice. Please try again.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif user_choice == "rock" and computer_choice == "scissors":
            print("You win!")
            user_wins += 1
        elif user_choice == "paper" and computer_choice == "rock":
            print("You win!")
            user_wins += 1
        elif user_choice == "scissors" and computer_choice == "paper":
            print("You win!")
            user_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
        print(f"Score - You: {user_wins}, Computer: {computer_wins}")

except TypeError:
    print("An error occurred. Please check your input and try again.")
else:
    print("Game ended successfully.")
finally:
    print("Final Score - You: {}, Computer: {}".format(user_wins, computer_wins))
    print("Thank you for playing!")