import timeit

IMPORT = '''
from copy import deepcopy
from random import randint

from head import X, O, HUMAN, COMPUTER, BLANK, B

inf = 999
    '''


CODE = '''
def test_vertical(plateau,joueur):
    return any(plateau[0][j] == plateau[1][j] == plateau[2][j] == joueur for j in range(3))

def test_diagonales(plateau,joueur):
    return all(plateau[i][i] == joueur for i in range(3)) or all(plateau[2-i][i] == joueur for i in range(3))
    
def test_horizontal(plateau,joueur):
    return any(all(plateau[lig][col] == joueur for col in range(3))for lig in range(3))
            
def isWin(plateau,joueur):
    return test_horizontal(plateau,joueur) or test_vertical(plateau,joueur) or test_diagonales(plateau,joueur)

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

#aiPlay(board)

isWin(board, X)
'''

moy = 0
i = 0
for meas in range(1000):
    moy += timeit.timeit(setup=IMPORT, stmt=CODE, number=1)
    i += 1

moy = moy/i
print(moy*1000000)