"""Is the year a leap year?"""


def leap_year(year):

    """
    Function:
        determines is the given year a lap yearm to be such it needs to be divisible by 4, and by 400 but not by 100

    Arguments:
        year (int) - year to check

    Returns:
        bool - is the given year a leap year
    """

    if year % 4 != 0:
        return False

    if year % 100 != 0:
        return True

    if year % 400 == 0:
        return True

    return False
    
