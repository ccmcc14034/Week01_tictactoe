# My TicTacToe game

import random

# Introduce Program
print ("Welcome to a Game of Tic-Tac-Toe")
print()

# Create Board
game_board = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True

# Draw Out The Board
def drawBoard(game_board): 
    print(game_board [0] + "|" + game_board [1] + "|" + game_board [2] )
    print("------")
    print(game_board [3] + "|" + game_board [4] + "|" + game_board [5] )
    print("------")
    print(game_board [6] + "|" + game_board [7] + "|" + game_board [8] )

# Take User Input
def userInput(game_board):
    choice = int(input("Enter a number 1-9: "))
    if game_board[choice-1] == "-":
        game_board[choice-1] = currentPlayer
    else:
        print("Sorry!That spot is already taken!")
        switchPlayer()

# Check For Horizontal Win
def horizontalWin(game_board):
    global winner
    if game_board[0] == game_board[1] == game_board[2] and game_board[0] != "-":
        winner = game_board[0]
        return True
    elif  game_board[3] == game_board[4] == game_board[5] and game_board[3] != "-":
        winner = game_board[3]
        return True
    elif  game_board[6] == game_board[7] == game_board[8] and game_board[6] != "-":
        winner = game_board[6]
        return True

# Check for Row Win
def rowWin(game_board):
    global winner
    if game_board[0] == game_board[3] == game_board[6] and game_board[0] != "-":
        winner = game_board[0]
        return True
    elif  game_board[1] == game_board[4] == game_board[7] and game_board[3] != "-":
        winner = game_board[1]
        return True
    elif  game_board[2] == game_board[5] == game_board[8] and game_board[6] != "-":
        winner = game_board[2]
        return True

# Check for Diagonal Win
def diagWin(game_board):
    global winner
    if game_board[0] == game_board[4] == game_board[8] and game_board[0] != "-":
        winner = game_board[0]
        return True
    elif  game_board[2] == game_board[4] == game_board[6] and game_board[3] != "-":
        winner = game_board[2]
        return True

# Check for a Tie
def tieWin(game_board):
    global gameRunning
    if "-" not in game_board:
        drawBoard(game_board)
        print("Good Game, It is a tie!")
        gameRunning = False

# Switch between players
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"

# Check for Win
def checkWin():
    global gameRunning
    if horizontalWin(game_board):
        drawBoard(game_board)
        print(f"The winner is {winner}!")
        gameRunning = False

    elif rowWin(game_board):
        drawBoard(game_board)
        print(f"The winner is {winner}!")
        gameRunning = False
        
    elif diagWin(game_board):
        drawBoard(game_board)
        print(f"The winner is {winner}!")
        gameRunning = False
   

# Computer player
def compPlayer(game_board):
    while currentPlayer == "O":
        spot = random.randint(0,8)
        if game_board[spot] == "-":
            game_board[spot] = "O"
            switchPlayer()


# Call Program 
while gameRunning:
    drawBoard(game_board)
    if winner != None:
        break
    userInput(game_board)
    checkWin()
    tieWin(game_board)
    switchPlayer()
    compPlayer(game_board)
    checkWin()
    tieWin(game_board)