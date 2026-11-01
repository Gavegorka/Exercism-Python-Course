import math as m

def cipher_text(plain_text):
    data = ''.join(char for char in plain_text.lower() if char.isalpha() or char.isdigit())
    if data == '':
        return data
    r = m.floor(m.sqrt(len(data)))
    c = m.ceil(len(data) / r)
    while c - r > 1:
        r += 1
        c = m.ceil(len(data) / r)
    rows = []

    for i in range(0, len(data), c):
        rows.append(data[i:i + c])
    rows[-1] += ' ' * (c - len(rows[-1]))


    cipher = ''
    for j in range(len(rows[0])):
        for i in range(len(rows)):
            cipher += rows[i][j]
    result = []
    for i in range(0, len(cipher), r):
        result.append(cipher[i:i + r])
    return ' '.join(result)

