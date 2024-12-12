import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100. Can you guess it?")

    while not guessed:
        try:
            # Get user input
            user_guess = int(input("Enter your guess: "))
            attempts += 1

            # Check the user's guess
            if user_guess < 1 or user_guess > 100:
                print("Please guess a number between 1 and 100.")
            elif user_guess < random_number:
                print("Higher! Try again.")
            elif user_guess > random_number:
                print("Lower! Try again.")
            else:
                guessed = True
                print(f"Congratulations! You've guessed the number {random_number} in {attempts} attempts.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

if __name__ == "__main__":
    number_guessing_game()