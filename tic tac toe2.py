# Tic Tac Toe - a simple game in Python
# Play with a friend or against the computer.

import random

# All 8 ways to win: 3 rows, 3 columns and 2 diagonals
WINNING_LINES = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6],
]
def print_board(board):
    """Show the board. Empty spots show their number (1-9)."""
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---+---+---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---+---+---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()
def is_free(board, position):
    """A spot is free if it does not have X or O in it."""
    return board[position] not in ("X", "O")
def check_winner(board, player):
    """"Return True if the player has 3 in a row."""
    for line in WINNING_LINES:
        if board[line[0]] == board[line[1]] == board[line[2]] == player:
            return True
    return False
def is_draw(board):
    """The game is a draw when no spot is free."""
    for position in range(9):
        if is_free(board, position):
            return False
    return True
def get_player_move(board, player):
    """Ask the player for a position until they enter a valid one."""
    while True:
        choice = input("Player " + player + ", choose a position (1-9): ")

        if not choice.isdigit():
            print("Please type a number from 1 to 9.")
            continue

        position = int(choice) - 1  

        if position < 0 or position > 8:
            print("Please type a number from 1 to 9.")
        elif not is_free(board, position):
            print("That spot is already taken. Try another one.")
        else:
            return position


def find_winning_move(board, player):
    """Return a position that would win the game for player, or None."""
    for position in range(9):
        if is_free(board, position):
            test_board = board.copy()
            test_board[position] = player
            if check_winner(test_board, player):
                return position
    return None


def get_computer_move(board):
    """Simple computer player (always plays O)."""
    # Win if possible
    move = find_winning_move(board, "O")
    if move is not None:
        return move

    # Block the human if they are about to win
    move = find_winning_move(board, "X")
    if move is not None:
        return move

    # Take the centre if it is free
    if is_free(board, 4):
        return 4

    # Otherwise pick any free spot at random
    free_spots = [p for p in range(9) if is_free(board, p)]
    return random.choice(free_spots)


def play_game(vs_computer):
    """Play one round. Returns 'X', 'O' or 'Draw'."""
    board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    current_player = "X"

    while True:
        print_board(board)

        if vs_computer and current_player == "O":
            position = get_computer_move(board)
            print("Computer chooses position", position + 1)
        else:
            position = get_player_move(board, current_player)

        board[position] = current_player

        if check_winner(board, current_player):
            print_board(board)
            if vs_computer and current_player == "O":
                print("The computer wins!")
            else:
                print("Player " + current_player + " wins!")
            return current_player

        if is_draw(board):
            print_board(board)
            print("It's a draw!")
            return "Draw"

        if current_player == "X":
            current_player = "O"
        else:
            current_player = "X"
def choose_mode():
    """Ask whether to play against a friend or the computer."""
    print("Choose a game mode:")
    print("  1. Two players")
    print("  2. Play against the computer")
    while True:
        choice = input("Enter 1 or 2: ")
        if choice == "1":
            return False
        if choice == "2":
            return True
        print("Please enter 1 or 2.")
def main():
    print("==============================")
    print("     Welcome to Tic Tac Toe")
    print("==============================")
    print("Get 3 in a row to win!")
    print()

    vs_computer = choose_mode()
    scores = {"X": 0, "O": 0, "Draw": 0}
    while True:
        result = play_game(vs_computer)
        scores[result] += 1

        print()
        print("Score -> X:", scores["X"], "| O:", scores["O"], "| Draws:", scores["Draw"])

        again = input("Play again? (y/n): ")
        if again != "y":
            break
    print("Thanks for playing!")

main()

