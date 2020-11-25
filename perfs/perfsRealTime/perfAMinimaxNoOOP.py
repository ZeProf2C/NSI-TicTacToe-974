import timeit

IMPORT = '''
from copy import deepcopy
from random import randint

from head import X, O, HUMAN, COMPUTER, BLANK, B

inf = 999
    '''


CODE = '''
def isWin(board, player):
    winStates = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[2][0], board[1][1], board[0][2]],
    ]

    if [player, player, player] in winStates:
        return True
    return False

def eval(board):
    if isWin(board, COMPUTER):
        return 1
    elif isWin(board, HUMAN):
        return -1
    else:
        return 0

def getEmpty(board):
    cells = list()
    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == BLANK:
                cells.append([i, j])
    return cells

def isPlayable(i, j, board):
    if board(i, j) == BLANK:
        return True
    return False

def minimax(board, depth, player):
    if player == COMPUTER: #On initialise le meilleur coup avec une position nulle et une valeure infiniment éloignée de ce qu'on veut
        best = [-1, -1, -inf]
    else:
        best = [-1, -1, +inf]
    
    if depth == 0 or eval(board) != 0:
        score = eval(board)
        return [-1, -1, score]

    for cell in getEmpty(board):
        i, j = cell[0], cell[1]
        board[i][j] = player
        nextPlayer = X if player == O else O
        score = minimax(board, depth-1, nextPlayer)
        board[i][j] = BLANK
        score[0], score[1] = i, j

        if player == COMPUTER: #on maximise le computer et minimise le human
            if score[2] > best[2]:
                best = score 
        else:
            if score[2] < best[2]:
                best = score
    return best

def aiPlay(board):
    depth = len(getEmpty(board))
    if depth == 0:
        return None

    if depth == 9: #Si l'ordi commence
        i, j = randint(0, 2), randint(0, 2)
        value = None
    else:
        i, j, value = minimax(board, depth, COMPUTER) 

    return i, j, value

board = [
    [X, B, B],
    [B, B, B],
    [B, B, B]
]

aiPlay(board)

'''

moy = 0
i = 0
for meas in range(1):
    moy += timeit.timeit(setup=IMPORT, stmt=CODE, number=1)
    i += 1

moy = moy/i
print(moy)