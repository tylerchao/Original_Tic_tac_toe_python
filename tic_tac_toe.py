current_player = "o"
gameRunning = True
winner = None

board  = ["-", "-","-",
          "-", "-","-",
          "-", "-","-"]


def print_board():
    print(board[0]+ " | " + board[1]+ " | "+ board[2])
    print(board[3]+ " | " + board[4]+ " | "+ board[5])
    print(board[6]+ " | " + board[7]+ " | "+ board[8])

def player_input():
    choice = int(input("player one turn : "))
    if choice >=1 and choice <= 9 and board[choice-1] == "-":
        board[choice-1]= current_player
    else: 
        print("choose another option !!!!")
        player_input()


def check_row(board):
    global winner
    if board[0] == board[1] == board[2]and board[0]!= "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5]and board[3]!= "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8]and board[6]!= "-":
        winner = board[6]
        return True

def check_column(board):
    global winner
    if board[0] == board[3] == board[6] and board[0]!= "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7]and board[1]!= "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8]and board[2]!= "-":
        winner = board[2]
        return True

def check_diagno(board):
    global winner
    if board[0] == board[4] == board[8] and board[0]!= "-":
        winner = board[4]
        return True
    elif board[2] == board[4] == board[6]and board[2]!= "-":
        winner = board[4]
        return True

def check_tie():
    global gameRunning
    if "-" not in board:
        print_board()
        print("It is a tie !!!")
        gameRunning = False

def check_win():
    global gameRunning
    if check_row(board) or check_column(board) or check_diagno(board):
        print(f"The winner is : {winner}" )
        gameRunning = False


def switch_player():
    global current_player
    if current_player == "o":
        current_player = "x"
    elif current_player == "x":
        current_player = "o"


if __name__ == "__main__":
    while(gameRunning):
        print_board()
        player_input()
        check_win()
        check_tie()
        switch_player()