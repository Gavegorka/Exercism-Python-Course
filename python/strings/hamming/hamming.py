def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("Strands must be of equal length.")
    else:
        errors = 0
        for char in range(len(strand_a)):
            if strand_a[char] != strand_b[char]:
                errors += 1
    return errors