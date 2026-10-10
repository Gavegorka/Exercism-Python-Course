def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    if output_base < 2:
        raise ValueError("output base must be >= 2")

    if any(dig < 0 or dig >= input_base for dig in digits):
        raise ValueError("all digits must satisfy 0 <= d < input base")

    if digits == [] or all(dig == 0 for dig in digits):
        return [0]

    number_in_ten = []
    power = len(digits) - 1
    for digit in digits:
        number_in_ten.append(digit * (input_base ** power))
        power -= 1


    chast = sum(number_in_ten)
    ost_lst = []
    
    while chast != 0:
        ost_lst.append(chast % output_base)
        chast = chast // output_base

    return ost_lst[::-1]