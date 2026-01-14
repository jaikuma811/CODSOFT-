import random

def playgame():
    # Initialize scores
    userscore = 0
    computerscore = 0
    options = ["rock", "paper", "scissors"]

    print("--- Welcome to Rock, Paper, Scissors! ---")
    print("Instructions: Type 'rock', 'paper', or 'scissors' to play.")
    print("Type 'quit' at any time to end the game.")

    while True:
        print(f"\nScore -> You: {userscore} | Computer: {computerscore}")
        
        # User Input
        cho = input("Enter your choice: ").lower()

        if cho == "quit":
            break
        
        if cho not in options:
            print("Invalid input. Please try again.")
            continue

        # Computer Selection
        computerchoice = random.choice(options)
        print(f"Computer chose: {computerchoice}")

        # Game Logic
        if cho == computerchoice:
            print(f"Both players selected {cho}. It's a tie!")
        elif cho == "rock":
            if computerchoice == "scissors":
                print("Rock smashes scissors! You win!")
                userscore += 1
            else:
                print("Paper covers rock! You lose.")
                computerscore += 1
        elif cho == "paper":
            if computerchoice == "rock":
                print("Paper covers rock! You win!")
                userscore += 1
            else:
                print("Scissors cuts paper! You lose.")
                computerscore += 1
        elif cho == "scissors":
            if computerchoice == "paper":
                print("Scissors cuts paper! You win!")
                userscore += 1
            else:
                print("Rock smashes scissors! You lose.")
                computerscore += 1

        # Play Again logic is handled by the loop, 
        # but we can add an explicit prompt:
        playagain = input("\nPlay another round? (yes/no): ").lower()
        if playagain != 'yes':
            break

    print("\n--- Final Results ---")
    print(f"Final Score -> You: {userscore} | Computer: {computerscore}")
    print("Thanks for playing!")

if __name__ == "__main__":
    playgame()