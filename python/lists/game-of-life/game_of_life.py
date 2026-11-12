def tick(matrix):
    result = []
    for row in range(len(matrix)):
        new_row = []
        for col in range(len(matrix[row])):
            alive_neighbors = 0
            for row_offset in range(-1, 2):
                for col_offset in range(-1, 2):
                    neighbor_row = row + row_offset
                    neighbor_col = col + col_offset
                    if 0 <= neighbor_row < len(matrix) and 0 <= neighbor_col < len(matrix[neighbor_row]):
                        if row_offset == 0 and col_offset == 0:
                            continue
                        if matrix[neighbor_row][neighbor_col] == 1:
                            alive_neighbors += 1


            if alive_neighbors in (2, 3) and matrix[row][col] == 1:
                 new_row.append(1)
            elif matrix[row][col] == 0 and alive_neighbors == 3:
                new_row.append(1)
            else:
                new_row.append(0)
        result.append(new_row)
    return result