from copy import deepcopy

X_WIN = 'Le joueur X gagne'
O_WIN = 'Le joueur O gagne'
DRAW = 'Match nul'

X = 'x'
O = 'o'
BLANK = ' '
B = BLANK

def eval_pos(board, turn):
    possibilities = list()
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == BLANK:
                copy = deepcopy(board)
                copy[i][j] = turn
                possibilities.append(copy)
    return possibilities

def eval_state(board):
    sums = list()
    for i in range(3):
        sums.append(
            board[i][0] + board[i][1] + board[i][2]
            )
    for j in range(3):
        sums.append(
            board[0][j] + board[1][j] + board[2][j]
            )
    sums.append(
        board[0][0] + board[1][1] + board[2][2]
    )
    sums.append(
        board[0][2] + board[1][1] + board[2][0]
    )
    
    for sum in sums:
        if sum == X+X+X:
            return X_WIN
        elif sum == O+O+O:
            return O_WIN
    return DRAW

def is_full(board):
    for row in board:
        try:
            print(row.index(''))
            return False
        except ValueError:
            return True

def solve_tree(board, player):
    playing = player
    waiting = O if player==X else X
    branch = eval_pos(board, playing)
    for game in branch:
        if eval_state(game) == X_WIN:
            print(X_WIN)
            for i in game:
                print(i)
        elif eval_state(game) == O_WIN:
            print(O_WIN)
            for i in game:
                print(i)
        else:
            if not is_full(board):
                print('recursiv')
                solve_tree(game, waiting)
            else:
                print(eval_state(board))
                for i in game:
                    print(i)

print(solve_tree(
    [
        [X,B,O],
        [B,O,X],
        [X,O,X]
    ],
    X
))