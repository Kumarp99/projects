def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Checks if there's a winner."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def is_full(board):
    """Checks if the board is full (a draw)."""
    for row in board:
        if " " in row:
            return False
    return True

def tic_tac_toe():
    print("Welcome to Tic-Tac-Toe!")
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print(f"\nPlayer {current_player}'s turn")
        print_board(board)
        
        try:
            row = int(input("Enter the row (0, 1, or 2): "))
            col = int(input("Enter the column (0, 1, or 2): "))
            if row not in range(3) or col not in range(3):
                print("Invalid input! Please enter numbers between 0 and 2.")
                continue
            if board[row][col] != " ":
                print("That spot is already taken! Choose another.")
                continue
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        # Place the marker
        board[row][col] = current_player

        # Check for a winner
        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"\nCongratulations! Player {winner} wins!")
            break

        # Check for a draw
        if is_full(board):
            print_board(board)
            print("\nIt's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"

# Start the game
tic_tac_toe()
