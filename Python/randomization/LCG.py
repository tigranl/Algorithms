def lcg(a: int, b: int, m: int, k: int):
    x = 0
    i = 0
    print(x)
    while k != i:
        n = (a * x + b) % m
        print(n)
        x = n
        i += 1
