import numpy
import random

class Game:
    def __init__(self):
        self.board = createBoard()
        print(printBoard(self.board))
        self.board = makeMove(self.board, "N")
        print(printBoard(self.board))
        self.board = addNumber(self.board)
        print(printBoard(self.board))

def createBoard():
    board = numpy.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,])
    random2s = random.sample(range(len(board)), 2)
    for a2 in random2s:
        board[a2] = 2
    print("The board was created:")
    return board

def makeMove(board, direction):
    newBoard = False
    if direction == "N":
        newSection1 = moveSection(numpy.array([board[0],board[4],board[8],board[12]]))
        newSection2 = moveSection(numpy.array([board[1],board[5],board[9],board[13]]))
        newSection3 = moveSection(numpy.array([board[2],board[6],board[10],board[14]]))
        newSection4 = moveSection(numpy.array([board[3],board[7],board[11],board[15]]))
        newBoard = numpy.array([
            newSection1[0], newSection2[0], newSection3[0], newSection4[0],
            newSection1[1], newSection2[1], newSection3[1], newSection4[1],
            newSection1[2], newSection2[2], newSection3[2], newSection4[2],
            newSection1[3], newSection2[3], newSection3[3], newSection4[3]
            ])
    elif direction == "E":
        newSection1 = moveSection(numpy.array([board[3],board[2],board[1],board[0]]))
        newSection2 = moveSection(numpy.array([board[7],board[6],board[5],board[4]]))
        newSection3 = moveSection(numpy.array([board[11],board[10],board[9],board[8]]))
        newSection4 = moveSection(numpy.array([board[15],board[14],board[13],board[12]]))
        newBoard = numpy.array([
            newSection1[3], newSection1[2], newSection1[1], newSection1[0],
            newSection2[3], newSection2[2], newSection2[1], newSection2[0],
            newSection3[3], newSection3[2], newSection3[1], newSection3[0],
            newSection4[3], newSection4[2], newSection4[1], newSection4[0]
            ])
    elif direction == "S":
        newSection1 = moveSection(numpy.array([board[12],board[8],board[4],board[0]]))
        newSection2 = moveSection(numpy.array([board[13],board[9],board[5],board[1]]))
        newSection3 = moveSection(numpy.array([board[14],board[10],board[6],board[2]]))
        newSection4 = moveSection(numpy.array([board[15],board[11],board[7],board[3]]))
        newBoard = numpy.array([
            newSection1[3], newSection2[3], newSection3[3], newSection4[3],
            newSection1[2], newSection2[2], newSection3[2], newSection4[2],
            newSection1[1], newSection2[1], newSection3[1], newSection4[1],
            newSection1[0], newSection2[0], newSection3[0], newSection4[0]
            ])
    elif direction == "W":
        newSection1 = moveSection(numpy.array([board[0],board[1],board[2],board[3]]))
        newSection2 = moveSection(numpy.array([board[4],board[5],board[6],board[7]]))
        newSection3 = moveSection(numpy.array([board[8],board[9],board[10],board[11]]))
        newSection4 = moveSection(numpy.array([board[12],board[13],board[14],board[15]]))
        newBoard = numpy.array([
            newSection1[0], newSection1[1], newSection1[2], newSection1[3],
            newSection2[0], newSection2[1], newSection2[2], newSection2[3],
            newSection3[0], newSection3[1], newSection3[2], newSection3[3],
            newSection4[0], newSection4[1], newSection4[2], newSection4[3]
            ])

    return newBoard

def addNumber(board):
    newBoard = board
    zeroList = []
    for i in range(16):
        if newBoard[i] == 0:
            zeroList.append(i)
    
    if len(zeroList) == 0:
        return False
    twoLocation = random.randint(0,len(zeroList)-1)
    rInt = random.randint(1,4)
    if rInt == 4:
        newBoard[twoLocation] = 4
    else:
        newBoard[twoLocation] = 2
    return newBoard

def moveSection(section):
    #will assume the section is passed in with the direction the section is moving as the first variable
    newSection = numpy.array([0,0,0,0])
    i = 0
    for n in section:
        if n != 0:
            if newSection[i - 1] == n:
                newSection[i - 1] = n * 2
            else:
                newSection[i] = n
                i += 1
    return newSection

def printBoard(board):
    printed = ""
    i = 1
    for n in board:
        printed = printed + str(n)
        if i % 4 == 0:
            printed = printed + "\n"
        else:
            printed = printed + " "
        i += 1
    return printed
