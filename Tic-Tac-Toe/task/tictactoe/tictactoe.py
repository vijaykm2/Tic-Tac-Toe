# write your code here
# print("Enter letters:")

xcount = 0
ocount = 0


def printTicTacToe():
    global i, j
    xcount = 0
    ocount = 0
    print("---------")
    for i in ticTacToeMatrix:
        print("|", end=" ")
        for j in i:
            if j == "O":
                ocount += 1
            elif j == "X":
                xcount += 1
            print(j, end=" ")
        print("|")
    print("---------")
    return ocount, xcount


letters = "         "
row1 = list(letters[0:3])
row2 = list(letters[3:6])
row3 = list(letters[6:9])
ticTacToeMatrix = [row1, row2, row3]


ocount, xcount = printTicTacToe()
diff = xcount - ocount
if diff < -1 or diff > 1:
    print("Impossible")
    exit(0)
xwins = False
owins = False


def check_game_state():
    global i, j, xwins, owins
    for i in range(0, 3):
        for j in range(0, 3):
            if j == 1:
                if ticTacToeMatrix[i][j - 1] == ticTacToeMatrix[i][j] and ticTacToeMatrix[i][j] == ticTacToeMatrix[i][
                    j + 1]:
                    if ticTacToeMatrix[i][j] == "X":
                        xwins = True
                    elif ticTacToeMatrix[i][j] == "O":
                        owins = True
            if i == 1:
                if ticTacToeMatrix[i - 1][j] == ticTacToeMatrix[i][j] and ticTacToeMatrix[i][j] == \
                        ticTacToeMatrix[i + 1][j]:
                    if ticTacToeMatrix[i][j] == "X":
                        xwins = True
                    elif ticTacToeMatrix[i][j] == "O":
                        owins = True
                if j == 1 and ticTacToeMatrix[i - 1][j - 1] == ticTacToeMatrix[i][j] and ticTacToeMatrix[i][j] == \
                        ticTacToeMatrix[i + 1][j + 1]:
                    if ticTacToeMatrix[i][j] == "X":
                        xwins = True
                    elif ticTacToeMatrix[i][j] == "O":
                        owins = True
                if j == 1 and ticTacToeMatrix[i - 1][j + 1] == ticTacToeMatrix[i][j] and ticTacToeMatrix[i][j] == \
                        ticTacToeMatrix[i + 1][j - 1]:
                    if ticTacToeMatrix[i][j] == "X":
                        xwins = True
                    elif ticTacToeMatrix[i][j] == "O":
                        owins = True
            if i == 2 and j == 2 and xwins == False and owins == False:
                letters2 = ''.join(row1)+''.join(row2)+''.join(row3)
                if " " in letters2:
                    print("Game not finished")
                else:
                    printTicTacToe()
                    print("Draw")

                    exit(0)


# check_game_state()

if xwins == True and owins == True:
    print("Impossible")
elif xwins == True:
    print("X wins")
elif owins == True:
    print("O wins")
enterCoords = True
letter = "X"
while enterCoords:
    print("Enter the coordinates: > ")
    coords = input()
    coords = coords.split(" ")
    isDig = True
    for i in coords:
        if not i.isdigit():
            isDig = False

    if not isDig:
        print("You should enter numbers!")

    columnInd = int(coords[0]) - 1

    rowInd = int(coords[1])
    if columnInd < 0 or columnInd > 2 or rowInd < 1 or rowInd > 3:
        print("Coordinates should be from 1 to 3!")
        continue
    row = ''
    if (rowInd == 1):
        row = row3
    elif (rowInd == 2):
        row = row2
    elif (rowInd == 3):
        row = row1

    element = row[columnInd]
    if (element == " "):
        # row = row[:columnInd]+'X'+row[columnInd+
        row[columnInd] = letter
        check_game_state()
        if letter == "X":
            letter = "O"
        else:
            letter = "X"
        if xwins == True and owins == True:
            printTicTacToe()
            print("Impossible")
            exit(0)
        elif xwins == True:
            printTicTacToe()
            print("X wins")
            exit(0)
        elif owins == True:
            printTicTacToe()
            print("O wins")
            exit(0)
        else:
            printTicTacToe()
    else:
        print("This cell is occupied! Choose another one!")

printTicTacToe()
