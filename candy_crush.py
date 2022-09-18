from typing import List
"""
`board` representing the grid of candy where board[i][j] represents the type of candy. 
board[i][j] == 0 represents that the cell is empty.

The given board represents the state of the game following the player's move. 
Now, you need to restore the board to a stable state by crushing candies according the RULES:

-   If three or more candies of the same type are adjacent vertically or horizontally,
    crush them all at the same time - these positions become empty.

-   After crushing all candies simultaneously, if an empty space on the board has candies on top of itself,
    then these candies will drop until they hit a candy or bottom at the same time. 
    No new candies will drop outside the top boundary.

-   After the above steps, there may exist more candies that can be crushed. 
    If so, you need to repeat the above steps.

-   If there does not exist more candies that can be crushed (i.e., the board is stable), 
    then return the current board.

** You need to perform the above rules until the board becomes stable, then return the stable board.

https://assets.leetcode.com/uploads/2018/10/12/candy_crush_example_2.png

Ex:
Input: board = [[1,3,5,5,2],[3,4,3,3,1],[3,2,4,5,2],[2,4,4,5,5],[1,4,4,1,1]]
Output: [[1,3,0,0,0],[3,4,0,5,2],[3,2,0,3,1],[2,4,0,5,2],[1,4,3,1,1]]
"""
from collections import defaultdict


class Solution:

    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        # Make board globally accesible without having to pass around through methods
        self.board = board
        # init stable to false
        stable = False
        while not stable:
            flips = self.scan()
            # if there are flips to make, crush them, and edit board
            if flips:
                self.crush(flips)
                self.gravity()
            else:
                stable = True

        return self.board

    def scan(self) -> defaultdict[set]:

        # Row num is index and cols are the flips
        flips = defaultdict(set)

        for r, row in enumerate(self.board):
            for c, val in enumerate(row):

                val = self.board[r][c]
                if val == 0:
                    continue

                # Row scan
                offset = 1
                row_count = 1
                while c + offset < len(self.board[0]):
                    if self.board[r][c + offset] == val:
                        row_count += 1
                        offset += 1
                    else:
                        break

                # Col scan
                offset = 1
                col_count = 1
                while r + offset < len(self.board):
                    if self.board[r + offset][c] == val:
                        col_count += 1
                        offset += 1
                    else:
                        break

                # Map flips in the defaultdict using the row as key only if value counts are greater than 3
                if row_count >= 3:
                    for i in range(row_count):
                        flips[r].add(c + i)

                if col_count >= 3:
                    for i in range(col_count):
                        flips[r + i].add(c)

        return flips if len(flips) > 0 else None

    def crush(self, flips: defaultdict[set]):
        # Edit flips to 0 ahead of gravity
        for row in flips:
            for col in flips[row]:
                self.board[row][col] = 0

    def gravity(self):
        n_cols = len(self.board[0])
        m_rows = len(self.board)
        # Since the gravity happens to top to bottom and each row is a list
        # Create a list that represents the column
        for col in range(n_cols):
            col_values = []

            for row in range(m_rows):
                col_values.append(self.board[row][col])

            # if there is a 0 we may need to edit
            if 0 in col_values:
                # create a list of non zero values and pad the left with zeros
                non_zero_vals = [x for x in col_values if x != 0]
                len_diff = m_rows - len(non_zero_vals)
                zeros = [0] * len_diff
                new_col = zeros + non_zero_vals

                # rebuild with new_col after edit
                for row, val in enumerate(new_col):
                    self.board[row][col] = val



