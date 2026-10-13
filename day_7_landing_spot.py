def find_landing_spot(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == 0:
                print([row, column], (matrix[row].index(matrix[row][column])))
            # if matrix[row][column] == 0 and ((matrix[row].index(matrix[row][column]) == 0) or (matrix[row].index(matrix[row][column]) == (len(matrix[row]) - 1))):
            #     print(row, column)
            # if matrix[row][column] == 0:
            #     print(row, column)

    # return matrix

print(find_landing_spot([
    [1, 2, 1], 
    [0, 0, 2], 
    [3, 0, 0]]))