def primes(number):
    if number < 2:
        return []

    numbers = list(range(number + 1))
    is_primes = [True] * len(numbers)
    is_primes[0] = False
    is_primes[1] = False

    for i in range(2, int(number ** 0.5) + 1):
        if is_primes[i]:
            for j in range(i * i, number + 1, i):
                is_primes[j] = False

    return [n for n in numbers if is_primes[n]]