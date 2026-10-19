digits = {
    ' _ | ||_|   ': '0',
    '     |  |   ': '1',
    ' _  _||_    ': '2',
    ' _  _| _|   ': '3',
    '   |_|  |   ': '4',
    ' _ |_  _|   ': '5',
    ' _ |_ |_|   ': '6',
    ' _   |  |   ': '7',
    ' _ |_||_|   ': '8',
    ' _ |_| _|   ': '9',
}

def convert(input_grid):
    result = ''
    if len(input_grid) % 4 != 0:
        raise ValueError('Number of input lines is not a multiple of four')
    for row in input_grid:
        if len(row) % 3 != 0:
            raise ValueError('Number of input columns is not a multiple of three')

    quant_symbols = len(input_grid[0]) // 3
    quant_groups = len(input_grid) // 4

    for j in range(quant_groups):
        for i in range(quant_symbols):
            symbol = ''
            for k in range(4):
                symbol += input_grid[j * 4 + k][i * 3:i * 3 + 3]

            if symbol in digits:
                result += digits[symbol]
            else:
                result += '?'

        if j != quant_groups - 1:
            result += ','
    return result