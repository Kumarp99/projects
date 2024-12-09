def start_game():
    print("Welcome to the Text-Based Adventure Game!")
    print("You find yourself in a dark forest. There are two paths ahead:")
    print("1. Take the left path")
    print("2. Take the right path")

    choice = input("What will you do? Enter 1 or 2: ")

    if choice == "1":
        left_path()
    elif choice == "2":
        right_path()
    else:
        print("Invalid choice. Please restart the game.")
        start_game()

def left_path():
    print("\nYou chose the left path and encounter a wild wolf!")
    print("1. Fight the wolf")
    print("2. Run away")

    choice = input("What will you do? Enter 1 or 2: ")

    if choice == "1":
        print("\nYou bravely fight the wolf and emerge victorious. You find a treasure chest!")
        print("Congratulations, you're a hero!")
    elif choice == "2":
        print("\nYou run away safely but miss out on discovering the treasure.")
        print("Game Over.")
    else:
        print("Invalid choice. The wolf attacks while you hesitate!")
        print("Game Over.")

def right_path():
    print("\nYou chose the right path and come across an old bridge.")
    print("1. Cross the bridge")
    print("2. Turn back")

    choice = input("What will you do? Enter 1 or 2: ")

    if choice == "1":
        print("\nThe bridge collapses midway, but you manage to swim to safety.")
        print("You discover a hidden cave filled with gold!")
        print("Congratulations, you're rich!")
    elif choice == "2":
        print("\nYou turn back and return home safely, but with no treasure.")
        print("Game Over.")
    else:
        print("Invalid choice. You stand there indecisively until night falls.")
        print("Game Over.")

# Start the adventure
start_game()
