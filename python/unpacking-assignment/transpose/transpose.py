def transpose(text):
    data = text.split('\n')
    original = data.copy()
    row = len(data)
    col = len(max(data, key=len))
    result = []
    for j in range(col):
        string = ''
        for i in range(row):
            if j < len(original[i]):
                string += data[i][j]
            elif any(j < len(line) for line in data[i + 1:]):
                string += ' '
        result.append(string)


    return '\n'.join(result)