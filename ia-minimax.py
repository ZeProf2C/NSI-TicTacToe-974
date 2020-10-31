from copy import deepcopy

X = 'x'
O = 'o'
BLANK = ''
B = BLANK

X_WIN = 'Le joueur X gagne'
O_WIN = 'Le joueur O gagne'
DRAW = 'MAtch nul'

def playable(board):
    if win(board) is None:
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
    return None

def isFull(board):
    for i in board:
        for j in board:
            if j == '':
                return False
    return True
    

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

def exploreNode(node):
    possible = list()
    for child in node.children:
        if len(child.children) == 0:
            possible.append(child.board)
        else:
            possible.append(exploreNode(child))
    return possible

board = [
    [X, O, X],
    [O, O, X],
    [B, B, B]
]

mainNode = Node(board, X, 0)
mainNode.createChildren()
explore = exploreNode(mainNode)

for game in explore:
    for row in game:
        print(row)
    print('\n')
