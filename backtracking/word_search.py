class Solution:
    def is_valid(self, i, j, board):
        return 0 <= i < len(board) and 0 <=j < len(board[0])
    
    def exist(self, board, word: str):
        # Your code goes here
        def w_search(visited,  i, j, index):
            directions = [[-1, 0], [1, 0], [0, 1], [1, 0]]
            
            for x in range(len(directions)):
                for y in range(len(directions[0])):
                    if (i + x, j + y) in visited:
                        continue
                    if self.is_valid(i+x, j+y, board) and board[i + x][j + y] == word[index]:
                        visited.add((i, j))
                        if w_search(visited,  i + x, j + y, index + 1):
                            return True
                        visited.remove((i, j))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if w_search(set(), i, j, 1):
                        return True
        return False
    
    def dfs_exist(self, board, word):
        rows, cols = len(board), len(board[0])

        def dfs(r, c, index):
            if index == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[index]:
                return False

            temp = board[r][c]
            board[r][c] = "#"

            found = (
                dfs(r+1, c, index+1) or
                dfs(r-1, c, index+1) or
                dfs(r, c+1, index+1) or
                dfs(r, c-1, index+1)
            )

            board[r][c] = temp
            return found

        # initialize depth-first search from
        # each of the cells that have the same first
        # letter as word
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if dfs(row, col, 0):
                        return True
        return False


board = [
    ['B', 'L', 'C', 'H'],
    ['D', 'E', 'L', 'T'],
    ['D', 'A', 'K', 'A'],
]
word = "BLEAD"
print(Solution().dfs_exist(board, word))