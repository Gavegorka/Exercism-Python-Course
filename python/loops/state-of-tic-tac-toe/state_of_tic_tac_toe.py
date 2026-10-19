def row_win(grid):
    winner = []

    for row in grid:
        if all(el == 'X' for el in row):
            winner.append('X')
        if all(el == 'O' for el in row):
            winner.append('O')

    return winner


def col_win(grid):
    winner = []

    for j in range(3):
        el_control = grid[0][j]

        if el_control == ' ':
            continue

        same = True

        for i in range(1, len(grid)):
            if grid[i][j] != el_control:
                same = False
                break

        if same and el_control in ['X', 'O']:
            winner.append(el_control)

    return winner


def diag_win(grid):
    winner = []

    el_control = grid[0][0]
    if el_control in ['X', 'O']:
        if grid[1][1] == el_control and grid[2][2] == el_control:
            winner.append(el_control)

    el_control = grid[0][2]
    if el_control in ['X', 'O']:
        if grid[1][1] == el_control and grid[2][0] == el_control:
            winner.append(el_control)

    return winner


def gamestate(board):
    quant_x = 0
    quant_o = 0

    for row in board:
        for el in row:
            if el == 'X':
                quant_x += 1
            elif el == 'O':
                quant_o += 1

    row_result = row_win(board)
    col_result = col_win(board)
    diag_result = diag_win(board)

    winners = []
    winners.extend(row_result)
    winners.extend(col_result)
    winners.extend(diag_result)

    if 'X' in winners and 'O' in winners:
        raise ValueError('Impossible board: game should have ended after the game was won')

    if quant_o > quant_x:
        raise ValueError('Wrong turn order: O started')

    if quant_x > quant_o + 1:
        raise ValueError('Wrong turn order: X went twice')

    if 'X' in winners and quant_x != quant_o + 1:
        raise ValueError('Impossible board: game should have ended after the game was won')

    if 'O' in winners and quant_x != quant_o:
        raise ValueError('Impossible board: game should have ended after the game was won')

    if winners:
        return 'win'

    if quant_x + quant_o == 9:
        return 'draw'

    return 'ongoing'