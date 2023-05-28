### Fully working, but may return to make method/style improvements
### Simulates a game of Tic-tac-toe using text
### Author: Andrew LeMay

def main():
    playAgain = 'y'
    while playAgain.lower() == "y":
        # Resets board for each game
        board = createBoard()

        # Initialize the players and valid turns. First player is X
        players = ['X', 'O']
        validMoves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        turn = 0
        player = players[0]

        gameOver = False
        # Show beginning board
        printBoard(board)
        while not gameOver:
            # Get moves from players
            move = input(f"Player {player} input the number for your move: ")
            # Check if desired move is valid and if available, removes it from list of valid moves if it is
            while move not in validMoves:
                move = input(f"That is not a valid move, Player {player} please input a valid move: ")
            validMoves.remove(move)

            # Makes the move, gets the resulting board, and checks if the game is done
            board = makeMove(board, player, move)
            turn += 1
            print()
            printBoard(board)
            gameOver = isGameOver(board, turn)
            # Switches to next player
            player = players[turn%2]
        print(gameOver)
        playAgain = input("Would you like to play again? (y/n): ")
        print()

# Creates board
def createBoard():
    return [[' ', '1', ' ', '|', ' ', '2', ' ', '|', ' ', '3', ' '],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        [' ', '4', ' ', '|', ' ', '5', ' ', '|', ' ', '6', ' '],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        [' ', '7', ' ', '|', ' ', '8', ' ', '|', ' ', '9', ' ']]

# Cleanly prints the current board
def printBoard(board):
    for i in board:
        print("".join(i))

# Checks all combinations of wins or if the game is a draw
def isGameOver(board, turn):
    if turn <= 4:
        return False
    elif board[0][1] == board[0][5] == board[0][9]:
        return f"{board[0][1]} wins!"
    elif board[2][1] == board[2][5] == board[2][9]:
        return f"{board[2][1]} wins!"
    elif board[4][1] == board[4][5] == board[4][9]:
        return f"{board[4][1]} wins!"
    elif board[0][1] == board[2][1] == board[4][1]:
        return f"{board[0][1]} wins!"
    elif board[0][5] == board[2][5] == board[4][5]:
        return f"{board[0][5]} wins!"
    elif board[0][9] == board[2][9] == board[4][9]:
        return f"{board[0][9]} wins!"
    elif board[0][1] == board[2][5] == board[4][9]:
        return f"{board[0][1]} wins!"
    elif board[0][9] == board[2][5] == board[4][1]:
        return f"{board[0][9]} wins!"
    elif turn == 9:
        return "The game is a draw"
    else:
        return False

# Makes the move by replacing the number with the player's letter (does not check if valid)
def makeMove(board, player, move):
    match move:
        case '1':
            board[0][1] = player
            return board
        case '2':
            board[0][5] = player
            return board
        case '3':
            board[0][9] = player
            return board
        case '4':
            board[2][1] = player
            return board
        case '5':
            board[2][5] = player
            return board
        case '6':
            board[2][9] = player
            return board
        case '7':
            board[4][1] = player
            return board
        case '8':
            board[4][5] = player
            return board
        case '9':
            board[4][9] = player
            return board

if __name__ == "__main__":
    main()