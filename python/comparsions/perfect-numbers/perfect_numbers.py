def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError('Classification is only possible for positive integers.')

    sum_div = sum(div for div in range(1, number) if number % div == 0)
    if number < 1:
        raise ValueError

        
    if sum_div == number:
        return 'perfect'
    elif sum_div > number:
        return 'abundant'
    return 'deficient'
