import os

def printstr(gameValues):
    print(f" {gameValues[0]} | {gameValues[1]} | {gameValues[2]} ")
    print(f"---|---|---")
    print(f" {gameValues[3]} | {gameValues[4]} | {gameValues[5]} ")
    print(f"---|---|---")
    print(f" {gameValues[6]} | {gameValues[7]} | {gameValues[8]} ")

def Winornot(gameValues):
    # Possible win cases
    wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for win in wins:
        # if gameValues matches with the pattern and has X then X won the Match
        if(gameValues[win[0]] == gameValues[win[1]] == gameValues[win[2]] == 'X'):
            printstr(gameValues)
            print("X Won the match")
            return 1

        # if gameValues matches with the pattern and has X then O won the Match
        if(gameValues[win[0]] == gameValues[win[1]] == gameValues[win[2]] == 'O'):
            printstr(gameValues)
            print("O Won the match")
            return 0

        # if all places are filled and no one is the winner
        if all(isinstance(item, str) for item in gameValues):
            printstr(gameValues)
            return -2
    # if no one wins then
    return -1

if __name__ == '__main__':
    print("Welcome to the Game")
    gameValues=[0, 1, 2, 3, 4, 5, 6, 7, 8]
    chance = 1

    while(True):
        try:
            if chance == 1:
                printstr(gameValues)
                print("\nX's Chance")
                value = int(input("\nPlease enter a value: "))

                # check if already filled with O
                if gameValues[value]!= 'O':
                    gameValues[value] = 'X'
                else:
                    os.system('CLS')
                    print("\nPlease Enter Different Location for X")
                    continue
                os.system('CLS')

            if chance == 0:
                printstr(gameValues)
                print("\nZ's Chance")
                value = int(input("\nPlease enter a value: "))

                # check if already filled with X
                if gameValues[value]!= 'X':
                    gameValues[value] = 'O'
                else:
                    os.system('CLS')
                    print("\nPlease Enter Different Location for O")
                    continue
                os.system('CLS')

        except IndexError:
            # exception if Value is not between 0 to 8 
            os.system('CLS')
            print("\nPlease Enter value from 0 - 8\n")
            continue

        # for giving chance to other player
        chance = 1 - chance
        cwin = winornot(gameValues)
        if(cwin == -2):
            print("Game Drawn")
            break
        if(cwin != -1):
            print("Match is over")
            break
