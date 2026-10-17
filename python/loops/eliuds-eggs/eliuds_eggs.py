def egg_count(display_value):
    count = 0
    number = display_value
    while number:
        if number & 1:
            count += 1
        number >>= 1
    return count