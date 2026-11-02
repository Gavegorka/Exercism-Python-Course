def sum_of_multiples(limit, multiples):
    result = set()

    for item in multiples:
        if item == 0:
            continue

        for i in range(item, limit, item):
            result.add(i)

    return sum(result)