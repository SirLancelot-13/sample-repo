def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != " ":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return board[0][2]

    return None

def tic_tac_toe():
    print("Welcome to Tic Tac Toe!")
    board = [[" " for _ in range(3)] for _ in range(3)]
    player_turn = "X"

    for _ in range(9):
        print_board(board)
        print(f"Player {player_turn}'s turn.")
        try:
            row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
            if board[row][col] != " ":
                print("Cell already taken. Try again.")
                continue
            board[row][col] = player_turn
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                return
            player_turn = "O" if player_turn == "X" else "X"
        except (ValueError, IndexError):
            print("Invalid input. Try again.")

    print_board(board)
    print("It's a draw!")

if __name__ == "__main__":
    tic_tac_toe()