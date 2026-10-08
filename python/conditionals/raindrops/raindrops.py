"""Determine if the given number is divisible by 3, 5 or 7."""


def convert(number):

    """
    Function determines if the given number is divisible by 3, 5 or 7

    Args:
        number (int) - number to check

    Returns:
        str - combination of 'Plong', 'Pling', 'Plang'
        If a given number:
            is divisible by 3, add "Pling" to the result.
            is divisible by 5, add "Plang" to the result.
            is divisible by 7, add "Plong" to the result.
            is not divisible by 3, 5, or 7, the result should be the number as a string.

    """
    number = int(number)
    answer = []
    
    if number % 3 != 0 and number % 5 != 0 and number % 7 != 0:
        return str(number)
        
    if number % 3 == 0:
        answer.append("Pling")
        
    if number % 5 == 0:
        answer.append("Plang")
        
    if number % 7 == 0:
        answer.append("Plong")
        
    return "".join(answer)
