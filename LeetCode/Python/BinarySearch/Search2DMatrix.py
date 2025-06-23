def searchMatrix(matrix, target):
    matrix = [item for sublist in matrix for item in sublist]

    left, right = 0, len(matrix) - 1

    while left <= right:
        mid = (left + right) // 2
        if matrix[mid] == target:
            return True
        elif matrix[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]

target = 3
##MMaybe redo this without flattening, so treating as an actual 2d matrix going throuhg rows n columns

print(searchMatrix(matrix, target))