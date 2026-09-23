import random

def number_guessing_game():
    target_number = random.randint(1, 100)
    attempts_left = 7
    
    print("=== Welcome to the Number Guessing Game! ===")
    print("I have chosen a number between 1 and 100. You have 7 attempts.\n")

    while attempts_left > 0:
        try:
            user_guess = int(input(f"Your Guess (Attempts left: {attempts_left}): "))
        except ValueError:
            print("Please enter a valid integer!")
            continue

        if user_guess == target_number:
            print(f"Congratulations! You guessed the correct number: {target_number} 🎉")
            break
        elif user_guess < target_number:
            print("Guess HIGHER ⬆️")
        else:
            print("Guess LOWER ⬇️")

        attempts_left -= 1

    if attempts_left == 0:
        print(f"\nGame Over! The target number was: {target_number}")

if __name__ == "__main__":
    number_guessing_game()
