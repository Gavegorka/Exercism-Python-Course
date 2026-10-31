def line_up(name, number):
    last_digit = number % 10
    last_two = number % 100
    if last_digit == 1 and last_two != 11:
        return f'{name}, you are the {number}st customer we serve today. Thank you!'
    elif last_digit == 2 and last_two != 12:
        return f'{name}, you are the {number}nd customer we serve today. Thank you!'
    elif last_digit == 3 and last_two != 13:
        return f'{name}, you are the {number}rd customer we serve today. Thank you!'
    return f'{name}, you are the {number}th customer we serve today. Thank you!'