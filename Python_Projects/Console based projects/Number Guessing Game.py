import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I have chosen a number between 1 and 100.")
    print("Your task is to guess the number!")
    
    # Generate a random number
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 10  # Maximum number of attempts allowed

    while attempts < max_attempts:
        try:
            guess = int(input(f"Attempt {attempts + 1}/{max_attempts}: Enter your guess: "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue
        
        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break
    else:
        print(f"Sorry, you've used all {max_attempts} attempts. The number was {secret_number}. Better luck next time!")

# Start the game
number_guessing_game()
