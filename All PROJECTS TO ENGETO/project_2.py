"""
projekt_2.py: první projekt do Engeto Online Python Akademie
author: Adam Kušnir
email: adamkushnir@outlook.cz
discord: Adam K. ASYPRO_AK#2480
"""
#Hraci polePřivitani a pravidla
print("Welcome to Tic Tac Toe")

dash = "="
print ((dash)* 46)
print("""
GAME RULES:
Each player can place one mark
per turn on the 3x3 grid. The WINNER is
who succeeds in placing three of their
marks in a:
* horizontal,
* vertical or
* diagonal row
Board:
 1 | 2 | 3
 4 | 5 | 6
 7 | 8 | 9
""")

#Hraci pole
Board = ['-','-','-',
         '-','-','-',
         '-','-','-']

#Proměne
GameGoing = True
winner = None
Player = "X"

#Vyprinti nase pole
def BoardPrint():
    print(Board[0] + ' | ' + Board[1] + ' | ' + Board[2])
    print(Board[3] + ' | ' + Board[4] + ' | ' + Board[5])
    print(Board[6] + ' | ' + Board[7] + ' | ' + Board[8])

def Tic_Tac_toe():

    BoardPrint()

    while GameGoing:
        BoardPosition(Player)
        
        check_Game_Going()
        
        SWAP_player()
    
    if winner == "X" or winner == "O":
        print(dash*46)
        print(f"Congratulations, the {winner} WON!")
        print(dash*46)
    elif winner == None:
        print(dash*46)
        print("OH NO, IT IS DRAW U CAN TRY AGAIN.")
        print(dash*46)


#Pozice na poli a jeji proverka
def BoardPosition(player):

    Positions = (input(f"Player {player}| Please enter your move number 1-9: "))
    print(dash*46)

    Check = False
    while not Check:
        while Positions not in ["1","2","3","4","5","6","7","8","9"]:
            Positions = input("Invalid input. Choose a position from 1-9 ")
        Positions = int(Positions) - 1

        if Board[Positions] =='-':
            Check = True
        else:
            print("U can't go there. TRY AGAIN!")

    Board[Positions] = player

    BoardPrint()
    print("""
1 | 2 | 3
4 | 5 | 6
7 | 8 | 9
 """)

# proverka jestli hra bezi
def check_Game_Going():
    chech_WINNER()
    check_DRAW()

# proverka na vyherce
def chech_WINNER():
    
    global winner

    VerticalWinner = check_Vertical()
    HorizontalWinner = check_Horizontal()
    DiagonalsWinner = check_Diagonals()

    if HorizontalWinner:
        winner = HorizontalWinner
    elif VerticalWinner:
        winner = VerticalWinner
    elif DiagonalsWinner:
        winner = DiagonalsWinner
    else:
        winner = None
    return

# Prověrka vertikalnich sloupcu
def check_Vertical():
    
    global GameGoing
    
    Vertical1 = Board[0] == Board[3] == Board[6] != "-"
    Vertical2 = Board[1] == Board[4] == Board[7] != "-"
    Vertical3 = Board[2] == Board[5] == Board[8] != "-"

    #Proverak jestli jo Sloupec se stejnym znakem nebo prazny
    if Vertical1 or Vertical2 or Vertical3:
        GameGoing = False

    if Vertical1:
        return Board[0]
    elif Vertical2:
        return Board[1]
    elif Vertical3:
        return Board[2]
    return

# Prověrka horizontalnich sloupcu
def check_Horizontal():
    
    global GameGoing

    Horizontal1 = Board[0] == Board[1] == Board[2] != "-"
    Horizontal2 = Board[3] == Board[4] == Board[5] != "-"
    Horizontal3 = Board[6] == Board[7] == Board[8] != "-"

    if Horizontal1 or Horizontal2 or Horizontal3:
        GameGoing = False

    if Horizontal1:
        return Board[0]
    elif Horizontal2:
        return Board[3]
    elif Horizontal3:
        return Board[6]
    return

# Prověrka Diagonalnich sloupcu
def check_Diagonals():
    
    global GameGoing
    Diagonal1 = Board[0] == Board[4] == Board[8] != "-"
    Diagonal2 = Board[6] == Board[4] == Board[2] != "-"

    if Diagonal1 or Diagonal2:
        GameGoing = False
    
    if Diagonal1:
        return Board[0]
    elif Diagonal2:
        return Board[6]
    return

# Funkce pro proverku remizy
def check_DRAW():
    global GameGoing
    if "-" not in Board:
        GameGoing = False
    return

# Funkce pro meneni X na O
def SWAP_player():
    global Player
    if Player == "X":
        Player = "O"
    elif Player == "O":
        Player = "X"
    return

Tic_Tac_toe()