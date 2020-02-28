# given a 2d matrix, find the minimum sum path to get to the bottom right,
# can only move right or down
# 5 9 10
# 2 8 12
# 7 2 1

input = [
    [5, 9, 10, 5, 11],
    [2, 8, 12, 17, 1],
    [7, 2, 1, 4, 8],
    [12, 9, 8, 11, 4],
    [7, 2, 1, 4, 5]
]

def min_cost(matrix, m, n):
    min_matrix = [[0 for x in range(m+1)] for y in range(n+1)]
    min_matrix[0][0] = matrix[0][0]

    # populate first column and first row
    for i in range(1, n+1):
        min_matrix[i][0] = min_matrix[i-1][0] + matrix[i][0]
    for j in range(1, m+1):
        min_matrix[0][j] = min_matrix[0][j-1] + matrix[0][j]

    for i in range(1, n+1):
        for j in range(1, m+1):
            left_cost = min_matrix[i-1][j]
            above_cost = min_matrix[i][j-1]
            min_matrix[i][j] = matrix[i][j] + min(left_cost,above_cost)
    for row in min_matrix:
        print(row)

    return min_matrix[n][m]

print(min_cost(input, 2, 2))

