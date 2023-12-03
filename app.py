user_wins = 0
computer_wins = 0

while True:
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    # Check if the user's choice is valid
    while user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    # Generate computer's choice
    import random
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
        user_wins += 1
    else:
        print("Computer wins!")
        computer_wins += 1
    
    # Print the choices
    print(f"Your choice: {user_choice}")
    print(f"Computer's choice: {computer_choice}")

    # Print the score
    print("Score:")
    print(f"You: {user_wins} wins")
    print(f"Computer: {computer_wins} wins")

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        break
    
# Print the final score
print("Final score:")
print(f"You: {user_wins} wins")
print(f"Computer: {computer_wins} wins")
