rows = int(input())


def getrow(rowNum):
    rowLength = rowNum + (rowNum - 1)
    row = ""
    for i in range(0, (rows - rowNum)):
        row += " "
    for i in range(0, rowLength):
        row += "#"
    for i in range(0, (rows - rowNum)):
        row += " "
    return row


for i in range(1, rows + 1):
    print(getrow(i))
