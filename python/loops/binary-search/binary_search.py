def find(search_list, value):
    search_list_sorted = sorted(search_list)
    if value not in search_list:
        raise ValueError("value not in array")
    low = 0
    high = len(search_list_sorted) - 1
    while low <= high:
        mid = (low + high) // 2
        if search_list_sorted[mid] == value:
            return mid
        elif search_list_sorted[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return None