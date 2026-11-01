def is_prime(number):
    if number < 2:
        return False

    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False

    return True

def prime(number):
    if number == 0:
        raise ValueError('there is no zeroth prime')
    
    count = 0
    candidate = 0
    while count < number:
        if is_prime(candidate):
            count += 1
        candidate += 1
    return candidate - 1