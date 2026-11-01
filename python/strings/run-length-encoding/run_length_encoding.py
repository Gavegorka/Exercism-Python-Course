def decode(string):
    if string == '':
        return ''

    result = ''
    count = ''
    current = ''
    for char in string:
        if char.isdigit():
            count += char
        else:
            current = char
            if count:
                count = int(count)
            else:
                count = 1
            result += f'{current * count}'
            current, count = '', ''
    return result
def encode(string):
    if string == '':
        return ''

    result = ''
    current = string[0]
    count = 1
    for char in string[1:]:
        if char == current:
            count += 1
        else:
            if count > 1:
                result += f'{count}{current}'
            else:
                result += f'{current}'
            current = char
            count = 1
    if count > 1:
        result += f'{count}{current}'
    else:
        result += f'{current}'
    return result