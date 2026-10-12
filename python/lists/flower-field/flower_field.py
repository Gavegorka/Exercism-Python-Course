

def annotate(garden):
    if garden == []:
        return []

    garden_lst = []
    for row in garden:
        garden_lst.append(list(row))

    len_test = len(garden_lst[0])

    for row in range(len(garden_lst)):
        if len(garden_lst[row]) != len_test:
            raise ValueError("The board is invalid with current input.")

    for row in range(len(garden_lst)):
        for col in range(len(garden_lst[row])):
            if garden_lst[row][col] == ' ':
                garden_lst[row][col] = 0
            elif garden_lst[row][col] == '*':
                continue
            elif garden_lst[row][col] not in(' ', '*'):
                raise ValueError("The board is invalid with current input.")





    for row in range(len(garden_lst)):
        for col in range(len(garden_lst[row])):
            for row_offset in range(-1, 2):
                for col_offset in range(-1, 2):
                    neighbor_row = row + row_offset
                    neighbor_col = col + col_offset
                    if 0 <= neighbor_row < len(garden_lst) and 0 <= neighbor_col < len(garden_lst[neighbor_row]):
                        if row_offset == 0 and col_offset == 0 or garden_lst[row][col] == '*':
                            continue
                        else:
                            if garden_lst[neighbor_row][neighbor_col] == '*':
                                garden_lst[row][col] += 1

    result = []
    for row in range(len(garden_lst)):
        for col in range(len(garden_lst[row])):
            if garden_lst[row][col] == '*':
                continue
            if garden_lst[row][col] == 0:
                garden_lst[row][col] = ' '
            garden_lst[row][col] = str(garden_lst[row][col])
        result.append(''.join(garden_lst[row]))
    return result
