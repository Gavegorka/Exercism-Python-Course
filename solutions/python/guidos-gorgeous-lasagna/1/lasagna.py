"""Functions used in preparing Guido's gorgeous lasagna.

Learn about Guido, the creator of the Python language:
https://en.wikipedia.org/wiki/Guido_van_Rossum

This is a module docstring, used to describe the functionality
of a module and its functions and/or classes.
"""


#TODO (student): define your EXPECTED_BAKE_TIME (required) and PREPARATION_TIME (optional) constants below.
EXPECTED_BAKE_TIME = 40
PREPARATION_TIME  = 2

#TODO (student): Remove 'pass' and complete the 'bake_time_remaining()' function below.
def bake_time_remaining(time_in_oven):
    """Calculate the bake time remaining.

    Parameters:
        elapsed_bake_time (int): The baking time already elapsed.

    Returns:
        int: The remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    elapsed_bake_time = EXPECTED_BAKE_TIME - time_in_oven
    return elapsed_bake_time


def preparation_time_in_minutes(number_of_layers):
    
    """Calculate the time to prepare lasagna with the number of layers
    
    Parametrs: 
        number_of_layers (int) - how many layers I want my lasagna to have
        
    Returns:
        int: Time I need to prepare lasagna with that many layers i want and gave to function
    
    Function that takes the number of layers i want my lasagna to be with and calculating the amount of time i need
    to prepare my lasagna by multiplicating number of layers and 'PREPARATION_TIME' - the amount of time I need to prepare one layer"""

    return (number_of_layers * PREPARATION_TIME)

    
def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):
    """Calculate the elapsed cooking time.
    
    Parameters:
        number_of_layers (int): The number of layers in the lasagna.
        elapsed_bake_time (int): Time the lasagna has been baking in the oven.
    
    Returns:
        int: The total time elapsed (in minutes) preparing and baking.

    This function takes two integers representing the number of lasagna 
    layers and the time already spent baking the lasagna. It calculates 
    the total elapsed minutes spent cooking (preparing + baking).
    
    """
    return number_of_layers * PREPARATION_TIME + elapsed_bake_time


    