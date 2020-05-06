import numpy
from run2048 import createBoard, moveSection, makeMove, addNumber, printBoard

def test_createBoard_returns_array():
    assert type(createBoard()) == type(numpy.array([]))

def test_createBoard_has_2():
    has2 = 0
    array = createBoard()
    for x in array:
        if x == 2:
            has2 += 1
    assert has2 == 2

def test_moveSection_returns_array4():
    assert moveSection(numpy.array([0,0,0,0])).size == 4

def test_moveSection_adds_numbers():
    assert all(moveSection(numpy.array([2,2,0,0])) == numpy.array([4,0,0,0]))
    assert all(moveSection(numpy.array([2,0,2,0])) == numpy.array([4,0,0,0]))
    assert all(moveSection(numpy.array([2,0,0,2])) == numpy.array([4,0,0,0]))

    assert all(moveSection(numpy.array([2,2,2,0])) == numpy.array([4,2,0,0]))
    assert all(moveSection(numpy.array([2,2,0,2])) == numpy.array([4,2,0,0]))

    assert all(moveSection(numpy.array([2,2,2,2])) == numpy.array([4,4,0,0]))
    assert all(moveSection(numpy.array([4,2,2,0])) == numpy.array([4,4,0,0]))

    assert all(moveSection(numpy.array([0,0,2,2])) == numpy.array([4,0,0,0]))

def test_makeMove_returns_board():
    assert makeMove(numpy.array([0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]), "N").size == 16

def test_makeMove_returns_correct():
    assert all(makeMove(numpy.array([2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,0]), "N") == numpy.array([4,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
    assert all(makeMove(numpy.array([2,0,0,0,2,0,0,0,0,0,0,0,0,0,0,4]), "N") == numpy.array([4,0,0,4,0,0,0,0,0,0,0,0,0,0,0,0]))
    assert all(makeMove(numpy.array([2,0,0,0,0,2,0,0,0,0,2,0,0,0,0,2]), "N") == numpy.array([2,2,2,2,0,0,0,0,0,0,0,0,0,0,0,0]))
    assert all(makeMove(numpy.array([2,2,0,0,2,2,0,0,0,0,0,0,0,0,0,0]), "N") == numpy.array([4,4,0,0,0,0,0,0,0,0,0,0,0,0,0,0]))
    assert all(makeMove(numpy.array([2,0,0,0,0,2,0,0,0,0,2,0,0,0,0,2]), "E") == numpy.array([0,0,0,2,0,0,0,2,0,0,0,2,0,0,0,2]))
    assert all(makeMove(numpy.array([2,0,0,0,0,2,0,0,0,0,2,0,0,0,0,2]), "S") == numpy.array([0,0,0,0,0,0,0,0,0,0,0,0,2,2,2,2]))
    assert all(makeMove(numpy.array([2,0,0,0,0,2,0,0,0,0,2,0,0,0,0,2]), "W") == numpy.array([2,0,0,0,2,0,0,0,2,0,0,0,2,0,0,0]))

def test_addNumber_adds_new_2_or_4():
    board = addNumber(numpy.array([2,0,0,0,0,2,0,0,0,0,2,0,0,0,0,2]))
    nonZeroCount = 0
    for n in board:
        if n !=0 and (n == 4 or n == 2):
            nonZeroCount += 1
    assert nonZeroCount == 5

def test_addNumber_fails():
    board = addNumber(numpy.array([2,4,8,16,16,8,4,2,2,4,8,16,16,8,4,2]))
    assert board == False

def test_printBoard():
    printedBoard = printBoard(numpy.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
    assert printedBoard == "1 2 3 4\n5 6 7 8\n9 10 11 12\n13 14 15 16\n"