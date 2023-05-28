### I created text based tic-tac-toe, I play chess almost every day, so why not?
### This would be a lot easier in a different language but who cares?
### Author: Andrew LeMay

def main():
    fileConversions = {'a':0, 'b':1, 'c':2, 'd':3, 'e':4, 'f':5, 'g':6, 'h':7}
    board = makeBoard()
    realBoard = makeRealBoard()
    printBoard(board)

def makeBoard():
    return[['_', '_', '__', '_', "_", '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_'],
           ['|', ' ', 'BR', ' ', "|", ' ', 'BN', ' ', '|', ' ', 'BB', ' ', '|', ' ', 'BQ', ' ', '|', ' ', 'BK', ' ', '|', ' ', 'BB', ' ', '|', ' ', 'BN', ' ', '|', ' ', 'BR', ' ', '|'],
           ['_', '_', '__', '_', "_", '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_'],
           ['|', ' ', 'Bp', ' ', "|", ' ', 'Bp', ' ', '|', ' ', 'Bp', ' ', '|', ' ', 'Bp', ' ', '|', ' ', 'Bp', ' ', '|', ' ', 'Bp', ' ', '|', ' ', 'Bp', ' ', '|', ' ', 'Bp', ' ', '|'],
           ['_', '_', '__', '_', "_", '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_'],
           ['|', ' ', '  ', ' ', "|", ' ', '  ', ' ', '|', ' ', '  ', ' ', '|', ' ', '  ', ' ', '|', ' ', '  ', ' ', '|', ' ', '  ', ' ', '|', ' ', '  ', ' ', '|', ' ', '  ', ' ', '|'],
           ['_', '_', '__', '_', "_", '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_'],
           ['|', ' ', '  ', ' ', "|", ' ', '  ', ' ', '|', ' ', '  ', ' ', '|', ' ', '  ', ' ', '|', ' ', '  ', ' ', '|', ' ', '  ', ' ', '|', ' ', '  ', ' ', '|', ' ', '  ', ' ', '|'],
           ['_', '_', '__', '_', "_", '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_'],
           ['|', ' ', '  ', ' ', "|", ' ', '  ', ' ', '|', ' ', '  ', ' ', '|', ' ', '  ', ' ', '|', ' ', '  ', ' ', '|', ' ', '  ', ' ', '|', ' ', '  ', ' ', '|', ' ', '  ', ' ', '|'],
           ['_', '_', '__', '_', "_", '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_'],
           ['|', ' ', '  ', ' ', "|", ' ', '  ', ' ', '|', ' ', '  ', ' ', '|', ' ', '  ', ' ', '|', ' ', '  ', ' ', '|', ' ', '  ', ' ', '|', ' ', '  ', ' ', '|', ' ', '  ', ' ', '|'],
           ['_', '_', '__', '_', "_", '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_'],
           ['|', ' ', 'Wp', ' ', "|", ' ', 'Wp', ' ', '|', ' ', 'Wp', ' ', '|', ' ', 'Wp', ' ', '|', ' ', 'Wp', ' ', '|', ' ', 'Wp', ' ', '|', ' ', 'Wp', ' ', '|', ' ', 'Wp', ' ', '|'],
           ['_', '_', '__', '_', "_", '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_'],
           ['|', ' ', 'WR', ' ', "|", ' ', 'WN', ' ', '|', ' ', 'WB', ' ', '|', ' ', 'WQ', ' ', '|', ' ', 'WK', ' ', '|', ' ', 'WB', ' ', '|', ' ', 'WN', ' ', '|', ' ', 'WR', ' ', '|'],
           ['_', '_', '__', '_', "_", '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_', '_', '__', '_', '_']]

def makeRealBoard():
    return [["BR", "BN", "BB", "BQ", "BK", "BB", "BN", "BR"],
            ["Bp", "Bp", "Bp", "Bp", "Bp", "Bp", "Bp", "Bp"],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["", "", "", "", "", "", "", ""],
            ["Wp", "Wp", "Wp", "Wp", "Wp", "Wp", "Wp", "Wp"],
            ["WR", "WN", "WB", "WQ", "WK", "WB", "WN", "WR"]]

def printBoard(board):
    for i in board:
        print("".join(i))

def makeMove(board, player):
    return board

if __name__ == "__main__":
    main()