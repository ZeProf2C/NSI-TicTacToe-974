class Game:
    def __init__(self):
        self.board = [
            ['X', '', ''],
            ['', 'O', ''],
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