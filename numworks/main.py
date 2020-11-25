#!/usr/bin/env python3
from ion import *
from kandinsky import *

WIDTH = 320
HEIGHT = 240

X = 'x'
O = 'o'
BLANK = ''
B = BLANK
X_WIN = 'Le joueur X gagne'
O_WIN = 'Le joueur O gagne'
DRAW = 'Match nul'
ONGOING = 'Des coups sont encore possibles'
WIN = 'Un joueur à gagné'
HUMAN = X
COMPUTER = O

inf = 999

def isWin(board, player): #2 fois moins longs que des for, 4 fois moins que des any/all
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
        i, j = 1, 1
    else:
        i, j, value = minimax(board, depth, COMPUTER) 

    return i, j, value

score = [0,0]
j = 0 #Joueur0 commence

while 1:
  Jeu = [" "]*9
  fin = 0

  draw_string("Appuyez sur EXE",84,42,(160,0,255))

  while not (keydown(KEY_EXE) or keydown(KEY_OK)):True

  fill_rect(62,25,255,190,'white')
  for a in range(65,160,30):
    fill_rect(65-3,a+8,91,1,'orange')
    fill_rect(a-3,73,1,90,'orange')

  draw_string("Joueur0 : "+str(score[0]),170,100,'blue')
  draw_string("Joueur1 : "+str(score[1]),170,120,'green')

  while fin == 0: #Tant que personne n'a gagné
    k = 9
    while k == 9: #Tant que le tour n'est pas joué
      if keydown(KEY_ONE) and Jeu[6] == " ":
        k = 6
      elif keydown(KEY_TWO) and Jeu[7] == " ":
        k = 7
      elif keydown(KEY_THREE) and Jeu[8] == " ":
        k = 8
      elif keydown(KEY_FOUR) and Jeu[3] == " ":
        k = 3
      elif keydown(KEY_FIVE) and Jeu[4] == " ":
        k = 4
      elif keydown(KEY_SIX) and Jeu[5] == " ":
        k = 5
      elif keydown(KEY_SEVEN) and Jeu[0] == " ":
        k = 0
      elif keydown(KEY_EIGHT) and Jeu[1] == " ":
        k = 1
      elif keydown(KEY_NINE) and Jeu[2] == " ":
        k = 2
    Jeu[k] = j #Le tour est joue
    aiPlay()
    draw_string(str(j),72+30*(k%3),80+30*(k//3),'red')

    j = 1-j #Changement de joueur

    gagnant = 2 #Pas de gagnant
    for k in range(3):
      if Jeu[0+3*k] in [0,1] and Jeu[0+3*k] == Jeu[1+3*k] == Jeu[2+3*k]:
        gagnant = Jeu[0+3*k]
      if Jeu[0+k] in [0,1] and Jeu[0+k] == Jeu[3+k] == Jeu[6+k]:
        gagnant = Jeu[0+k]
    if Jeu[0] in [0,1] and Jeu[0] == Jeu[4] == Jeu[8]:
      gagnant = Jeu[0]
    elif Jeu[2] in [0,1] and Jeu[2] == Jeu[4] == Jeu[6]:
      gagnant = Jeu[2]
    if gagnant < 2:
      draw_string("Joueur"+str(gagnant)+" a gagné",84,25,'red')
      score[gagnant] += 1
      draw_string("Joueur"+str(gagnant)+" : "+str(score[gagnant]),170,100+20*gagnant,'red')
      fin = 1
    elif Jeu.count(0)+Jeu.count(1) == 9 and fin == 0:
      draw_string("Personne n'a gagné",68,25)
      fin = 1
