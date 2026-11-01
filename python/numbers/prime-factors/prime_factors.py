def factors(value):
    result = []
    number = value
    factor = 2

    while factor * factor <= number:
        while number % factor == 0:
            result.append(factor)
            number //= factor
        factor += 1

    if number > 1:
        result.append(number)

    return result