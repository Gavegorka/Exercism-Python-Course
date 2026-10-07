"""Function for calculating amount of seeds on the chessboard from the legeng about servant and prince """
def square(number):
    """Function calculates the number of seeds on the given to function square on the chessboard

    Argument:
        number (int) - nubmer of the square

    Returns:
        int - how many seeds are on the square
    
    Exception:
        There's only 64 squares on the chessboard so if the given number is more than 64 or less than one,
        func will raise a Value Error
    """
    seeds_on_the_square = 2 ** (number - 1) # how many seeds are on the square
    if number > 64 or number < 1:
        raise ValueError("square must be between 1 and 64")
    return seeds_on_the_square

def total():
    """Function calculates how many seeds are on the board total
    
    Returns:
        int - how many seeds are on the board
        """
    total_seeds = 2 ** 64 - 1 # how many seeds are on the board | sum of geom. progression
    return total_seeds