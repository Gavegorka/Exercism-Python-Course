from math import gcd

def triplets_with_sum(number):
    triplets = []
    for m in range(2, int((number / 2) ** 0.5) + 1):
        for n in range(1, m):
            if m % 2 != n % 2 and gcd(m, n) == 1:
                if number % (2 * m * (m + n)) == 0:
                    k = number // (2 * m * (m + n))
                    a = (m ** 2 - n ** 2) * k
                    b = (2 * m * n) * k
                    c = (m ** 2 + n ** 2) * k
                    triplets.append([min(a, b), max(a,b), c])
    return triplets