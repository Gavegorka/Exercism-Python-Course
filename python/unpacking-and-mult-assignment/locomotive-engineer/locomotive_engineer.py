"""Functions which helps the locomotive engineer to keep track of the train."""


def get_list_of_wagons(*args):
    """Return a list of wagons, given an arbitrary amount of wagon numbers.

    Parameters:
        An arbitrary number of wagon numbers, unpacked.

    Returns:
        list: A list of wagon numbers.
    """
    return [*args]


def fix_list_of_wagons(each_wagons_id, missing_wagons):
    """Fix the list of wagons.

    Parameters:
        each_wagons_id (list[int]): The list of wagons.
        missing_wagons (list[int]): The list of missing wagons.

    Returns:
        list[int]: The corrected list of wagons.
    """
    first_two = each_wagons_id[:2]
    each_wagons_id = each_wagons_id[2:]
    
    index = each_wagons_id.index(1)
    
    wagons = [
        *each_wagons_id[:index + 1],
        *missing_wagons,
        *each_wagons_id[index + 1:],
        *first_two
    ]
    
    return wagons


def add_missing_stops(route, **kwargs):
    """Add missing stops to route dict.

    Parameters:
        route (dict): The dict of routing information.
        (dict): An arbitrary number of stops.

    Returns:
        dict: The updated route dictionary.
    """

    route["stops"] = list(kwargs.values())
    return route


def extend_route_information(route, more_route_information):
    """Extend route information with more_route_information.

    Parameters:
        route (dict): The route information.
        more_route_information (dict): The extra route information.

    Returns:
        dict: The extended route information.
    """
    return {**route, **more_route_information}

def fix_wagon_depot(wagons_rows):
    """Fix the list of rows of wagons.

    Parameters:
        wagons_rows (list[list[tuple]]): The list of rows of wagons.

    Returns:
        list[list[tuple]]: the list of rows of wagons.
    """
    result = []
    for i in range(len(wagons_rows)):
        row = []
        for j in range(len(wagons_rows[0])):
            row.append(wagons_rows[j][i])
        result.append(row)

    return result
