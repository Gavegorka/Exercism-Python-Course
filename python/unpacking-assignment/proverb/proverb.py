def proverb(*items, qualifier=None):
    if not items:
        return []
    result = []
    rows = zip(items, items[1:])
    if len(items) > 1:
        for first, second in rows:
            result.append(f'For want of a {first} the {second} was lost.')

    if qualifier is not None:
        result.append(f'And all for the want of a {qualifier} {items[0]}.')
    else:
        result.append(f'And all for the want of a {items[0]}.')
    return result