class Game:
    def __init__(self):
        self.board = [
            ['x', '', ''],
            ['', 'o', ''],
            ['', '', '']
        ]
        self.current_player = "x"
    
    def getBoard(self, i=None, j=None):
        if i != None and j != None:
            return self.board[i][j]
        else:
            return self.board

    def change_player(self):
        if self.current_player == "x":
            self.current_player = "o"
        else:
            self.current_player = "x"

    def move(self, i, j):
        self.board[i][j] = self.current_player
        self.change_player()
    
    def is_there_winner(self):
        sums = list() #each elements is a sum of one col, one row or one diagonal
        for i in range(3): #Column
            sums.append(self.board[i][0] + self.board[i][1] + self.board[i][2])

        for j in range(3): #Row
            sums.append(self.board[0][j] + self.board[1][j] + self.board[2][j])
        
        sums.append(self.board[0][0] + self.board[1][1] + self.board[2][2]) #Diag leftToRight
        
        sums.append(self.board[0][2] + self.board[1][1] + self.board[2][0]) #Diag rightToLeft

        for sum in sums:
            if sum == 'xxx' or sum == 'ooo':
                return True

        
        return False