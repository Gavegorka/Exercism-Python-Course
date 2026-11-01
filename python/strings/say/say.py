ones = {
    0: "zero",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}

tens = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

scales = ['', 'thousand', 'million', 'billion']

def groups(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")

    number_lst = []
    while number > 0:
        number_lst.append(number % 1000)
        number = number // 1000

    return number_lst


def say_hundreds(number):
    result = ''
    hundreds = number // 100
    digits = number % 100

    if hundreds > 0:
        result += f'{ones[hundreds]} hundred'
    if 0 < digits < 20:
        if result:
            result += ' '
        result += ones[digits]
    elif digits >= 20:
        if result:
            result += ' '
        result += tens[digits // 10]
        if digits % 10 != 0:
            result += f'-{ones[digits % 10]}'

    return result


def say(number):
    if number < 0 or number > 999999999999:
        raise ValueError("input out of range")
    if number == 0:
        return 'zero'
    result = []

    for i, item in enumerate(groups(number)):
        if item == 0:
            continue
        if scales[i]:
            result.append( f'{say_hundreds(item)} {scales[i]}')
        else:
            result.append(f'{say_hundreds(item)}')
    return ' '.join(reversed(result))