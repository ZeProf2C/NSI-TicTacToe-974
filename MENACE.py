from head import *
from Game import *
from minimax import getEmpty,isPlayable
from copy import deepcopy
import pickle

def get_ia_moves (board):
    human = []
    computer = []
    for line in range(len(board)):
        for case in range(len(board[line])):
            if board[line][case] == COMPUTER:
                computer.append(case + line * 3)
    for line in range(len(board)):
        for case in range(len(board[line])):
            if board[line][case] == HUMAN:
                human.append(case + line * 3)
                
    return [computer,human]

def signature(board):
    return tuple(sum(2**move for move in player) for player in board)   

def sym_vert(board):
    sym={0:2,1:1,2:0,3:5,4:4,5:3,6:8,7:7,8:6}
    return [[sym[move] for move in player] for player in board]

def rot_dir(board):
    rot={0:6,1:3,2:6,3:7,4:4,5:1,6:8,7:5,8:2}
    return [[rot[move] for move in player] for player in board]

def equivalent(sign,board):
    rep=False
    for sym in range(2):
        for rot in range(4):
            if sign==signature(board):
                rep=True
            board=rot_dir(board)
        board=sym_vert(board)
    return rep

def rech_sign_equi(board,config):
    for sign in config.keys():
        if equivalent(sign,board):
            return sign
    return None



def init_menace():
    pickle.dump({}, open('menace', 'wb'))
    return {}

def load_menace():
    config = pickle.load(open('menace', 'rb'))
    return config
    
def save_menace(config):
    pickle.dump(config, open('menace', 'wb'))

def get_possible_moves(board,config):
    list_moves = {}
    move = []
    sign = []
    for i in getEmpty(board):
        move = deepcopy(board)
        move[i[0]][i[1]] = COMPUTER
        move = get_ia_moves(move)
        sign=rech_sign_equi(move,config)
        if sign==None:
            sign=signature(move)
            config[sign] = 0
        list_moves[sign] = i
    return list_moves

        
def ai_menace_play (board,hist,config):
    possibleMoves = get_possible_moves(board,config)
    bestMove = next(iter(possibleMoves.keys()))
    for sign in possibleMoves:
        if config[bestMove] < config[sign]:
            bestMove = sign
    hist.append(bestMove)
    return possibleMoves[bestMove][0],possibleMoves[bestMove][1]

def ai_reward(intens,hist,config):
    for sign in hist:
        config[sign] += intens
    hist = []
    save_menace(config)
        
init_menace()
