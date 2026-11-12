def saddle_points(matrix):

    if not matrix:
        return []

    result = []
    etalon = len(matrix[0])

    for row in matrix:
        if len(row) != etalon:
            raise ValueError("irregular matrix")

    for i, row in enumerate(matrix):
        for j in range(len(row)):
            if matrix[i][j] == max(matrix[i]) and matrix[i][j] == min(matrix[k][j] for k in range(len(matrix))):
                result.append({"row": i + 1, "column": j + 1})
    return result