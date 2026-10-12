ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def rows(letter):
    diamond = []
    index = ALPHABET.index(letter) + 1
    for i in range(index):
        if i == 0:
            diamond.append(f'{' ' * (index - i - 1)}'
                           f'{ALPHABET[i]}{' ' * (2 * i - 1)}'
                           f'{' ' * (index - i - 1)}')
        else:
            diamond.append(f'{' ' * (index - i - 1)}'
                           f'{ALPHABET[i]}{' ' * (2 * i  - 1)}'
                           f'{ALPHABET[i]}'
                           f'{' ' * (index - i - 1)}')

    for i in range(index - 2, -1, -1):
        if i == 0:
            diamond.append(f'{' ' * (index - i - 1)}'
                           f'{ALPHABET[i]}{' ' * (2 * i - 1)}'
                           f'{' ' * (index - i - 1)}')
        else:
            diamond.append(f'{' ' * (index - i - 1)}'
                           f'{ALPHABET[i]}{' ' * (2 * i - 1)}'
                           f'{ALPHABET[i]}'
                           f'{' ' * (index - i - 1)}')
    return diamond