import random

def rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    user_score = 0
    computer_score = 0

    print("=== Welcome to Rock, Paper, Scissors! ===")
    print("Type 'exit' to quit the game.\n")

    while True:
        user_choice = input("Choose Rock, Paper, or Scissors: ").lower().strip()
        
        if user_choice == "exit":
            print("\nGame Over!")
            print(f"Final Score -> You: {user_score} | Computer: {computer_score}")
            break

        if user_choice not in options:
            print("Invalid choice! Please type 'rock', 'paper', or 'scissors'.")
            continue

        computer_choice = random.choice(options)
        print(f"Computer chose: {computer_choice.capitalize()}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win this round! 🏆")
            user_score += 1
        else:
            print("Computer wins this round! 🤖")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}\n" + "-"*30)

if __name__ == "__main__":
    rock_paper_scissors()
