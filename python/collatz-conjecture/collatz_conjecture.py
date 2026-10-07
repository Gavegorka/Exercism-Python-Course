"""Function that checks amount of steps folowing the Collatz Conjecture for a given number
Only positive number allowed, if even -> divide by two, odd -> multiply by 3 and add 1"""


def steps(number):
    """
    How many steps does it take to reach 1 flowing Collatz Conjecture for a given number

    Arguments:
        number(int) - only positive numbers allowed, number to start Collatz algo

    Returns:
        int - amount of steps to reach 1 from given number with Collatz Conjecture
    """


    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    amount_of_steps = 0

    while number != 1:
        if number % 2 == 0:
            number = number // 2
        else:
            number = number * 3 + 1

        amount_of_steps += 1

    return amount_of_steps
