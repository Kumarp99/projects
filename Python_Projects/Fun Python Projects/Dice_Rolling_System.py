import random

def roll_dice():
    print("Welcome to the Dice Rolling Simulator!")
    while True:
        sides = input("Enter the number of sides for the dice (e.g., 6 for a standard dice): ")
        try:
            sides = int(sides)
            if sides < 2:
                print("A dice must have at least 2 sides. Try again.")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        dice_roll = random.randint(1, sides)
        print(f"\nYou rolled a {dice_roll}!")
        
        roll_again = input("Do you want to roll the dice again? (yes/no): ").lower()
        if roll_again not in ('yes', 'y'):
            print("Thanks for using the Dice Rolling Simulator! Goodbye!")
            break

# Start the dice rolling simulator
roll_dice()
