def square_root(number):
    left = 0
    right = number
    while left <= right:
        mid = (left + right) // 2
        if mid * mid == number:
            return mid
        elif mid * mid < number:
            left = mid + 1
        else:
            right = mid - 1
    return None