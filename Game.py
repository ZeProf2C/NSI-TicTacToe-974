from head import *


class Game:
    def __init__(self):
        self.board = [
            [B, B, B],
            [B, B, B],
            [B, B, B]
        ]
        self.current_player = HUMAN
        self.wait_player = COMPUTER
        self.win_player = str()
    
    def get_board(self, i=None, j=None):
        if i != None and j != None:
            return self.board[i][j]
        else:
            return self.board

    def change_player(self):
        self.current_player, self.wait_player = self.wait_player, self.current_player

    def move(self, i, j):
        if self.board[i][j] == BLANK:
            self.board[i][j] = self.current_player
            self.change_player()
            return True
        return False
    
    def is_there_winner(self):
        winStates = [
            [self.board[1][0], self.board[1][1], self.board[1][2]],
            [self.board[0][0], self.board[0][1], self.board[0][2]],
            [self.board[2][0], self.board[2][1], self.board[2][2]],
            [self.board[0][0], self.board[1][0], self.board[2][0]],
            [self.board[0][1], self.board[1][1], self.board[2][1]],
            [self.board[0][2], self.board[1][2], self.board[2][2]],
            [self.board[0][0], self.board[1][1], self.board[2][2]],
            [self.board[2][0], self.board[1][1], self.board[0][2]],
        ]

        if [X, X, X] in winStates:
            self.win_player = X
            return True
        elif [O, O, O] in winStates:
            self.win_player = O
            return True
        return False

    def winner(self):
        return self.win_player if self.is_there_winner() else False

    def no_winner(self):
       
        for i in range(3): #Column
            for j in range(3): #Row
                if self.board[i][j] == BLANK:
                    return False
        return True if self.winner()==False else False

    def get_state(self):
        if self.winner():
            return WIN
        elif self.no_winner():
            return DRAW
        else:
            return ONGOING