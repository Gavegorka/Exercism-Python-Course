def slices(series, length):
    if not series:
        raise ValueError("series cannot be empty")
    elif length == 0:
        raise ValueError("slice length cannot be zero")
    elif length < 0:
        raise ValueError("slice length cannot be negative")
    elif length > len(series):
        raise ValueError("slice length cannot be greater than series length")


    result = []

    for i in range(len(series)):
        if i <= len(series) - length:
            result.append(series[i:i+length])
    return result