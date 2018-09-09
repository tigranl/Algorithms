from math import sqrt


def prime_factors(num):
    f = []
    while num % 2 == 0:
        f.append(2)
        num = num // 2
    i = 3
    m = sqrt(num)
    while i <= m:
        while num % i == 0:
            f.append(i)
            num = num // i
        i += 2
    if num > 1:
        f.append(num)
    return f
