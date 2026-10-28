numbers = {
    1: 'One',
    2: 'Two',
    3: 'Three',
    4: 'Four',
    5: 'Five',
    6: 'Six',
    7: 'Seven',
    8: 'Eight',
    9: 'Nine',
    10: 'Ten',
}


def recite(start, take=1):
    result = []
    for i in range(take):
        if start - i == 1:
            result.append(f'{numbers[start - i]} green bottle hanging on the wall,')
            result.append(f'{numbers[start - i]} green bottle hanging on the wall,')
            result.append('And if one green bottle should accidentally fall,')
            result.append(f"There'll be no green bottles hanging on the wall.")
        elif start - i == 2:
            result.append(f'{numbers[start - i]} green bottles hanging on the wall,')
            result.append(f'{numbers[start - i]} green bottles hanging on the wall,')
            result.append('And if one green bottle should accidentally fall,')
            result.append(f"There'll be one green bottle hanging on the wall.")
        else:
            result.append(f'{numbers[start - i]} green bottles hanging on the wall,')
            result.append(f'{numbers[start - i]} green bottles hanging on the wall,')
            result.append('And if one green bottle should accidentally fall,')
            result.append(f"There'll be {numbers[start - i - 1].lower()} green bottles hanging on the wall.")
        if i != take - 1:
            result.append(f'')
    return result