"""
Questions
Input
["size_of_board", "move", "move", "move", "move", "move", "move", "move"]
[[3], [0, 0, 1], [0, 2, 2], [2, 2, 1], [1, 1, 2], [2, 0, 1], [1, 0, 2], [2, 1, 1]]
Output
[null, 0, 0, 0, 0, 0, 0, 1]


Rules:
1. Once a winning condition is reached, no more moves are allowed.
2. valid move is when you place X 0 in empty cell
"""


class TicTacToe(object):
    """
    + we will use projection Method to Design this.
    + We know tic-tac-toe is 2 players game
    and offset is 1 for `playerA` & offset is -1 for `playerB`.
    """

    def __init__(self, n: int):
        # n is the size of the board
        self.n = n
        
        # projection variable
        self.row, self.col = [0]*n, [0]*n
        self.diag, self.anti_diag = 0, 0
        
        # --not in use---
        # mapping player'id to offset
        self.offset_map = {
            1:1,
            2:-1,
        }

    def move(self, row, col, player: int):
        # (row, col) is the move made by player (id)
        offset = player * 2 - 3  # smart move, converting id's -> offset 
        self.row[row] += offset
        self.col[col] += offset
        
        if row == col:
            self.diag += offset
        
        if row + col == self.n - 1:
            self.anti_diag += offset
        
        if self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 2
        
        if -self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 1
        
        return 0

# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)



# Brute Force
def __init__(self, n: int):
        self.board = [[0 for i in range(n)] for j in range(n)]
        self.n = n
        

    def move(self, row: int, col: int, player: int) -> int:
        self.board[row][col] = player
        r_count = 0
        for i in range(self.n):
            if self.board[i][col] == player:
                r_count+=1
        
        if r_count == self.n: return player
        
        c_count = 0
        for i in range(self.n):
            if self.board[row][i] == player:
                c_count +=1
            
        if c_count == self.n:
            return player
        
        l_diagonal = 0
        for i in range(self.n):
            if self.board[i][i] == player:
                l_diagonal+=1
        
        if l_diagonal == self.n: return player
        
        r_diagonal = 0
        j = 0
        for i in range(self.n-1,-1,-1):
            if self.board[i][j] == player:
                r_diagonal+=1
            j+=1
        
        if r_diagonal == self.n: return player

        return 0
