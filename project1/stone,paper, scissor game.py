import random

def play():
    choices = ["stone", "paper", "scissors"]
    while True:
        user_choice = input("Enter your choice (stone/paper/scissors or q to quit): ").lower()
        
        if user_choice == "q":
            print("Thanks for playing! Goodbye 👋")
            break
        
        if user_choice not in choices:
            print("Invalid choice! Please pick stone, paper, or scissors.")
            continue
        
        computer_choice = random.choice(choices)
        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "stone" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "stone") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win!")
        else:
            print("You lose!")

# Run the game
play()
