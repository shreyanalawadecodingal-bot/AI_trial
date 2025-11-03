# 🎮 Tic-Tac-Toe Game in Python

def print_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")


def check_winner(board, player):
    # All winning combinations
    wins = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ]
    for combo in wins:
        if all(board[i] == player for i in combo):
            return True
    return False


def is_draw(board):
    return all(cell != " " for cell in board)


def tic_tac_toe():
    print("🎮 Welcome to Tic-Tac-Toe!")
    board = [" "] * 9
    current_player = "X"

    print_board(board)

    while True:
        try:
            move = int(input(f"Player {current_player}, choose your move (1-9): ")) - 1
            if move < 0 or move > 8 or board[move] != " ":
                print("❌ Invalid move. Try again.")
                continue
        except ValueError:
            print("⚠️ Please enter a number between 1 and 9.")
            continue

        board[move] = current_player
        print_board(board)

        if check_winner(board, current_player):
            print(f"🏆 Player {current_player} wins!")
            break

        if is_draw(board):
            print("🤝 It's a draw!")
            break

        # Switch player
        current_player = "O" if current_player == "X" else "X"


if __name__ == "__main__":
    tic_tac_toe()
