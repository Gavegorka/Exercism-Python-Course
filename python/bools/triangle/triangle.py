"""
These functions can determine if a triangle is equilateral, isosceles, or scalene.

Rules for a valid triangle:
    1. All sides must be > 0.
    2. The sum of any two sides must be >= the third side (degenerate triangles allowed).
"""


def _is_valid_triangle(sides):
    """
    Check if the given sides can form a valid triangle.

    A valid triangle must have all sides > 0 and satisfy the triangle 
    inequality theorem (non-strict, allowing degenerate triangles).

    Args:
        sides (list): A list of three numbers representing the sides.

    Returns:
        bool: True if the sides form a valid triangle, False otherwise.
    """
    if len(sides) != 3:
        return False

    a, b, c = sides

    # Rule 1: All sides must be positive
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # Rule 2: Triangle inequality theorem (non-strict for degenerate triangles)
    return a + b >= c and b + c >= a and c + a >= b


def equilateral(sides):
    """
    Determine if the triangle is equilateral (all three sides are equal).

    Args:
        sides (list): A list of three numbers representing the sides.

    Returns:
        bool: True if the triangle is equilateral, False otherwise.
    """
    if not _is_valid_triangle(sides):
        return False

    a, b, c = sides
    return a == b == c


def isosceles(sides):
    """
    Determine if the triangle is isosceles (at least two sides are equal).

    Note: An equilateral triangle is also considered isosceles.

    Args:
        sides (list): A list of three numbers representing the sides.

    Returns:
        bool: True if the triangle is isosceles, False otherwise.
    """
    if not _is_valid_triangle(sides):
        return False

    a, b, c = sides
    return a == b or b == c or c == a


def scalene(sides):
    """
    Determine if the triangle is scalene (all sides are different).

    Args:
        sides (list): A list of three numbers representing the sides.

    Returns:
        bool: True if the triangle is scalene, False otherwise.
    """
    if not _is_valid_triangle(sides):
        return False

    a, b, c = sides
    return a != b and b != c and c != a