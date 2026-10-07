"""Function that can determine what number is an Armstrong number
(number that is the sum of its own digits each raised to the power of the number of digits.)"""


def is_armstrong_number(number):
    """

    Note:
        I'll make a bool cond that make a comparsion between given number and the number I got with calculations

    Arguments:
        number (int) - number to chekc if it is an Armstrong number

    Returns:
        bool - is the number an Armstrong numbers
    """

    def armstrong_alg(number_to_check_in_alg):

        """Inner function that calculates the number with armstrong algorithm"""

        calced_number = 0

        for digit in str(number_to_check_in_alg):
            calced_number += int(digit) ** len(str(number_to_check_in_alg))
        return calced_number

    armstrong_cond = number == armstrong_alg(number)  # are given number and calced number equal

    return armstrong_cond