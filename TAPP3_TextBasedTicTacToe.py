def createBoard():
    return [[" ", 1, " ", "|", " ", 2, " ", "|", " ", 3, " "],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
        [" ", 4, " ", "|", " ", 5, " ", "|", " ", 6, " "],
        ["_", "_", "_", "_", "_", "_", "_", "_", "_", "_", "_"],
        [" ", 7, " ", "|", " ", 8, " ", "|", " ", 9, " "]]

playAgain = True
while playAgain:
    board = createBoard()

    print("Here is the board:")
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end="")
        print("\n")
    print("The player playing X starts.")
    player = 'X'
    
    end = "z"
    while end == "":

        invalidMove = True
        while(invalidMove):
            move = input(f"Player \"{player}\" please type in the number of the space for your move.")
            for i in range(len(board[0])):
                break

        if not invalidMove:
            if board[0][1] == board[0][5] == board[0][9]:
                end = board[0][1]
            elif board[2][1] == board[2][5] == board[2][9]:
                end = board[2][1]
            elif board[4][1] == board[4][5] == board[4][9]:
                end = board[4][1]
            elif board[0][1] == board[2][1] == board[4][1]:
                end = board[0][1]
            elif board[0][5] == board[2][5] == board[4][5]:
                end = board[0][5]
            elif board[0][9] == board[2][9] == board[4][9]:
                end = board[0][9]
            elif board[0][1] == board[2][5] == board[4][9]:
                end = board[0][1]
            elif board[4][1] == board[2][5] == board[0][9]:
                end = board[4][1]

    playAgain = False