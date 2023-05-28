## Fully working, but may return to make method/style improvements
def main():
    playAgain = 'y'
    while playAgain.lower() == "y":
        board = createBoard()
        players = ['X', 'O']
        validMoves = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        turn = 0
        player = players[0]
        gameOver = False
        printBoard(board)
        while not gameOver:
            move = input(f"Player {player} input the number for your move: ")
            while move not in validMoves:
                move = input(f"That is not a valid move, Player {player} please input a valid move: ")
            validMoves.remove(move)
            board = makeMove(board, player, move)
            turn += 1
            print()
            printBoard(board)
            gameOver = isGameOver(board, turn)
            player = players[turn%2]
        print(gameOver)
        playAgain = input("Would you like to play again? (y/n): ")
        print()

def createBoard():
    return [[' ', '1', ' ', '|', ' ', '2', ' ', '|', ' ', '3', ' '],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        [' ', '4', ' ', '|', ' ', '5', ' ', '|', ' ', '6', ' '],
        ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_'],
        [' ', '7', ' ', '|', ' ', '8', ' ', '|', ' ', '9', ' ']]

def printBoard(board):
    for i in board:
        print("".join(i))

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