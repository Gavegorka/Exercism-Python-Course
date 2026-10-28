roman_numerals = {
    1000: 'M',
    900: 'CM',
    500: 'D',
    400: 'CD',
    100: 'C',
    90: 'XC',
    50: 'L',
    40: 'XL',
    10: 'X',
    9: 'IX',
    5: 'V',
    4: 'IV',
    1: 'I'
}


def roman(number):
    result = ''
    while number > 0:
        for key, value in roman_numerals.items():
            if number >= key:
                number -= key
                result += value
                break
    return result