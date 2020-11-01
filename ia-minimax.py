from copy import deepcopy

X = 'x'
O = 'o'
BLANK = ''
B = BLANK

X_WIN = 'Le joueur X gagne'
O_WIN = 'Le joueur O gagne'
DRAW = 'MAtch nul'

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
        for child in self.children:
            if len(child.children) == 0: #Si l'enfant n'a pas d'enfant
                if evalBoard(child.board) == minPlayer:
                    child.value = -1
                elif evalBoard(child.board) == DRAW:
                    child.value = 0
                elif evalBoard(child.board) == maxPlayer:
                    child.value = 1
                childrenValues.append(child.value)
            else:
                childrenValues.append(child.evalValue(minPlayer, maxPlayer))
        minValue = 1
        print(childrenValues)
        for i in childrenValues:
            if i < minValue:
                minValue = i
        print(minValue)
        return minValue

                

"""def setTreeValue(node, minPlayer, maxPlayer): #Calculate the value of all node in tree. min is human, max is computer
    childValues = list()
    for child in node.children:
        if len(child.children) == 0:
            if evalBoard(child.board) == minPlayer:
                child.value = -1
            elif evalBoard(child.board) == DRAW:
                child.value = 0
            elif evalBoard(child.board) == maxPlayer:
                child.value = 1
            childValues.append(child.value)
            print(childValues)
        else:
            setTreeValue(child, minPlayer, maxPlayer)
"""




board = [
    [X, O, X],
    [O, O, X],
    [B, B, B]
]

mainNode = Node(board, X, 0)
mainNode.evalValue(O, X)

