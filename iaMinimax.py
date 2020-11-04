from head import *
from copy import deepcopy

def playable(board):
    if not win(board):
        return True
    else: 
        return False

def win(board):
    sums = list() #each elements is a sum of one col, one row or one diagonal
    for i in range(3): #Column
        sums.append(board[i][0] + board[i][1] + board[i][2])

    for j in range(3): #Row
        sums.append(board[0][j] + board[1][j] + board[2][j])
    
    sums.append(board[0][0] + board[1][1] + board[2][2]) #Diag leftToRight
    sums.append(board[0][2] + board[1][1] + board[2][0])

    for sum in sums:
        if sum == X+X+X:
            return X_WIN
        elif sum == O+O+O:
            return O_WIN
    return False

def isFull(board):
    for i in board:
        for j in board:
            if j == BLANK:
                return False
    return True

def drawGame(board):
    if isFull(board) and not win(board):
        return  DRAW
    else:
        return False

def evalBoard(board):
    if win(board) == X_WIN:
        return X
    elif win(board) == O_WIN:
        return O
    elif drawGame(board) == DRAW:
        return DRAW
    else:
        return False
    
def jolieBoard(board):
    for row in board:
        print(row)
    print('\n')

def bestBoard(mainNode):
    lastValue = mainNode.children[0].value
    bestBoard = mainNode.children[0].board
    for child in mainNode.children:
        if child.value > lastValue:
            lastValue = child.value
            bestBoard = child.board
    return bestBoard

def knowTurn(board, computer, human): #Définis un certains nombre d'état (vide, premier coup...) pour éviter les calculs
    c = computer
    h = human
    boards = [
        [[B, B, B],[B, B, B],[B, B, B]],
        [[h, B, B],[B, B, B],[B, B, B]],
        [[B, h, B],[B, B, B],[B, B, B]],
        [[B, B, h],[B, B, B],[B, B, B]],
        [[B, B, B],[h, B, B],[B, B, B]],
        [[B, B, B],[B, h, B],[B, B, B]],
        [[B, B, B],[B, B, h],[B, B, B]],
        [[B, B, B],[B, B, B],[h, B, B]],
        [[B, B, B],[B, B, B],[B, h, B]],
        [[B, B, B],[B, B, B],[B, B, h]]
    ]
    for boardModel in boards:
        if board <= boardModel:
            if board[1][1] == BLANK:
                return 1, 1
            else:
                return 0, 0
    return False


class Node():
    def __init__(self, board, turn, depth):
        self.board = board
        self.turn = turn
        self.depth = depth
        self.children = list()
        self.value = None
        self.createChildren()

    def createChildren(self):
        if playable(self.board):
            for i in range(3):
                for j in range(3):
                    if self.board[i][j] == BLANK:
                        copy = deepcopy(self.board)
                        copy[i][j] = self.turn
                        self.children.append(
                            Node(
                                copy,
                                X if self.turn == O else O,
                                self.depth-1
                            )
                        )
    def evalValue(self, minPlayer, maxPlayer):
        childrenValues = list()
        bestValue = 0
        if self.turn == maxPlayer:
            playing = maxPlayer
            waiting = minPlayer
            maximising = True
        else:
            playing = minPlayer
            waiting = maxPlayer
            maximising = False

        for child in self.children:
            if len(child.children) == 0: #Si l'enfant n'a pas d'enfant
                if evalBoard(child.board) == minPlayer:
                    child.value = -100-self.depth
                    childrenValues.append(child.value)
                elif evalBoard(child.board) == maxPlayer:
                    child.value = 100+self.depth
                    childrenValues.append(child.value)
            else:
                childrenValues.append(child.evalValue(minPlayer, maxPlayer))

        for i in childrenValues:
            if maximising:
                if i > bestValue:
                    bestValue = i
            elif not maximising:
                if i < bestValue:
                    bestValue = i
        self.value = bestValue
        return bestValue

"""board = [
    [O, X, X],
    [X, O, O],
    [B, B, B]
]

mainNode = Node(board, X, 0)
mainNode.evalValue(O, X)
board = bestBoard(mainNode)
jolieBoard(board)"""



def minimax(board, computer, human):
    if knowTurn(board, computer, human):
        return knowTurn(board, computer, human)
    mainNode = Node(board, computer, 0)
    mainNode.evalValue(human, computer)
    newBoard = bestBoard(mainNode)
    for i in range(len(newBoard)):
        for j in range(len(newBoard[i])):
            if newBoard[i][j] != board[i][j]:
                del mainNode
                return i, j