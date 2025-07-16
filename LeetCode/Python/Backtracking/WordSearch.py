def exist(board, word):

    ROWS, COLS = len(board), len(board[0])
    visited = [[False for _ in range(COLS)] for _ in range(ROWS)]

    def backtrack(r,c,i):
        if i == len(word):
            return True

        if (r< 0 or c < 0 or r >= ROWS or c >= COLS or word[i] != board[r][c] or visited[r][c]):
            return False

        visited[r][c] = True
        res = (backtrack(r + 1, c, i + 1) or
               backtrack(r - 1, c, i + 1) or
               backtrack(r, c + 1, i + 1) or
               backtrack(r, c - 1, i + 1))
        visited[r][c] = False
        return res

    for r in range(ROWS):
        for c in range(COLS):
            if backtrack(r, c, 0):
                return True
    return False



board = [
  ["A","B","C","D"],
  ["S","A","A","T"],
  ["A","C","A","E"]
]
word = "CAT"

print(exist(board,word))