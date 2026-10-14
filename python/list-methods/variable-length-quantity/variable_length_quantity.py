def encode(numbers):
    result = []

    for number in numbers:
        number_i = []
        if number == 0:
            number_i.append(number)

        while number != 0:
            byte = number & 0x7F

            number >>= 7
            number_i.append(byte)
        number_i = number_i[::-1]
        for i in range(len(number_i) - 1):
            number_i[i] = number_i[i] | 0x80
        result.extend(number_i)

    return result


def decode(bytes):
    result = []
    number = 0
    for byte in bytes:
        number <<= 7
        number |= byte & 0x7F
        if byte & 0x80 == 0:
            result.append(number)
            number = 0
    if bytes and bytes[-1] & 0x80:
        raise ValueError("incomplete sequence")
    return result