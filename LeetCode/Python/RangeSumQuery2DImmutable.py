class NumMatrix:

    def __init__(self, matrix):
        self.matrix = matrix
        self.col = len(matrix[0])
        self.row = len(matrix)
        self.prefixSum = [[0] * (self.col + 1) for _ in range(self.row + 1)]
        print(self.prefixSum)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        pass



x = NumMatrix([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]])