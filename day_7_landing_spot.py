def find_landing_spot(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[0])):
            if matrix[row][column] == 0:
                print(row, column)

    return matrix

print(find_landing_spot([
    [9, 0, 3], 
    [7, 0, 4], 
    [8, 0, 5],
    ]))