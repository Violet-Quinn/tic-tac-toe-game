def print_board(board):
    for i in range(0, 9, 3):
        print(f"{board[i]} | {board[i + 1]} | {board[i + 2]}")
        if i < 6:
            print("--+---+--")


def player_move(board, player):
    move = input(f"Player {player}, enter position (0-8): ")

    # Input validation loop
    while not move.isdigit() or int(move) < 0 or int(move) > 8 or board[int(move)] != " ":
        if not move.isdigit():
            print("Invalid input. Please enter a number.")
        else:
            move = int(move)
            if move < 0 or move > 8:
                print("Position must be between 0 and 8.")
            elif board[move] != " ":
                print("That position is already taken.")
        move = input(f"Player {player}, enter position (0-8): ")

    board[int(move)] = player


def check_win(board, player):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
        (0, 4, 8), (2, 4, 6)  # diagonals
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_conditions)


def is_tie(board):
    return " " not in board


def play_game():
    board = [" " for _ in range(9)]
    current_player = "X"

    while True:
        print_board(board)
        player_move(board, current_player)

        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        elif is_tie(board):
            print_board(board)
            print("It's a tie!")
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    play_game()

